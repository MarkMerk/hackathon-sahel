# Tab. 2b — Capture Ratio und menschliche Entwicklung

Spearman-Rangkorrelation auf **Länder-Periodenmitteln** (ein Wert je Land
und Periode, mindestens 3 gültige Jahre). Rangbasiert, weil beide
Größen schief verteilt sind und der Zusammenhang nicht linear sein muss.

## Capture Ratio ↔ HDI

| Ebene | n | Spearman ρ | p |
|---|---|---|---|
| Querschnitt (ein Wert je Land) | 26 | 0,517 | 0,007 |
| 2000–2007 | 21 | 0,577 | 0,006 |
| 2008–2014 | 26 | 0,456 | 0,019 |
| 2015–2021 | 21 | 0,679 | < 0,001 |

## Capture Ratio ↔ Stromzugang (% der Bevölkerung)

| Ebene | n | Spearman ρ | p |
|---|---|---|---|
| Querschnitt (ein Wert je Land) | 26 | 0,410 | 0,038 |
| 2000–2007 | 22 | 0,456 | 0,033 |
| 2008–2014 | 26 | 0,355 | 0,076 |
| 2015–2021 | 21 | 0,551 | 0,010 |

## Two-way-Fixed-Effects-OLS (Ergänzung)

Modell: `hdi ~ capture_ratio + log(BIP pro Kopf) + Land-FE + Jahr-FE`,
Standardfehler geclustert nach Land.

Koeffizient der Capture Ratio: **0,0007** (SE 0,0005, p 0,177, 95-%-KI [-0,0003; 0,0017]), n = 442 Länderjahre aus 28 Ländern, R² = 0,985 — dieses R² stammt fast vollständig aus den Länder-Fixed-Effects; das inkrementelle R² der Capture Ratio beträgt etwa 0,00005.

**Diese Schätzung ist nicht belastbar und wird nur exploratorisch berichtet.** Drei Gründe: Das Vorzeichen wechselt mit der Spezifikation (nur Länder-Fixed-Effects: −0,0019, p = 0,041, also negativ und nominell signifikant). Die scheinbare Präzision stammt von wenigen Extremwerten: Ohne die 19 geflaggten Beobachtungen — 14 davon Botswana — steigt der Standardfehler um das Achtzehnfache auf 0,0090, das Konfidenzintervall umspannt [−0,015; +0,021]. Und die Clusterzahl ist klein, fünf Länder haben weniger als fünf Beobachtungen. Aus dem Nullbefund folgt daher **nicht**, dass es innerhalb der Länder keinen Zusammenhang gibt — es folgt, dass diese Daten die Frage nicht beantworten.

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
- Der Nullbefund der Fixed-Effects-Schätzung liegt **nicht** daran, dass der
  Koeffizient nicht identifiziert wäre: Die Capture Ratio behält nach Abzug
  der Länder- und Jahreseffekte rund ein Drittel ihrer Streuung. Er liegt an
  der Hebelwirkung weniger Extremwerte und an der
  Spezifikationsabhängigkeit — siehe oben.
- Die Tests der Gruppenvergleiche laufen auf Länder-Periodenmitteln, diese
  Schätzung auf Länderjahren. Fixed Effects benötigen Variation innerhalb der
  Länder, die drei Periodenmittel je Land nicht hergeben; die geclusterten
  Standardfehler adressieren die Abhängigkeit der Jahre eines Landes. Diese
  Abweichung von der Analyseeinheit ist bewusst und in Abschnitt 4 benannt.

Quelle: World Bank WDI, UNU-WIDER GRD 2025, UNDP HDI; eigene Berechnung.
Erzeugt von `src/05_zusammenhang_hdi.py`.
