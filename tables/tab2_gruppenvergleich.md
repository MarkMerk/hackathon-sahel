# Tab. 2 — Capture Ratio: Sahel vs. übriges Subsahara-Afrika

Einheit der Analyse: **Länder-Periodenmittel** der zentriert
3-jährig geglätteten Capture Ratio (Forschungsdesign §3; ein Wert je Land
und Periode, Länder mit weniger als 3 gültigen Jahren in einer
Periode bleiben für diese Periode unberücksichtigt).
Test: Mann-Whitney-U (zweiseitig). Effektgröße: Cliff's Delta
(negativ = Sahel niedriger). Eine Einordnung nach Romano et al. (2006)
entfällt, weil sie bei vier Ländern je Periode eine Genauigkeit
suggerieren würde, die die Datenlage nicht hergibt.

| Periode | n Sahel | Median Sahel | IQR Sahel | n übr. SSA | Median übr. SSA | IQR übr. SSA | U | p | Cliff's δ |
|---|---|---|---|---|---|---|---|---|---|
| 2000–2007 | 4 | 0,10 | 0,03–0,28 | 18 | 0,51 | 0,10–0,71 | 21,0 | 0,227 | -0,42 (n zu klein für Einordnung) |
| 2008–2014 | 4 | 0,21 | 0,04–0,38 | 22 | 0,35 | 0,09–0,76 | 25,0 | 0,197 | -0,43 (n zu klein für Einordnung) |
| 2015–2021 | 4 | 0,16 | 0,06–0,32 | 17 | 0,26 | 0,11–0,45 | 25,0 | 0,462 | -0,26 (n zu klein für Einordnung) |

**Lesehilfe:** Die Capture Ratio ist einheitenlos und gibt den Anteil der
Rohstoffrenten an, der als Ressourceneinnahme im Staatshaushalt ankommt
(0,30 = 30 %). Cliff's δ = −0,50 bedeutet: In 75 % der Länderpaare liegt das
Sahel-Land unter dem Vergleichsland.

**Hinweise zur Interpretation:**
- Der Test prüft, ob ein zufällig gezogenes Sahel-Land über einem zufällig
  gezogenen Vergleichsland liegt, nicht Kausalität. Alle Befunde sind
  **Assoziationen**.
- Mit n = 4 Sahel-Ländern je Periode ist die Teststärke gering.
  Ein nicht signifikantes Ergebnis heißt „für eine Aussage reichen die Daten
  nicht", nicht „kein Unterschied". Deshalb steht die Effektgröße vor dem p-Wert.
- Länderjahre mit Rohstoffrenten < 1 % BIP erhalten in `panel.csv` keine
  Capture Ratio (kleiner Nenner) und gehen daher nicht ein.
- Die Vergleichsgruppe enthält Sudan und Senegal; Variante (b) in Tab. 3
  ordnet sie dem erweiterten Sahel zu.
- Der Interquartilsabstand beruht bei n = 4 auf Interpolation zwischen
  wenigen Werten und ist nur illustrativ.
- Nicht in allen Perioden vertretene Sahel-Länder: MLI (fehlt in 2000–2007, 2008–2014, 2015–2021).
- 19 Länderjahre mit Capture Ratio > 1,5 sind enthalten und geflaggt
  (`flag_ratio_high`); sie entstehen durch Timing zwischen Rentenanfall und
  Zahlungseingang sowie durch Preisschocks und wurden nicht entfernt.

Quelle: World Bank WDI, UNU-WIDER GRD 2025; eigene Berechnung.
Erzeugt von `src/04_gruppenvergleich.py`.
