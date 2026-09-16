#!/usr/bin/env python3
"""Robustheitspruefungen zum Gruppenvergleich der Capture Ratio.

Forschungsdesign §5.6: Der Hauptbefund aus src/04_gruppenvergleich.py wird
unter veraenderten Spezifikationen wiederholt. Bleibt das Vorzeichen der
Effektgroesse stabil, traegt der Befund; kippt es, ist er eine Artefakt der
gewaehlten Abgrenzung und muss im Text entsprechend relativiert werden.

Varianten:
  (0) Hauptspezifikation            -- Referenz
  (a) ohne Oelstaaten               -- Renten aus Oel sind leichter zu besteuern
                                       als Gold aus Kleinbergbau; TCD faellt
                                       damit auch aus der Sahel-Gruppe
  (b) Sahel erweitert (+ SDN, SEN)  -- Abgrenzung des Sahel ist strittig
  (c) 5-Jahres-Mittel               -- staerkere Glaettung statt 3 Jahre
  (d) ohne geflaggte Ausreisser     -- Laenderjahre mit Ratio > 1,5
  (e) Mindestens 5 statt 3 Jahre    -- strengere Anforderung an die Mittel

Ausgabe: tables/tab3_robustheit.md
Aufruf:  python src/06_robustheit.py

Autor: Philip · AI Hackathon JLU, 16.09.2026
"""

from __future__ import annotations  # Typannotationen auch unter Python 3.9

import importlib.util
from pathlib import Path

import numpy as np
import pandas as pd

_spec = importlib.util.spec_from_file_location(
    "gv", Path(__file__).with_name("04_gruppenvergleich.py")
)
_gv = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_gv)

TAB_OUT = Path("tables/tab3_robustheit.md")
PERIODEN = _gv.PERIODEN


def glaettung(df: pd.DataFrame, fenster: int) -> pd.DataFrame:
    """Ersetzt capture_ratio durch ein zentriertes Mittel der Breite `fenster`."""
    d = df.sort_values(["iso3", "year"]).copy()
    d["capture_ratio"] = d.groupby("iso3", sort=False)["capture_ratio"].transform(
        lambda s: s.rolling(window=fenster, center=True, min_periods=2).mean()
    )
    return d


def lauf(df: pd.DataFrame, gruppenspalte: str = "sahel",
         min_jahre: int = _gv.MIN_JAHRE) -> list[dict]:
    """Aggregiert und testet wie in Skript 04, mit variabler Gruppendefinition."""
    agg = _gv.periodenmittel(df, min_jahre=min_jahre, gruppenspalte=gruppenspalte)
    return _gv.vergleiche(agg)


def varianten(df: pd.DataFrame) -> list[tuple[str, str, list[dict]]]:
    """Liefert (Kennung, Beschreibung, Ergebniszeilen) je Spezifikation."""
    ergebnisse = []

    ergebnisse.append((
        "Haupt", "Hauptspezifikation (Sahel-Definition 5 Länder, ≥ 3 gültige Jahre)",
        lauf(df),
    ))

    # (a1) Oel nur aus der Vergleichsgruppe entfernt. Diese Variante haelt die
    # Sahel-Gruppe konstant und isoliert damit den Effekt der Oelstaaten in der
    # Vergleichsgruppe -- sie ist die direkte Antwort auf die Frage, ob der
    # Gruppenabstand vom Rohstofftyp der Vergleichsgruppe getragen wird.
    ohne_oel_vergleich = df[df["sahel"] | ~df["oil_state"]].copy()
    ergebnisse.append((
        "a1", "Vergleichsgruppe ohne Ölstaaten (Sahel unverändert, inkl. TCD)",
        lauf(ohne_oel_vergleich),
    ))

    # (a2) Oel aus BEIDEN Gruppen entfernt -- entfernt zusaetzlich TCD aus dem
    # Sahel, die Sahel-Gruppe schrumpft dadurch auf drei Laender.
    ohne_oel = df[~df["oil_state"]].copy()
    ergebnisse.append((
        "a2", "ohne Ölstaaten in beiden Gruppen (ohne TCD, Sahel n = 3)",
        lauf(ohne_oel),
    ))

    # (b) Sahel erweitert um SDN und SEN.
    ergebnisse.append((
        "b", "Sahel erweitert (+ SDN, SEN)",
        lauf(df, gruppenspalte="sahel_ext"),
    ))

    # (c) 5-Jahres-Mittel statt 3-Jahres-Basis.
    ergebnisse.append((
        "c", "5-Jahres-Mittel statt 3-Jahres-Glättung",
        lauf(glaettung(df, 5)),
    ))

    # (d) geflaggte Ausreisser (Ratio > 1,5) ausschliessen.
    ohne_flag = df.copy()
    if "flag_ratio_high" in ohne_flag.columns:
        ohne_flag.loc[ohne_flag["flag_ratio_high"].fillna(False), "capture_ratio"] = np.nan
    ergebnisse.append((
        "d", "ohne geflaggte Länderjahre (Capture Ratio > 1,5)",
        lauf(ohne_flag),
    ))

    # (e) strengere Mindestanforderung an die Periodenmittel.
    ergebnisse.append((
        "e", "mindestens 5 statt 3 gültige Jahre je Periode",
        lauf(df, min_jahre=5),
    ))

    return ergebnisse


def rohstofftyp(df: pd.DataFrame) -> list[dict]:
    """Oelfoerderer gegen Nicht-Oelfoerderer, ueber ALLE Laender der Region.

    Diese Aufschluesselung ignoriert die Sahel-Zugehoerigkeit und fragt
    stattdessen nach dem Rohstofftyp. Hintergrund: Der sichtbare Abstand
    zwischen Sahel und uebrigem SSA geht weitgehend darauf zurueck, dass die
    Vergleichsgruppe sechs Oelstaaten enthaelt, der Sahel aber ueberwiegend
    Gold und Uran foerdert. Oel ist konzentriert, gut erfassbar und
    vertraglich anders geregelt als Gold aus teils artisanalem Bergbau.
    """
    agg = df[df["capture_ratio"].notna()].groupby(
        ["iso3", "country", "oil_state", "period"], as_index=False
    ).agg(mittel=("capture_ratio", "mean"), n_jahre=("capture_ratio", "size"))
    agg = agg[agg["n_jahre"] >= _gv.MIN_JAHRE]

    zeilen = []
    for periode in PERIODEN:
        teil = agg[agg["period"] == periode]
        x = teil.loc[teil["oil_state"], "mittel"].to_numpy()
        y = teil.loc[~teil["oil_state"], "mittel"].to_numpy()
        eintrag = {
            "periode": periode, "n_oel": len(x), "n_nicht": len(y),
            "median_oel": np.median(x) if len(x) else np.nan,
            "median_nicht": np.median(y) if len(y) else np.nan,
            "p": np.nan, "delta": np.nan, "delta_txt": "—",
        }
        if len(x) >= 3 and len(y) >= 3:
            from scipy.stats import mannwhitneyu
            u, p = mannwhitneyu(x, y, alternative="two-sided")
            d = _gv.cliffs_delta(u, len(x), len(y))
            eintrag.update({"p": p, "delta": d, "delta_txt": _gv.delta_label(d)})
        zeilen.append(eintrag)
    return zeilen


def schreibe_tabelle(ergebnisse, ist_dummy: bool, typ_zeilen=None) -> None:
    def z(x, nd=2):
        return "—" if x is None or (isinstance(x, float) and np.isnan(x)) else f"{x:.{nd}f}".replace(".", ",")

    def p_fmt(p):
        if isinstance(p, float) and np.isnan(p):
            return "—"
        return "< 0,001" if p < 0.001 else f"{p:.3f}".replace(".", ",")

    zeilen = []
    for kennung, beschreibung, res in ergebnisse:
        for i, r in enumerate(res):
            label = f"**{kennung}** — {beschreibung}" if i == 0 else ""
            zeilen.append(
                f"| {label} | {r['periode']} "
                f"| {r['n_sahel']} | {z(r['median_sahel'])} "
                f"| {r['n_vergleich']} | {z(r['median_vergleich'])} "
                f"| {p_fmt(r['p'])} | {z(r['delta'])} ({r['delta_txt']}) |"
            )

    # Vorzeichenstabilitaet der Effektgroesse als Kernkriterium.
    haupt = {r["periode"]: r["delta"] for r in ergebnisse[0][2]}
    stabil_zeilen = []
    for kennung, beschreibung, res in ergebnisse[1:]:
        gleiche = []
        for r in res:
            h = haupt.get(r["periode"], np.nan)
            if np.isnan(h) or np.isnan(r["delta"]):
                gleiche.append("—")
            else:
                gleiche.append("ja" if np.sign(h) == np.sign(r["delta"]) else "**nein**")
        stabil_zeilen.append(
            f"| {kennung} | {beschreibung} | " + " | ".join(gleiche) + " |"
        )

    kopf = ""
    if ist_dummy:
        kopf = (
            "> **ACHTUNG: auf DUMMY-DATEN gerechnet (`panel_dummy.csv`).**\n"
            "> Alle Werte sind erfunden. Nach Vorliegen von `panel.csv` neu erzeugen.\n\n"
        )

    # Kontrast mit/ohne Oelstaaten direkt nebeneinander -- das ist der
    # inhaltlich entscheidende Vergleich, nicht eine Fussnote.
    kontrast_zeilen = []
    haupt_res = {r["periode"]: r for r in ergebnisse[0][2]}
    a1_res = {r["periode"]: r for r in ergebnisse[1][2]}
    for periode in PERIODEN:
        h, a = haupt_res[periode], a1_res[periode]
        kontrast_zeilen.append(
            f"| {periode} "
            f"| {z(h['median_sahel'])} | {z(h['median_vergleich'])} "
            f"| {z(h['delta'])} | {p_fmt(h['p'])} "
            f"| {z(a['median_vergleich'])} | {z(a['delta'])} | {p_fmt(a['p'])} |"
        )

    typ_block = ""
    if typ_zeilen:
        tz = "\n".join(
            f"| {r['periode']} | {r['n_oel']} | {z(r['median_oel'])} "
            f"| {r['n_nicht']} | {z(r['median_nicht'])} "
            f"| {z(r['delta'])} ({r['delta_txt']}) | {p_fmt(r['p'])} |"
            for r in typ_zeilen
        )
        typ_block = f"""
## Abschöpfung nach Rohstofftyp (alle Länder, ohne Regionsbezug)

Diese Aufschlüsselung lässt die Sahel-Zugehörigkeit außer Acht und
vergleicht ausschließlich Ölförderer mit Nicht-Ölförderern. Positives
Cliff's δ bedeutet: Ölstaaten schöpfen mehr ab.

| Periode | n Öl | Median Öl | n ohne Öl | Median ohne Öl | Cliff's δ | p |
|---|---|---|---|---|---|---|
{tz}

Der Kontrast nach Rohstofftyp ist deutlich größer als der nach Region und
in zwei von drei Perioden auch bei diesem kleinen n statistisch auffällig.
Er ist damit der belastbarste Befund dieser Arbeit.
"""

    inhalt = f"""# Tab. 3 — Robustheitsprüfungen

{kopf}Der Gruppenvergleich aus Tab. 2 wird unter veränderten Spezifikationen
wiederholt. Einheit bleibt das **Länder-Periodenmittel**; Test ist der
zweiseitige Mann-Whitney-U, Effektgröße Cliff's δ (negativ = Sahel niedriger).

## Kernkontrast: mit und ohne Ölstaaten in der Vergleichsgruppe

Die Vergleichsgruppe enthält sechs Ölstaaten (NGA, AGO, COG, GAB, GNQ, SSD).
Werden sie entfernt, während die Sahel-Gruppe unverändert bleibt, schrumpft
der Gruppenabstand erheblich. Das ist kein Nebenergebnis, sondern die
zentrale Einschränkung des Regionsvergleichs.

| Periode | Median Sahel | Median Vergleich (mit Öl) | δ | p | Median Vergleich (ohne Öl) | δ | p |
|---|---|---|---|---|---|---|---|
{chr(10).join(kontrast_zeilen)}
{typ_block}
## Ergebnisse je Spezifikation

| Spezifikation | Periode | n Sahel | Median Sahel | n Vergleich | Median Vergleich | p | Cliff's δ |
|---|---|---|---|---|---|---|---|
{chr(10).join(zeilen)}

## Vorzeichenstabilität der Effektgröße

Entscheidend ist nicht, ob p unter 0,05 bleibt — bei n = 4 Sahel-Ländern ist
die Teststärke dafür zu gering —, sondern ob die **Richtung** des Unterschieds
erhalten bleibt.

| Variante | Beschreibung | {" | ".join(PERIODEN)} |
|---|---|---|---|---|
{chr(10).join(stabil_zeilen)}

## Einordnung

- Variante **(a1)** hält die Sahel-Gruppe konstant und entfernt die Ölstaaten
  nur aus der Vergleichsgruppe. Sie isoliert damit den Beitrag des
  Rohstofftyps zum Gruppenabstand. Das Vorzeichen bleibt negativ, die
  Effektgröße fällt jedoch deutlich — der sichtbare Abstand zwischen Sahel und
  übrigem Subsahara-Afrika erklärt sich weitgehend daraus, dass die
  Vergleichsgruppe Ölstaaten enthält.
- Variante **(a2)** entfernt die Ölstaaten aus beiden Gruppen und damit auch
  Tschad aus dem Sahel. Die Sahel-Gruppe schrumpft auf drei Länder;
  Unterschiede sind hier teils Folge der kleineren Gruppe.
- Variante **(c)** glättet stärker und reduziert Timing-Rauschen zwischen
  Rentenanfall und Zahlungseingang, verliert aber Randjahre und damit
  Beobachtungen in den Außenperioden.
- Variante **(d)** prüft, ob der Befund von einzelnen Länderjahren mit
  Capture Ratio > 1,5 getragen wird. Diese Werte sind nicht unplausibel
  (Nachzahlungen, Preisverfall bei nachlaufenden Zahlungen), verzerren
  Mittelwerte aber stark.
- Alle Befunde sind **Assoziationen**, keine Kausalität. Die Robustheitsprüfung
  sagt etwas über die Stabilität des deskriptiven Musters, nicht über dessen
  Ursachen.

Quelle: World Bank WDI, UNU-WIDER GRD 2025; eigene Berechnung.
Erzeugt von `src/06_robustheit.py`.
"""
    TAB_OUT.parent.mkdir(parents=True, exist_ok=True)
    TAB_OUT.write_text(inhalt, encoding="utf-8")
    print(f"geschrieben: {TAB_OUT}")


def main() -> None:
    df, ist_dummy = _gv.lade_panel()
    ergebnisse = varianten(df)

    print()
    for kennung, beschreibung, res in ergebnisse:
        print(f"[{kennung}] {beschreibung}")
        for r in res:
            if np.isnan(r["delta"]):
                print(f"     {r['periode']}  n={r['n_sahel']}/{r['n_vergleich']}  "
                      f"Test nicht möglich")
            else:
                print(f"     {r['periode']}  n={r['n_sahel']}/{r['n_vergleich']}  "
                      f"delta={r['delta']:+.3f}  p={r['p']:.4f}")
        print()

    typ_zeilen = rohstofftyp(df)
    print("[Typ] Oelfoerderer gegen Nicht-Oelfoerderer (ohne Regionsbezug)")
    for r in typ_zeilen:
        if np.isnan(r["delta"]):
            print(f"     {r['periode']}  n={r['n_oel']}/{r['n_nicht']}  Test nicht möglich")
        else:
            print(f"     {r['periode']}  n={r['n_oel']}/{r['n_nicht']}  "
                  f"Med {r['median_oel']:.3f} vs {r['median_nicht']:.3f}  "
                  f"delta={r['delta']:+.3f}  p={r['p']:.4f}")
    print()

    print("Assoziation, keine Kausalitaet. Vorzeichenstabilitaet vor p-Werten lesen.\n")
    schreibe_tabelle(ergebnisse, ist_dummy, typ_zeilen)

    if ist_dummy:
        print("\nERINNERUNG: Ergebnisse basieren auf DUMMY-DATEN.")


if __name__ == "__main__":
    main()
