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
        "Haupt", "Hauptspezifikation (Sahel = 5 Länder, 3-Jahres-Basis, ≥ 3 Jahre)",
        lauf(df),
    ))

    # (a) ohne Oelstaaten -- entfernt NGA, AGO, GNQ, COG, GAB, SSD und TCD.
    ohne_oel = df[~df["oil_state"]].copy()
    ergebnisse.append((
        "a", "ohne Ölstaaten (NGA, AGO, GNQ, COG, GAB, SSD, TCD)",
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


def schreibe_tabelle(ergebnisse, ist_dummy: bool) -> None:
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

    inhalt = f"""# Tab. 3 — Robustheitsprüfungen

{kopf}Der Gruppenvergleich aus Tab. 2 wird unter veränderten Spezifikationen
wiederholt. Einheit bleibt das **Länder-Periodenmittel**; Test ist der
zweiseitige Mann-Whitney-U, Effektgröße Cliff's δ (negativ = Sahel niedriger).

## Ergebnisse je Spezifikation

| Spezifikation | Periode | n Sahel | Median Sahel | n Vergleich | Median Vergleich | p | Cliff's δ |
|---|---|---|---|---|---|---|---|
{chr(10).join(zeilen)}

## Vorzeichenstabilität der Effektgröße

Entscheidend ist nicht, ob p unter 0,05 bleibt — bei n = 5 Sahel-Ländern ist
die Teststärke dafür zu gering —, sondern ob die **Richtung** des Unterschieds
erhalten bleibt.

| Variante | Beschreibung | {" | ".join(PERIODEN)} |
|---|---|---|---|---|
{chr(10).join(stabil_zeilen)}

## Einordnung

- Variante **(a)** entfernt mit den Ölstaaten auch Tschad aus der Sahel-Gruppe.
  Die Sahel-Gruppe schrumpft damit auf vier Länder; Unterschiede zur
  Hauptspezifikation sind daher teils Folge der kleineren Gruppe, nicht nur
  des Ölstaaten-Ausschlusses.
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

Quelle: World Bank WDI, ICTD/UNU-WIDER GRD 2023; eigene Berechnung.
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

    print("Assoziation, keine Kausalitaet. Vorzeichenstabilitaet vor p-Werten lesen.\n")
    schreibe_tabelle(ergebnisse, ist_dummy)

    if ist_dummy:
        print("\nERINNERUNG: Ergebnisse basieren auf DUMMY-DATEN.")


if __name__ == "__main__":
    main()
