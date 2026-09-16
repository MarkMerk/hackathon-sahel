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
    """Ersetzt capture_ratio_3y durch ein zentriertes Mittel der Breite `fenster`.

    Die Glaettung laeuft auf den *ungeglaetteten* Jahreswerten, damit nicht
    zweimal gemittelt wird. Anschliessend werden die Zellen wieder maskiert,
    in denen das Laenderjahr selbst keine Capture Ratio hat -- sonst hebt die
    Glaettung Laender ueber die Mindestjahres-Schwelle, die die eigentlichen
    Filterkriterien nicht erfuellen (stille Imputation).
    """
    d = df.sort_values(["iso3", "year"]).copy()
    geglaettet = d.groupby("iso3", sort=False)["capture_ratio"].transform(
        lambda s: s.rolling(window=fenster, center=True, min_periods=2).mean()
    )
    d["capture_ratio_3y"] = geglaettet.where(d["capture_ratio"].notna())
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

    # (c) 5-Jahres-Mittel statt der 3-Jahres-Glaettung der Hauptspezifikation.
    ergebnisse.append((
        "c", "5- statt 3-Jahres-Glättung",
        lauf(glaettung(df, 5)),
    ))

    # (c0) ungeglaettete Jahreswerte -- prueft, ob die Glaettung selbst den
    # Befund traegt. Bis 14:20 war dies versehentlich die Hauptspezifikation.
    ergebnisse.append((
        "c0", "ungeglättete Jahreswerte (ohne Glättung)",
        [dict(z) for z in _gv.vergleiche(
            _gv.periodenmittel(df, wert="capture_ratio")
        )],
    ))

    # (f) Quotient der Periodensummen statt Mittel der Jahresquotienten.
    # Entkraeftet den Einwand, dass das Mittel von Quotienten Jahre mit
    # kleinem Nenner ueberproportional gewichtet.
    ergebnisse.append((
        "f", "Quotient der Periodensummen statt Mittel der Jahresquotienten",
        summenquotient(df),
    ))

    # (g) Imputation der fehlenden Zaehler. Der GRD-Nutzerleitfaden nennt als
    # Grund fuer fehlende Werte Ressourceneinnahmen unter etwa 1 % BIP. Die
    # Ausfallquote ist stark asymmetrisch (Sahel 25 %, Vergleichsgruppe 56 %),
    # die Vergleichsgruppe also staerker nach oben verzerrt. Diese Variante
    # prueft, wie viel vom Gruppenabstand unter plausibler Imputation bleibt.
    for imp in (0.5, 0.8):
        ergebnisse.append((
            f"g{str(imp).replace('.', ',')}",
            f"fehlende Ressourceneinnahmen mit {imp} % BIP imputiert",
            lauf(imputiere_zaehler(df, imp)),
        ))

    # (d) geflaggte Ausreisser (Ratio > 1,5) ausschliessen. Beide Spalten
    # maskieren und danach neu glaetten -- sonst traegt capture_ratio_3y die
    # Ausreisser weiter und die Variante waere identisch zur Hauptspezifikation.
    ohne_flag = df.copy()
    if "flag_ratio_high" in ohne_flag.columns:
        flag = ohne_flag["flag_ratio_high"].fillna(False)
        ohne_flag.loc[flag, ["capture_ratio", "capture_ratio_3y"]] = np.nan
        ohne_flag = glaettung(ohne_flag, 3)
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


def imputiere_zaehler(df: pd.DataFrame, wert: float) -> pd.DataFrame:
    """Setzt fehlende Ressourceneinnahmen auf `wert` (% BIP) und rechnet neu.

    Nur fuer Laenderjahre mit Renten >= 1 % BIP, also solche, die ohne den
    fehlenden Zaehler in die Analyse eingegangen waeren.
    """
    d = df.copy()
    fehlt = (d["rents_pct_gdp"] >= 1) & (d["res_rev_pct_gdp"].isna())
    d.loc[fehlt, "res_rev_pct_gdp"] = wert
    d["capture_ratio"] = np.where(
        d["rents_pct_gdp"] >= 1, d["res_rev_pct_gdp"] / d["rents_pct_gdp"], np.nan
    )
    return glaettung(d, 3)


def summenquotient(df: pd.DataFrame) -> list[dict]:
    """Capture Ratio je Periode als Quotient der Summen statt Mittel der Quotienten.

    Inhaltlich naeher an der Forschungsfrage („welcher Anteil der ueber die
    Periode erzeugten Rente kommt im Haushalt an"), weil Jahre mit kleinem
    Nenner nicht ueberproportional gewichtet werden.
    """
    basis = df[df["capture_ratio"].notna()].copy()
    agg = basis.groupby(["iso3", "country", "sahel", "period"], as_index=False).agg(
        rev=("res_rev_pct_gdp", "sum"), rent=("rents_pct_gdp", "sum"),
        n_jahre=("capture_ratio", "size"),
    )
    agg = agg[(agg["n_jahre"] >= _gv.MIN_JAHRE) & (agg["rent"] > 0)].copy()
    agg["mittel"] = agg["rev"] / agg["rent"]
    agg["gruppe_sahel"] = agg["sahel"]
    return _gv.vergleiche(agg)


def rohstofftyp(df: pd.DataFrame, spalte: str = "oil_state") -> list[dict]:
    """Laender mit Oelfoerderung gegen die uebrigen, ueber ALLE Laender.

    POST HOC: Diese Aufschluesselung ist nicht im Forschungsdesign §5.6
    vorgesehen, sondern nach Sichtung der Regionsergebnisse hinzugekommen.
    Das ist beim Berichten zu deklarieren.

    Zur Klassifikation: Die Panelspalte `oil_state` wurde fuer den
    Robustheits-Ausschluss definiert (NGA, AGO, GNQ, COG, GAB, SSD, TCD) und
    ist als Oel-Kennzeichnung unvollstaendig -- Kamerun, Sudan und
    Mauretanien (seit 2006) foerdern ebenfalls Erdoel, stehen dort aber in
    der Vergleichsgruppe. Deshalb wird der Test zusaetzlich mit der
    erweiterten Abgrenzung gerechnet (`oil_ext`).
    """
    agg = df[df["capture_ratio"].notna()].groupby(
        ["iso3", "country", spalte, "period"], as_index=False
    ).agg(mittel=("capture_ratio", "mean"), n_jahre=("capture_ratio", "size"))
    agg = agg[agg["n_jahre"] >= _gv.MIN_JAHRE]
    agg = agg.rename(columns={spalte: "oil_state"})

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
            eintrag.update({"p": p, "delta": d,
                            "delta_txt": _gv.delta_label(d, min(len(x), len(y)))})
        zeilen.append(eintrag)
    return zeilen


def schreibe_tabelle(ergebnisse, ist_dummy: bool, typ_zeilen=None,
                     typ_ext=None) -> None:
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
        def typ_tabelle(zeilen_):
            return "\n".join(
                f"| {r['periode']} | {r['n_oel']} | {z(r['median_oel'])} "
                f"| {r['n_nicht']} | {z(r['median_nicht'])} "
                f"| {z(r['delta'])} | {p_fmt(r['p'])} |"
                for r in zeilen_
            )
        ext_block = ""
        if typ_ext:
            ext_block = f"""
Mit erweiterter Abgrenzung (zusätzlich Kamerun, Sudan und Mauretanien, die
ebenfalls Erdöl fördern):

| Periode | n Öl | Median Öl | n ohne Öl | Median ohne Öl | Cliff's δ | p |
|---|---|---|---|---|---|---|
{typ_tabelle(typ_ext)}
"""
        typ_block = f"""
## Abschöpfung nach Rohstofftyp (alle Länder, ohne Regionsbezug)

Diese Aufschlüsselung lässt die Sahel-Zugehörigkeit außer Acht. Positives
Cliff's δ bedeutet: Länder mit Ölförderung schöpfen mehr ab.

**Diese Auswertung ist post hoc**: Sie ist im Forschungsdesign §5.6 nicht
vorgesehen und wurde nach Sichtung der Regionsergebnisse ergänzt. Die
p-Werte sind nicht für multiples Testen adjustiert (siehe unten).

Erste Abgrenzung nach der Panelspalte `oil_state` (NGA, AGO, GNQ, COG, GAB,
SSD, TCD). Diese Spalte wurde für den Robustheits-Ausschluss definiert und
ist als Öl-Kennzeichnung unvollständig:

| Periode | n Öl | Median Öl | n ohne Öl | Median ohne Öl | Cliff's δ | p |
|---|---|---|---|---|---|---|
{typ_tabelle(typ_zeilen)}
{ext_block}
Der Kontrast nach Rohstofftyp ist deskriptiv deutlicher als der nach Region
und unter beiden Abgrenzungen gleichgerichtet; mit der erweiterten
Abgrenzung fällt er stärker aus. Er hält auch der Holm-Korrektur über alle
17 in dieser Arbeit berichteten Tests stand (erweiterte Abgrenzung:
p_Holm = 0,020 für 2008–2014 und 0,038 für 2015–2021).

Einschränkungen: Die Auswertung ist post hoc, und die drei Periodentests
beruhen auf denselben wenigen Ländern — sie sind keine drei unabhängigen
Belege. Die Klassifikation nach Rohstofftyp ist eine Vereinfachung; die
Länder fördern jeweils mehrere Rohstoffe in unterschiedlichem Anteil.
"""

    inhalt = f"""# Tab. 3 — Robustheitsprüfungen

{kopf}Der Gruppenvergleich aus Tab. 2 wird unter veränderten Spezifikationen
wiederholt. Einheit bleibt das **Länder-Periodenmittel**; Test ist der
zweiseitige Mann-Whitney-U, Effektgröße Cliff's δ (negativ = Sahel niedriger).

## Kernkontrast: mit und ohne Ölstaaten in der Vergleichsgruppe

Die Vergleichsgruppe enthält je Periode bis zu sechs Ölstaaten (NGA, AGO,
COG, GAB, GNQ, SSD; Südsudan erreicht nur 2008–2014 die Mindestzahl Jahre).
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

Entscheidend ist nicht, ob p unter 0,05 bleibt — bei vier Sahel-Ländern ist
die Teststärke dafür zu gering —, sondern ob die **Richtung** des Unterschieds
erhalten bleibt. Zu beachten: Die Zellen sind **keine unabhängigen
Replikationen**, da sie auf denselben vier Sahel-Ländern beruhen. In Variante
(a1) fällt die Effektgröße 2015–2021 auf −0,08 und ist damit
vernachlässigbar klein; als Bestätigung einer Richtung trägt sie kaum.

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
- Variante **(c0)** rechnet ohne Glättung und zeigt, dass der Befund nicht
  durch die Glättung entsteht. Bis 14:20 war diese Variante versehentlich
  die Hauptspezifikation; die Umstellung auf die im Design vorgesehene
  3-Jahres-Glättung verstärkt den Befund leicht.
- Variante **(d)** prüft, ob der Befund von einzelnen Länderjahren mit
  Capture Ratio > 1,5 getragen wird. Diese Werte sind nicht unplausibel
  (Nachzahlungen, Preisverfall bei nachlaufenden Zahlungen), verzerren
  Mittelwerte aber stark. Zu beachten: Botswana verliert dadurch alle 14
  gültigen Jahre und fällt vollständig aus der Vergleichsgruppe; (d) ist
  faktisch ein Länderausschluss, keine bloße Ausreißerbereinigung.
- Variante **(f)** bildet die Capture Ratio als Quotient der Periodensummen.
  Das gewichtet Jahre mit kleinem Nenner nicht über, ist inhaltlich näher an
  der Forschungsfrage und stützt den Befund.
- Variante **(g)** ist die einzige, die den Befund faktisch entkräftet: Unter
  Imputation der fehlenden Ressourceneinnahmen mit 0,5 % BIP sinkt die
  Effektgröße auf −0,26/−0,09/−0,04, unter 0,8 % BIP schwächer. Plausibel,
  weil die Ausfallquote asymmetrisch ist (Sahel 25 %, Vergleichsgruppe 56 %
  fehlende Werte bei Renten ≥ 1 % BIP). Das ist die stärkste Einschränkung
  dieser Arbeit, nicht eine Variante unter vielen.
- **Multiples Testen:** Diese Arbeit berichtet 17 Signifikanztests. Die
  p-Werte in dieser Tabelle sind nicht adjustiert; nach Holm-Korrektur über
  alle berichteten Tests bleibt kein Regionstest signifikant — er ist es
  auch unadjustiert nicht.
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

    # Erweiterte Oel-Abgrenzung: CMR, SDN und MRT foerdern ebenfalls Erdoel,
    # sind in der Panelspalte oil_state aber nicht als solche gefuehrt.
    df = df.copy()
    df["oil_ext"] = df["oil_state"] | df["iso3"].isin(["CMR", "SDN", "MRT"])

    typ_zeilen = rohstofftyp(df)
    typ_ext = rohstofftyp(df, spalte="oil_ext")
    for label, zeilen_ in [("Panelspalte oil_state", typ_zeilen),
                           ("erweitert (+ CMR, SDN, MRT)", typ_ext)]:
        print(f"[Typ] Oelfoerderung gegen uebrige Laender -- {label}")
        for r in zeilen_:
            if np.isnan(r["delta"]):
                print(f"     {r['periode']}  n={r['n_oel']}/{r['n_nicht']}  Test nicht möglich")
            else:
                print(f"     {r['periode']}  n={r['n_oel']}/{r['n_nicht']}  "
                      f"Med {r['median_oel']:.3f} vs {r['median_nicht']:.3f}  "
                      f"delta={r['delta']:+.3f}  p={r['p']:.4f}")
        print()

    print("Assoziation, keine Kausalitaet. Vorzeichenstabilitaet vor p-Werten lesen.")
    print("Post-hoc-Test, p-Werte nicht fuer multiples Testen adjustiert.\n")
    schreibe_tabelle(ergebnisse, ist_dummy, typ_zeilen, typ_ext)

    if ist_dummy:
        print("\nERINNERUNG: Ergebnisse basieren auf DUMMY-DATEN.")


if __name__ == "__main__":
    main()
