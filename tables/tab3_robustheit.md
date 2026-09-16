# Tab. 3 — Robustheitsprüfungen

> **ACHTUNG: auf DUMMY-DATEN gerechnet (`panel_dummy.csv`).**
> Alle Werte sind erfunden. Nach Vorliegen von `panel.csv` neu erzeugen.

Der Gruppenvergleich aus Tab. 2 wird unter veränderten Spezifikationen
wiederholt. Einheit bleibt das **Länder-Periodenmittel**; Test ist der
zweiseitige Mann-Whitney-U, Effektgröße Cliff's δ (negativ = Sahel niedriger).

## Ergebnisse je Spezifikation

| Spezifikation | Periode | n Sahel | Median Sahel | n Vergleich | Median Vergleich | p | Cliff's δ |
|---|---|---|---|---|---|---|---|
| **Haupt** — Hauptspezifikation (Sahel = 5 Länder, 3-Jahres-Basis, ≥ 3 Jahre) | 2000–2007 | 5 | 0,45 | 37 | 0,43 | 0,940 | 0,03 (vernachlässigbar) |
|  | 2008–2014 | 5 | 0,37 | 38 | 0,46 | 0,273 | -0,32 (klein) |
|  | 2015–2021 | 5 | 0,48 | 37 | 0,41 | 0,237 | 0,34 (mittel) |
| **a** — ohne Ölstaaten (NGA, AGO, GNQ, COG, GAB, SSD, TCD) | 2000–2007 | 4 | 0,41 | 31 | 0,43 | 0,745 | -0,11 (vernachlässigbar) |
|  | 2008–2014 | 4 | 0,36 | 32 | 0,46 | 0,208 | -0,41 (mittel) |
|  | 2015–2021 | 4 | 0,54 | 31 | 0,41 | 0,352 | 0,31 (klein) |
| **b** — Sahel erweitert (+ SDN, SEN) | 2000–2007 | 7 | 0,43 | 35 | 0,43 | 0,921 | -0,03 (vernachlässigbar) |
|  | 2008–2014 | 7 | 0,38 | 36 | 0,46 | 0,236 | -0,29 (klein) |
|  | 2015–2021 | 7 | 0,47 | 35 | 0,41 | 0,692 | 0,10 (vernachlässigbar) |
| **c** — 5-Jahres-Mittel statt 3-Jahres-Glättung | 2000–2007 | 5 | 0,42 | 37 | 0,43 | 0,851 | -0,06 (vernachlässigbar) |
|  | 2008–2014 | 5 | 0,37 | 38 | 0,46 | 0,405 | -0,24 (klein) |
|  | 2015–2021 | 5 | 0,50 | 37 | 0,42 | 0,286 | 0,31 (klein) |
| **d** — ohne geflaggte Länderjahre (Capture Ratio > 1,5) | 2000–2007 | 5 | 0,45 | 37 | 0,43 | 0,910 | 0,04 (vernachlässigbar) |
|  | 2008–2014 | 5 | 0,37 | 38 | 0,45 | 0,308 | -0,29 (klein) |
|  | 2015–2021 | 5 | 0,47 | 37 | 0,41 | 0,426 | 0,23 (klein) |
| **e** — mindestens 5 statt 3 gültige Jahre je Periode | 2000–2007 | 5 | 0,45 | 36 | 0,43 | 0,985 | 0,01 (vernachlässigbar) |
|  | 2008–2014 | 5 | 0,37 | 37 | 0,47 | 0,269 | -0,32 (klein) |
|  | 2015–2021 | 4 | 0,55 | 34 | 0,41 | 0,035 | 0,65 (groß) |

## Vorzeichenstabilität der Effektgröße

Entscheidend ist nicht, ob p unter 0,05 bleibt — bei n = 5 Sahel-Ländern ist
die Teststärke dafür zu gering —, sondern ob die **Richtung** des Unterschieds
erhalten bleibt.

| Variante | Beschreibung | 2000–2007 | 2008–2014 | 2015–2021 |
|---|---|---|---|---|
| a | ohne Ölstaaten (NGA, AGO, GNQ, COG, GAB, SSD, TCD) | **nein** | ja | ja |
| b | Sahel erweitert (+ SDN, SEN) | **nein** | ja | ja |
| c | 5-Jahres-Mittel statt 3-Jahres-Glättung | **nein** | ja | ja |
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

Quelle: World Bank WDI, ICTD/UNU-WIDER GRD 2023; eigene Berechnung.
Erzeugt von `src/06_robustheit.py`.
