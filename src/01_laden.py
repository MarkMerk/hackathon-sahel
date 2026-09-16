"""01_laden.py — Rohdaten laden und data/processed/panel.csv erzeugen.

Quellen (manuell nach data/raw/ geladen, siehe DATA_DOWNLOAD.md):
  - World Bank WDI: NY.GDP.TOTL.RT.ZS (Rohstoffrenten), NY.GDP.PCAP.KD (BIP p. c.),
    EG.ELC.ACCS.ZS (Stromzugang) sowie die Metadatendatei mit der Regionszuordnung.
  - ICTD/UNU-WIDER Government Revenue Dataset (GRD): Total Resource Revenue, Resource taxes.
  - UNDP HDR: Human Development Index.

Ausgabe: data/processed/panel.csv exakt nach dem Schema in docs/Forschungsdesign.md §4.
Keine Interpolation, keine Extrapolation — fehlende Werte bleiben leer.

Aufruf: python src/01_laden.py
"""

from __future__ import annotations

import sys
import unicodedata
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
OUT = ROOT / "data" / "processed" / "panel.csv"

JAHR_VON, JAHR_BIS = 2000, 2021

SAHEL = ["MLI", "BFA", "NER", "TCD", "MRT"]
SAHEL_EXT = SAHEL + ["SDN", "SEN"]
OELSTAATEN = ["NGA", "AGO", "GNQ", "COG", "GAB", "SSD", "TCD"]

RENTEN_MINDESTNIVEAU = 1.0  # Capture Ratio nur bei Renten >= 1 % BIP
RATIO_FLAG_GRENZE = 1.5


# ---------------------------------------------------------------------------
# Hilfsfunktionen
# ---------------------------------------------------------------------------


def finde_datei(muster: str) -> Path:
    """Genau eine Datei zu einem Glob-Muster in data/raw/ finden."""
    treffer = sorted(RAW.glob(muster))
    if not treffer:
        raise FileNotFoundError(
            f"Keine Datei zum Muster '{muster}' in {RAW}. "
            "Siehe DATA_DOWNLOAD.md — Datei fehlt oder ist anders benannt."
        )
    if len(treffer) > 1:
        # Neueste nach Dateiname (enthält das Datum) verwenden, aber sichtbar machen.
        print(f"  Hinweis: mehrere Dateien zu '{muster}': "
              f"{[p.name for p in treffer]} → verwende {treffer[-1].name}")
    return treffer[-1]


def normalisiere(text: str) -> str:
    """Spaltennamen vergleichbar machen: klein, ohne Akzente, ohne Sonderzeichen."""
    text = unicodedata.normalize("NFKD", str(text))
    text = "".join(z for z in text if not unicodedata.combining(z))
    return "".join(z for z in text.lower() if z.isalnum())


def waehle_spalte(df: pd.DataFrame, kandidaten: list[str], zweck: str) -> str:
    """Erste passende Spalte finden — erst exakt, dann als Teilstring.

    Die GRD- und HDR-Dateien benennen ihre Spalten je nach Version unterschiedlich.
    Statt einen Namen fest zu verdrahten, prüfen wir eine Liste plausibler Varianten
    und brechen mit einer aussagekräftigen Meldung ab, wenn keine passt.
    """
    karte = {normalisiere(s): s for s in df.columns}

    for kandidat in kandidaten:
        if (schluessel := normalisiere(kandidat)) in karte:
            return karte[schluessel]

    for kandidat in kandidaten:
        schluessel = normalisiere(kandidat)
        for norm_name, original in karte.items():
            if schluessel in norm_name:
                print(f"  Hinweis: {zweck} → Spalte '{original}' "
                      f"(unscharfer Treffer für '{kandidat}')")
                return original

    raise KeyError(
        f"Keine Spalte für {zweck} gefunden. Gesucht: {kandidaten}. "
        f"Vorhanden: {list(df.columns)[:40]}"
    )


def lies_wdi(pfad: Path, wertname: str) -> pd.DataFrame:
    """WDI-CSV im Breitformat (Jahre als Spalten) einlesen und in Langformat bringen.

    Die Datei der World Bank hat vier Kopfzeilen vor der eigentlichen Tabelle.
    """
    for kopfzeilen in (4, 0, 2, 3, 5):
        df = pd.read_csv(pfad, skiprows=kopfzeilen, encoding="utf-8-sig")
        if "Country Code" in df.columns:
            break
    else:
        raise ValueError(f"'Country Code' in {pfad.name} nicht gefunden.")

    jahresspalten = [s for s in df.columns if str(s)[:4].isdigit()
                     and JAHR_VON <= int(str(s)[:4]) <= JAHR_BIS]

    lang = df.melt(
        id_vars=["Country Name", "Country Code"],
        value_vars=jahresspalten,
        var_name="year",
        value_name=wertname,
    )
    lang["year"] = lang["year"].astype(str).str[:4].astype(int)
    lang = lang.rename(columns={"Country Code": "iso3", "Country Name": "country"})
    lang[wertname] = pd.to_numeric(lang[wertname], errors="coerce")
    return lang[["iso3", "country", "year", wertname]]


def lies_tabelle(pfad: Path) -> pd.DataFrame:
    """Excel, Stata oder CSV einlesen — je nach Dateiendung.

    Die UNDP-HDR-Datei ist nicht UTF-8 kodiert (Ländernamen wie „Côte d'Ivoire“),
    deshalb werden mehrere Kodierungen der Reihe nach versucht.
    """
    suffix = pfad.suffix.lower()
    if suffix in {".xlsx", ".xls"}:
        blaetter = pd.read_excel(pfad, sheet_name=None)
        # Das Blatt mit den meisten Zeilen ist die Datentabelle (nicht das Deckblatt).
        name, df = max(blaetter.items(), key=lambda kv: len(kv[1]))
        if len(blaetter) > 1:
            print(f"  Hinweis: {pfad.name} hat {len(blaetter)} Blätter → verwende '{name}'")
        return df
    if suffix == ".dta":
        return pd.read_stata(pfad, convert_categoricals=False)

    for kodierung in ("utf-8-sig", "latin-1"):
        try:
            df = pd.read_csv(pfad, encoding=kodierung, low_memory=False)
        except UnicodeDecodeError:
            continue
        if kodierung != "utf-8-sig":
            print(f"  Hinweis: {pfad.name} als {kodierung} gelesen (nicht UTF-8).")
        return df
    raise UnicodeDecodeError(
        "utf-8", b"", 0, 1, f"{pfad.name} ließ sich mit keiner bekannten Kodierung lesen."
    )


# ---------------------------------------------------------------------------
# Einzelne Quellen
# ---------------------------------------------------------------------------


def lade_wdi_regionen() -> pd.DataFrame:
    """ISO3-Codes der World-Bank-Region Subsahara-Afrika (SSF).

    Die Metadatendatei enthält nur echte Länder mit Region; Aggregate wie
    'Sub-Saharan Africa' selbst haben ein leeres Regionsfeld und fallen damit raus.
    """
    meta = pd.read_csv(finde_datei("wdi_country_meta_*.csv"), encoding="utf-8-sig")
    spalte_region = waehle_spalte(meta, ["Region"], "WDI-Region")
    spalte_iso = waehle_spalte(meta, ["Country Code", "iso3"], "WDI-Ländercode")

    ssa = meta[meta[spalte_region].astype(str).str.contains(
        "Sub-Saharan Africa", case=False, na=False
    )]
    codes = sorted(ssa[spalte_iso].dropna().astype(str).str.upper().unique())
    print(f"  Subsahara-Afrika: {len(codes)} Länder")
    return pd.DataFrame({"iso3": codes})


def lade_grd() -> pd.DataFrame:
    """GRD: Total Resource Revenue und Resource taxes, jeweils % BIP."""
    pfad = finde_datei("grd_*")
    print(f"  GRD-Datei: {pfad.name}")
    df = lies_tabelle(pfad)

    spalte_iso = waehle_spalte(
        df, ["ISO", "iso3", "ISO3", "Country Code", "countrycode", "iso_3"], "GRD-Ländercode"
    )
    spalte_jahr = waehle_spalte(df, ["Year", "year"], "GRD-Jahr")
    spalte_rev = waehle_spalte(
        df,
        ["Total Resource Revenue", "resource_revenue", "Resource Revenue",
         "rev_resource", "totalresourcerevenue"],
        "GRD Total Resource Revenue",
    )
    spalte_tax = waehle_spalte(
        df,
        ["Resource taxes", "resource_taxes", "tax_resource", "resourcetaxes"],
        "GRD Resource taxes",
    )

    schlank = df[[spalte_iso, spalte_jahr, spalte_rev, spalte_tax]].copy()
    schlank.columns = ["iso3", "year", "res_rev_pct_gdp", "res_tax_pct_gdp"]
    schlank["iso3"] = schlank["iso3"].astype(str).str.strip().str.upper()
    schlank["year"] = pd.to_numeric(schlank["year"], errors="coerce")
    for spalte in ("res_rev_pct_gdp", "res_tax_pct_gdp"):
        schlank[spalte] = pd.to_numeric(schlank[spalte], errors="coerce")

    schlank = schlank.dropna(subset=["iso3", "year"])
    schlank["year"] = schlank["year"].astype(int)
    schlank = schlank[schlank["year"].between(JAHR_VON, JAHR_BIS)]

    # Manche GRD-Versionen führen je Land/Jahr mehrere Zeilen (z. B. general vs.
    # central government). Wir behalten die Zeile mit der besseren Abdeckung.
    if schlank.duplicated(["iso3", "year"]).any():
        vorher = len(schlank)
        schlank = (schlank
                   .assign(_gefuellt=schlank[["res_rev_pct_gdp", "res_tax_pct_gdp"]].notna().sum(axis=1))
                   .sort_values("_gefuellt", ascending=False)
                   .drop_duplicates(["iso3", "year"], keep="first")
                   .drop(columns="_gefuellt"))
        print(f"  Hinweis: {vorher - len(schlank)} doppelte Land-Jahr-Zeilen in GRD "
              "zusammengeführt (Zeile mit mehr Werten behalten) — in der Methodik erwähnen.")

    return schlank


def lade_hdi() -> pd.DataFrame:
    """UNDP HDI aus der Datei 'All composite indices and components time series'."""
    pfad = finde_datei("hdr_composite_*")
    print(f"  HDI-Datei: {pfad.name}")
    df = lies_tabelle(pfad)

    spalte_iso = waehle_spalte(df, ["iso3", "ISO3", "country_code"], "HDR-Ländercode")

    # Breitformat: hdi_2000 ... hdi_2021
    hdi_spalten = {
        s: int(str(s).split("_")[-1])
        for s in df.columns
        if str(s).lower().startswith("hdi_")
        and str(s).split("_")[-1].isdigit()
        and JAHR_VON <= int(str(s).split("_")[-1]) <= JAHR_BIS
    }

    if hdi_spalten:
        lang = df.melt(
            id_vars=[spalte_iso],
            value_vars=list(hdi_spalten),
            var_name="_spalte",
            value_name="hdi",
        )
        lang["year"] = lang["_spalte"].map(hdi_spalten)
        lang = lang.drop(columns="_spalte")
    else:
        # Langformat als Rückfallebene
        spalte_jahr = waehle_spalte(df, ["year", "Year"], "HDR-Jahr")
        spalte_wert = waehle_spalte(df, ["hdi", "value", "Human Development Index"], "HDI-Wert")
        lang = df[[spalte_iso, spalte_jahr, spalte_wert]].copy()
        lang.columns = [spalte_iso, "year", "hdi"]

    lang = lang.rename(columns={spalte_iso: "iso3"})
    lang["iso3"] = lang["iso3"].astype(str).str.strip().str.upper()
    lang["year"] = pd.to_numeric(lang["year"], errors="coerce")
    lang["hdi"] = pd.to_numeric(lang["hdi"], errors="coerce")
    lang = lang.dropna(subset=["iso3", "year"])
    lang["year"] = lang["year"].astype(int)
    lang = lang[lang["year"].between(JAHR_VON, JAHR_BIS)]
    return lang[["iso3", "year", "hdi"]].drop_duplicates(["iso3", "year"])


# ---------------------------------------------------------------------------
# Abgeleitete Größen
# ---------------------------------------------------------------------------


def dreijahresmittel(reihe: pd.Series) -> pd.Series:
    """Zentriertes 3-Jahres-Mittel; Randjahre brauchen mindestens zwei Werte.

    Begründung (docs/Forschungsdesign.md §3): Renten folgen den Weltmarktpreisen,
    Staatseinnahmen laufen zeitverzögert nach. Die Glättung macht das Niveau
    vergleichbar, ohne Werte zu erfinden.
    """
    return reihe.rolling(window=3, center=True, min_periods=2).mean()


def periode(jahr: int) -> str:
    if jahr <= 2007:
        return "2000–2007"
    if jahr <= 2014:
        return "2008–2014"
    return "2015–2021"


# ---------------------------------------------------------------------------
# Ablauf
# ---------------------------------------------------------------------------


def main() -> int:
    print("01_laden.py — Panel aufbauen")
    print(f"Rohdaten aus: {RAW}")

    print("\n[1/5] WDI einlesen")
    renten = lies_wdi(finde_datei("wdi_rents_*.csv"), "rents_pct_gdp")
    gdppc = lies_wdi(finde_datei("wdi_gdppc_*.csv"), "gdppc_const")
    strom = lies_wdi(finde_datei("wdi_elec_*.csv"), "elec_access_pct")

    print("\n[2/5] Region Subsahara-Afrika bestimmen")
    ssa = lade_wdi_regionen()

    print("\n[3/5] GRD und HDI einlesen")
    grd = lade_grd()
    hdi = lade_hdi()

    print("\n[4/5] Zusammenführen (ISO3 × Jahr)")
    panel = (
        ssa.merge(renten, on="iso3", how="left")
        .merge(gdppc[["iso3", "year", "gdppc_const"]], on=["iso3", "year"], how="left")
        .merge(strom[["iso3", "year", "elec_access_pct"]], on=["iso3", "year"], how="left")
        .merge(grd, on=["iso3", "year"], how="left")
        .merge(hdi, on=["iso3", "year"], how="left")
    )
    panel = panel.dropna(subset=["year"])
    panel["year"] = panel["year"].astype(int)
    panel = panel[panel["year"].between(JAHR_VON, JAHR_BIS)]

    print("\n[5/5] Kennzahlen berechnen")
    panel["sahel"] = panel["iso3"].isin(SAHEL)
    panel["sahel_ext"] = panel["iso3"].isin(SAHEL_EXT)
    panel["oil_state"] = panel["iso3"].isin(OELSTAATEN)

    # Capture Ratio nur, wenn die Renten mindestens 1 % des BIP betragen —
    # bei kleinerem Nenner wird der Quotient instabil.
    genug_renten = panel["rents_pct_gdp"] >= RENTEN_MINDESTNIVEAU
    panel["capture_ratio"] = np.where(
        genug_renten & panel["res_rev_pct_gdp"].notna(),
        panel["res_rev_pct_gdp"] / panel["rents_pct_gdp"],
        np.nan,
    )

    panel = panel.sort_values(["iso3", "year"]).reset_index(drop=True)
    panel["capture_ratio_3y"] = (
        panel.groupby("iso3")["capture_ratio"].transform(dreijahresmittel)
    )
    panel["flag_ratio_high"] = panel["capture_ratio"] > RATIO_FLAG_GRENZE
    panel["period"] = panel["year"].map(periode)

    spalten = [
        "iso3", "country", "year", "sahel", "sahel_ext", "oil_state",
        "rents_pct_gdp", "res_rev_pct_gdp", "res_tax_pct_gdp",
        "gdppc_const", "elec_access_pct", "hdi",
        "capture_ratio", "capture_ratio_3y", "flag_ratio_high", "period",
    ]
    panel = panel[spalten]

    OUT.parent.mkdir(parents=True, exist_ok=True)
    panel.to_csv(OUT, index=False, encoding="utf-8")

    print(f"\nGeschrieben: {OUT.relative_to(ROOT)}")
    print(f"  {len(panel)} Länderjahre, {panel['iso3'].nunique()} Länder, "
          f"{panel['year'].min()}–{panel['year'].max()}")
    print(f"  mit Renten: {panel['rents_pct_gdp'].notna().sum()}")
    print(f"  mit Ressourceneinnahmen (GRD): {panel['res_rev_pct_gdp'].notna().sum()}")
    print(f"  mit Capture Ratio: {panel['capture_ratio'].notna().sum()}")
    print(f"  davon > {RATIO_FLAG_GRENZE} (geflaggt): {int(panel['flag_ratio_high'].sum())}")

    fehlend = [c for c in SAHEL if c not in set(panel["iso3"])]
    if fehlend:
        print(f"\n  WARNUNG: Sahel-Kernländer fehlen im Panel: {fehlend}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
