# Tab. 2b — Capture Ratio und menschliche Entwicklung

> **ACHTUNG: auf DUMMY-DATEN gerechnet (`panel_dummy.csv`).**
> Alle Werte sind erfunden. Nach Vorliegen von `panel.csv` neu erzeugen.

Spearman-Rangkorrelation auf **Länder-Periodenmitteln** (ein Wert je Land
und Periode, mindestens 3 gültige Jahre). Rangbasiert, weil beide
Größen schief verteilt sind und der Zusammenhang nicht linear sein muss.

## Capture Ratio ↔ HDI

| Ebene | n | Spearman ρ | p |
|---|---|---|---|
| alle Perioden | 127 | -0,001 | 0,994 |
| 2000–2007 | 42 | 0,004 | 0,982 |
| 2008–2014 | 43 | 0,022 | 0,888 |
| 2015–2021 | 42 | -0,042 | 0,793 |

## Capture Ratio ↔ Stromzugang (% der Bevölkerung)

| Ebene | n | Spearman ρ | p |
|---|---|---|---|
| alle Perioden | 127 | 0,013 | 0,885 |
| 2000–2007 | 42 | 0,151 | 0,339 |
| 2008–2014 | 43 | -0,037 | 0,812 |
| 2015–2021 | 42 | -0,073 | 0,648 |

## Two-way-Fixed-Effects-OLS (Ergänzung)

Modell: `hdi ~ capture_ratio + log(BIP pro Kopf) + Land-FE + Jahr-FE`,
Standardfehler geclustert nach Land.

Koeffizient der Capture Ratio: **0,0018** (SE 0,0013, p 0,155, 95-%-KI [-0,0007; 0,0044]), n = 823 Länderjahre aus 45 Ländern, R² = 0,993 (inkl. Fixed Effects).

Lesart: Eine um 0,1 höhere Capture Ratio geht mit einem um 0,0002 HDI-Punkten abweichenden Wert einher — **innerhalb** eines Landes und nach Kontrolle des Jahres und des BIP pro Kopf. Das ist eine Assoziation; die Wirkungsrichtung ist nicht identifiziert.

## Einordnung

- **Assoziation, keine Kausalität.** Eine höhere Abschöpfungsquote und ein
  höherer HDI können beide Folge einer dritten Größe sein — etwa staatlicher
  Verwaltungskapazität oder der Qualität fiskalischer Institutionen. Auch die
  umgekehrte Richtung ist denkbar: entwickeltere Staaten können Renten besser
  besteuern.
- Die Capture Ratio sagt nichts darüber, **wofür** die Einnahmen verwendet
  werden. Ein hoher Wert bedeutet nicht, dass die Mittel entwicklungswirksam
  eingesetzt werden; die Verteilung innerhalb des Staates bleibt außerhalb
  der Reichweite dieser Daten.
- Der HDI bewegt sich über 22 Jahre träge und monoton nach oben. In der
  FE-Schätzung konkurriert die Capture Ratio daher mit einem starken
  Zeittrend, der über die Jahres-Fixed-Effects absorbiert wird.

Quelle: World Bank WDI, ICTD/UNU-WIDER GRD 2023, UNDP HDI; eigene Berechnung.
Erzeugt von `src/05_zusammenhang_hdi.py`.
