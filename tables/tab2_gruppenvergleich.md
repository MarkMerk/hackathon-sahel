# Tab. 2 — Capture Ratio: Sahel vs. übriges Subsahara-Afrika

> **ACHTUNG: auf DUMMY-DATEN gerechnet (`panel_dummy.csv`).**
> Alle Werte sind erfunden und dienen nur dem Test der Pipeline.
> Nach Vorliegen von `panel.csv` neu erzeugen.

Einheit der Analyse: **Länder-Periodenmittel** der Capture Ratio
(ein Wert je Land und Periode; Länder mit weniger als 3 gültigen
Jahren in einer Periode bleiben für diese Periode unberücksichtigt).
Test: Mann-Whitney-U (zweiseitig). Effektgröße: Cliff's Delta
(negativ = Sahel niedriger), Einordnung nach Romano et al. (2006).

| Periode | n Sahel | Median Sahel | IQR Sahel | n übr. SSA | Median übr. SSA | IQR übr. SSA | U | p | Cliff's δ |
|---|---|---|---|---|---|---|---|---|---|
| 2000–2007 | 5 | 0,45 | 0,38–0,46 | 37 | 0,43 | 0,37–0,48 | 95,0 | 0,940 | 0,03 (vernachlässigbar) |
| 2008–2014 | 5 | 0,37 | 0,34–0,47 | 38 | 0,46 | 0,38–0,50 | 65,0 | 0,273 | -0,32 (klein) |
| 2015–2021 | 5 | 0,48 | 0,47–0,61 | 37 | 0,41 | 0,38–0,48 | 124,0 | 0,237 | 0,34 (mittel) |

**Lesehilfe:** Die Capture Ratio ist einheitenlos und gibt den Anteil der
Rohstoffrenten an, der als Ressourceneinnahme im Staatshaushalt ankommt
(0,30 = 30 %). Cliff's δ = −0,50 bedeutet: In 75 % der Länderpaare liegt das
Sahel-Land unter dem Vergleichsland.

**Hinweise zur Interpretation:**
- Der Test prüft, ob ein zufällig gezogenes Sahel-Land über einem zufällig
  gezogenen Vergleichsland liegt, nicht Kausalität. Alle Befunde sind
  **Assoziationen**.
- Mit n = 5–5 Sahel-Ländern ist die Teststärke gering.
  Ein nicht signifikantes Ergebnis heißt „für eine Aussage reichen die Daten
  nicht", nicht „kein Unterschied". Deshalb steht die Effektgröße vor dem p-Wert.
- Länderjahre mit Rohstoffrenten < 1 % BIP sind bereits in `panel.csv`
  ausgeschlossen (kleiner Nenner).
- 5 Länderjahre mit Capture Ratio > 1,5 sind enthalten und geflaggt
  (`flag_ratio_high`); sie entstehen durch Timing zwischen Rentenanfall und
  Zahlungseingang sowie durch Preisschocks und wurden nicht entfernt.

Quelle: World Bank WDI, ICTD/UNU-WIDER GRD 2023; eigene Berechnung.
Erzeugt von `src/04_gruppenvergleich.py`.
