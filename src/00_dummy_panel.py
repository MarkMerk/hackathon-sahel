#!/usr/bin/env python3
# ============================================================================
#  ACHTUNG: DUMMY-DATEN — NICHT FUER ERGEBNISSE VERWENDEN
# ============================================================================
#  Dieses Skript erzeugt data/processed/panel_dummy.csv mit *erfundenen*
#  Zufallswerten im exakten Schema aus docs/Forschungsdesign.md §4.
#  Zweck: Die Analyseskripte src/04_*, src/05_*, src/06_* koennen entwickelt
#  und getestet werden, bevor Marks echte data/processed/panel.csv vorliegt.
#
#  KEINE Zahl aus dieser Datei oder aus darauf basierenden Tabellen und
#  Abbildungen darf in results/zahlen.md oder in den Text uebernommen werden.
#  Die Gruppenunterschiede sind willkuerlich gesetzt, nicht empirisch.
#
#  Autor: Philip · AI Hackathon JLU, 16.09.2026
#  Aufruf: python src/00_dummy_panel.py
# ============================================================================

from pathlib import Path

import numpy as np
import pandas as pd

SEED = 20260916
OUT = Path("data/processed/panel_dummy.csv")
YEARS = range(2000, 2022)  # Analysefenster 2000-2021 (Forschungsdesign §1)

# Gruppendefinitionen (Forschungsdesign §3 und §4) -- identisch zum echten Panel
SAHEL = ["MLI", "BFA", "NER", "TCD", "MRT"]
SAHEL_EXT_ADD = ["SDN", "SEN"]  # sahel_ext = SAHEL + diese beiden
OIL_STATES = ["NGA", "AGO", "GNQ", "COG", "GAB", "SSD", "TCD"]

# Laender der World-Bank-Region Subsahara-Afrika (SSF), ISO3 + WDI-Name.
COUNTRIES = {
    "AGO": "Angola",
    "BEN": "Benin",
    "BWA": "Botswana",
    "BFA": "Burkina Faso",
    "BDI": "Burundi",
    "CPV": "Cabo Verde",
    "CMR": "Cameroon",
    "CAF": "Central African Republic",
    "TCD": "Chad",
    "COM": "Comoros",
    "COD": "Congo, Dem. Rep.",
    "COG": "Congo, Rep.",
    "CIV": "Cote d'Ivoire",
    "GNQ": "Equatorial Guinea",
    "ERI": "Eritrea",
    "SWZ": "Eswatini",
    "ETH": "Ethiopia",
    "GAB": "Gabon",
    "GMB": "Gambia, The",
    "GHA": "Ghana",
    "GIN": "Guinea",
    "GNB": "Guinea-Bissau",
    "KEN": "Kenya",
    "LSO": "Lesotho",
    "LBR": "Liberia",
    "MDG": "Madagascar",
    "MWI": "Malawi",
    "MLI": "Mali",
    "MRT": "Mauritania",
    "MUS": "Mauritius",
    "MOZ": "Mozambique",
    "NAM": "Namibia",
    "NER": "Niger",
    "NGA": "Nigeria",
    "RWA": "Rwanda",
    "STP": "Sao Tome and Principe",
    "SEN": "Senegal",
    "SYC": "Seychelles",
    "SLE": "Sierra Leone",
    "SOM": "Somalia",
    "ZAF": "South Africa",
    "SSD": "South Sudan",
    "SDN": "Sudan",
    "TZA": "Tanzania",
    "TGO": "Togo",
    "UGA": "Uganda",
    "ZMB": "Zambia",
    "ZWE": "Zimbabwe",
}


def periode(jahr: int) -> str:
    """Periodenzuordnung nach Forschungsdesign §3 (Gedankenstrich wie im Schema)."""
    if jahr <= 2007:
        return "2000–2007"
    if jahr <= 2014:
        return "2008–2014"
    return "2015–2021"


def baue_panel(rng: np.random.Generator) -> pd.DataFrame:
    """Erzeugt das Laenderjahr-Panel mit laenderspezifischen Niveaus und
    einem gemeinsamen Weltmarktpreis-Zyklus (Renten sind preisgetrieben)."""

    # Gemeinsamer Preiszyklus: Rohstoffboom 2005-2013, danach Abschwung.
    jahre = np.array(list(YEARS))
    zyklus = 1.0 + 0.35 * np.sin((jahre - 2000) / 22 * 2 * np.pi)

    zeilen = []
    for iso3, name in COUNTRIES.items():
        ist_sahel = iso3 in SAHEL
        ist_oel = iso3 in OIL_STATES

        # Laenderspezifisches Rentenniveau: Oelstaaten deutlich hoeher.
        if ist_oel:
            renten_niveau = rng.uniform(15, 35)
        elif ist_sahel:
            renten_niveau = rng.uniform(4, 20)
        else:
            renten_niveau = rng.uniform(0.2, 18)

        # WILLKUERLICH gesetzter Abschoepfungsgrad -- kein empirischer Befund.
        # Leichter Sahel-Nachteil, damit die Tests etwas zu rechnen haben.
        basis_quote = rng.normal(0.32 if ist_sahel else 0.40, 0.10)
        basis_quote = float(np.clip(basis_quote, 0.05, 0.95))

        hdi_niveau = rng.uniform(0.28, 0.62)
        strom_niveau = rng.uniform(5, 85)
        gdppc_niveau = rng.uniform(300, 6000)

        for i, jahr in enumerate(jahre):
            # --- Rohstoffrenten (% BIP), WDI NY.GDP.TOTL.RT.ZS ---
            renten = renten_niveau * zyklus[i] * rng.normal(1.0, 0.12)
            renten = float(np.clip(renten, 0.0, 40.0))

            # --- Ressourceneinnahmen (% BIP), GRD Total Resource Revenue ---
            # Einnahmen folgen den Renten mit einem Jahr Verzoegerung.
            renten_vorjahr = renten if i == 0 else zeilen[-1]["rents_pct_gdp"]
            res_rev = basis_quote * (0.4 * renten + 0.6 * renten_vorjahr)
            res_rev = float(np.clip(res_rev * rng.normal(1.0, 0.18), 0.0, 15.0))

            # Vereinzelte Einnahmespitzen (Nachzahlungen, Einmalabgaben,
            # Preisverfall bei nachlaufenden Zahlungen). Erzeugen Ratios > 1,5
            # und pruefen damit den Flag-Pfad der Analyseskripte.
            if rng.random() < 0.03:
                res_rev = float(np.clip(res_rev * rng.uniform(4.0, 7.0), 0.0, 15.0))

            res_tax = float(np.clip(res_rev * rng.uniform(0.45, 0.9), 0.0, 15.0))

            # --- GRD-Fehlwerte: laut User Guide fehlen Werte meist, wenn die
            # Ressourceneinnahmen unter ca. 1 % des BIP liegen. ---
            if res_rev < 1.0 and rng.random() < 0.75:
                res_rev = np.nan
                res_tax = np.nan
            elif rng.random() < 0.06:  # sonstige Lueckenjahre
                res_rev = np.nan
                res_tax = np.nan

            # --- Entwicklungsindikatoren mit Trend ---
            trend = i / (len(jahre) - 1)
            hdi = hdi_niveau + 0.12 * trend + rng.normal(0, 0.008)
            hdi = float(np.clip(hdi, 0.30, 0.70))
            strom = float(np.clip(strom_niveau + 22 * trend + rng.normal(0, 2), 1, 100))
            gdppc = float(gdppc_niveau * (1 + 0.015) ** i * rng.normal(1.0, 0.05))

            if rng.random() < 0.04:  # vereinzelte Fehlwerte in den WDI-Reihen
                hdi = np.nan
            if rng.random() < 0.03:
                strom = np.nan

            zeilen.append(
                {
                    "iso3": iso3,
                    "country": name,
                    "year": int(jahr),
                    "sahel": ist_sahel,
                    "sahel_ext": ist_sahel or iso3 in SAHEL_EXT_ADD,
                    "oil_state": ist_oel,
                    "rents_pct_gdp": round(renten, 3),
                    "res_rev_pct_gdp": res_rev if pd.isna(res_rev) else round(res_rev, 3),
                    "res_tax_pct_gdp": res_tax if pd.isna(res_tax) else round(res_tax, 3),
                    "gdppc_const": round(gdppc, 2),
                    "elec_access_pct": strom if pd.isna(strom) else round(strom, 2),
                    "hdi": hdi if pd.isna(hdi) else round(hdi, 4),
                }
            )

    return pd.DataFrame(zeilen)


def abgeleitete_spalten(df: pd.DataFrame) -> pd.DataFrame:
    """Capture Ratio, Glaettung, Flag und Periode nach Forschungsdesign §3/§4."""

    # Nur Laenderjahre mit Renten >= 1 % BIP (kleiner Nenner verzerrt sonst).
    gueltig = df["rents_pct_gdp"] >= 1.0
    df["capture_ratio"] = np.where(
        gueltig, df["res_rev_pct_gdp"] / df["rents_pct_gdp"], np.nan
    )

    # Zentriertes 3-Jahres-Mittel je Land; min_periods=2 haelt die Randjahre
    # 2000 und 2021 besetzt (sonst fiele je Land ein Periodenjahr weg).
    df = df.sort_values(["iso3", "year"]).reset_index(drop=True)
    df["capture_ratio_3y"] = df.groupby("iso3", sort=False)["capture_ratio"].transform(
        lambda s: s.rolling(window=3, center=True, min_periods=2).mean()
    )

    # Werte > 1,5 flaggen, nicht loeschen (Timing, Preisschocks).
    df["flag_ratio_high"] = df["capture_ratio"] > 1.5

    df["period"] = df["year"].apply(periode)
    return df


SPALTEN = [
    "iso3", "country", "year", "sahel", "sahel_ext", "oil_state",
    "rents_pct_gdp", "res_rev_pct_gdp", "res_tax_pct_gdp", "gdppc_const",
    "elec_access_pct", "hdi", "capture_ratio", "capture_ratio_3y",
    "flag_ratio_high", "period",
]


def main() -> None:
    rng = np.random.default_rng(SEED)
    df = abgeleitete_spalten(baue_panel(rng))
    df = df[SPALTEN]

    OUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT, index=False)

    print("=" * 70)
    print("DUMMY-PANEL erzeugt — NICHT fuer Ergebnisse verwenden!")
    print("=" * 70)
    print(f"Datei:            {OUT}")
    print(f"Zeilen x Spalten: {df.shape[0]} x {df.shape[1]}")
    print(f"Laender:          {df['iso3'].nunique()}  (davon Sahel: "
          f"{df.loc[df['sahel'], 'iso3'].nunique()}, "
          f"Sahel erweitert: {df.loc[df['sahel_ext'], 'iso3'].nunique()}, "
          f"Oelstaaten: {df.loc[df['oil_state'], 'iso3'].nunique()})")
    print(f"Jahre:            {df['year'].min()}-{df['year'].max()}")
    print(f"Schema korrekt:   {list(df.columns) == SPALTEN}")
    print()
    print("Fehlwerte je Spalte:")
    for spalte, anzahl in df.isna().sum().items():
        if anzahl:
            print(f"  {spalte:<20} {anzahl:>5}  ({anzahl / len(df):.1%})")
    print()
    print(f"capture_ratio gueltig: {df['capture_ratio'].notna().sum()} Laenderjahre")
    print(f"flag_ratio_high:       {int(df['flag_ratio_high'].sum())} Laenderjahre > 1,5")


if __name__ == "__main__":
    main()
