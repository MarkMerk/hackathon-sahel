# Tab. 2b — Capture Ratio und menschliche Entwicklung

Spearman-Rangkorrelation auf **Länder-Periodenmitteln** (ein Wert je Land
und Periode, mindestens 3 gültige Jahre). Rangbasiert, weil beide
Größen schief verteilt sind und der Zusammenhang nicht linear sein muss.

## Capture Ratio ↔ HDI

| Ebene | n | Spearman ρ | p |
|---|---|---|---|
| alle Perioden | 68 | 0,515 | < 0,001 |
| 2000–2007 | 21 | 0,577 | 0,006 |
| 2008–2014 | 26 | 0,456 | 0,019 |
| 2015–2021 | 21 | 0,679 | < 0,001 |

## Capture Ratio ↔ Stromzugang (% der Bevölkerung)

| Ebene | n | Spearman ρ | p |
|---|---|---|---|
| alle Perioden | 69 | 0,429 | < 0,001 |
| 2000–2007 | 22 | 0,456 | 0,033 |
| 2008–2014 | 26 | 0,355 | 0,076 |
| 2015–2021 | 21 | 0,551 | 0,010 |

## Two-way-Fixed-Effects-OLS (Ergänzung)

Modell: `hdi ~ capture_ratio + log(BIP pro Kopf) + Land-FE + Jahr-FE`,
Standardfehler geclustert nach Land.

Koeffizient der Capture Ratio: **0,0007** (SE 0,0005, p 0,177, 95-%-KI [-0,0003; 0,0017]), n = 442 Länderjahre aus 28 Ländern, R² = 0,985 (inkl. Fixed Effects).

Lesart: Eine um 0,1 höhere Capture Ratio geht mit einem um 0,0001 HDI-Punkten abweichenden Wert einher — **innerhalb** eines Landes und nach Kontrolle des Jahres und des BIP pro Kopf. Das ist eine Assoziation; die Wirkungsrichtung ist nicht identifiziert.

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

Quelle: World Bank WDI, UNU-WIDER GRD 2025, UNDP HDI; eigene Berechnung.
Erzeugt von `src/05_zusammenhang_hdi.py`.
