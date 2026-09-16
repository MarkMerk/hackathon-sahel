# Tab. 3 — Robustheitsprüfungen

Der Gruppenvergleich aus Tab. 2 wird unter veränderten Spezifikationen
wiederholt. Einheit bleibt das **Länder-Periodenmittel**; Test ist der
zweiseitige Mann-Whitney-U, Effektgröße Cliff's δ (negativ = Sahel niedriger).

## Ergebnisse je Spezifikation

| Spezifikation | Periode | n Sahel | Median Sahel | n Vergleich | Median Vergleich | p | Cliff's δ |
|---|---|---|---|---|---|---|---|
| **Haupt** — Hauptspezifikation (Sahel = 5 Länder, 3-Jahres-Basis, ≥ 3 Jahre) | 2000–2007 | 4 | 0,10 | 18 | 0,51 | 0,300 | -0,36 (mittel) |
|  | 2008–2014 | 4 | 0,21 | 22 | 0,25 | 0,252 | -0,39 (mittel) |
|  | 2015–2021 | 4 | 0,15 | 17 | 0,27 | 0,517 | -0,24 (klein) |
| **a** — ohne Ölstaaten (NGA, AGO, GNQ, COG, GAB, SSD, TCD) | 2000–2007 | 3 | 0,03 | 13 | 0,14 | 0,364 | -0,38 (mittel) |
|  | 2008–2014 | 3 | 0,05 | 16 | 0,15 | 0,359 | -0,38 (mittel) |
|  | 2015–2021 | 3 | 0,07 | 12 | 0,16 | 0,734 | -0,17 (klein) |
| **b** — Sahel erweitert (+ SDN, SEN) | 2000–2007 | 6 | 0,13 | 16 | 0,51 | 0,494 | -0,21 (klein) |
|  | 2008–2014 | 6 | 0,22 | 20 | 0,25 | 0,268 | -0,32 (klein) |
|  | 2015–2021 | 6 | 0,18 | 15 | 0,37 | 0,424 | -0,24 (klein) |
| **c** — 5-Jahres-Mittel statt 3-Jahres-Glättung | 2000–2007 | 4 | 0,09 | 19 | 0,50 | 0,324 | -0,34 (mittel) |
|  | 2008–2014 | 5 | 0,22 | 22 | 0,35 | 0,232 | -0,36 (mittel) |
|  | 2015–2021 | 5 | 0,19 | 17 | 0,26 | 0,493 | -0,22 (klein) |
| **d** — ohne geflaggte Länderjahre (Capture Ratio > 1,5) | 2000–2007 | 4 | 0,10 | 16 | 0,37 | 0,437 | -0,28 (klein) |
|  | 2008–2014 | 4 | 0,21 | 20 | 0,22 | 0,347 | -0,32 (klein) |
|  | 2015–2021 | 4 | 0,15 | 17 | 0,27 | 0,517 | -0,24 (klein) |
| **e** — mindestens 5 statt 3 gültige Jahre je Periode | 2000–2007 | 3 | 0,03 | 14 | 0,37 | 0,432 | -0,33 (mittel) |
|  | 2008–2014 | 3 | 0,05 | 17 | 0,47 | 0,118 | -0,61 (groß) |
|  | 2015–2021 | 4 | 0,15 | 17 | 0,27 | 0,517 | -0,24 (klein) |

## Vorzeichenstabilität der Effektgröße

Entscheidend ist nicht, ob p unter 0,05 bleibt — bei n = 5 Sahel-Ländern ist
die Teststärke dafür zu gering —, sondern ob die **Richtung** des Unterschieds
erhalten bleibt.

| Variante | Beschreibung | 2000–2007 | 2008–2014 | 2015–2021 |
|---|---|---|---|---|
| a | ohne Ölstaaten (NGA, AGO, GNQ, COG, GAB, SSD, TCD) | ja | ja | ja |
| b | Sahel erweitert (+ SDN, SEN) | ja | ja | ja |
| c | 5-Jahres-Mittel statt 3-Jahres-Glättung | ja | ja | ja |
| d | ohne geflaggte Länderjahre (Capture Ratio > 1,5) | ja | ja | ja |
| e | mindestens 5 statt 3 gültige Jahre je Periode | ja | ja | ja |

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

Quelle: World Bank WDI, UNU-WIDER GRD 2025; eigene Berechnung.
Erzeugt von `src/06_robustheit.py`.
