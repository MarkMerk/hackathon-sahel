# Anhang D — Tabellen

Alle Tabellen in diesem Anhang sind skriptgeneriert; die zugrunde liegenden Skripte sind in Anhang A dokumentiert.

## D.1 Datenquellen und Indikatoren

**Tabelle D.1**
*Datenquellen und Indikatoren*

Erzeugt von: `src/03_capture_ratio.py` (Datengrundlage: `src/01_laden.py`)

| Indikator | Variable im Panel | Quelle | Einheit | Abdeckung |
|---|---|---|---|---|
| Rohstoffrenten | `rents_pct_gdp` | World Bank WDI, `NY.GDP.TOTL.RT.ZS` | % des BIP | 1014 Länderjahre |
| Staatliche Ressourceneinnahmen | `res_rev_pct_gdp` | UNU-WIDER GRD 2025, *Total Resource Revenue* | % des BIP | 478 Länderjahre |
| Ressourcensteuern | `res_tax_pct_gdp` | UNU-WIDER GRD 2025, *Resource Taxes* | % des BIP | 269 Länderjahre |
| Bruttoinlandsprodukt pro Kopf | `gdppc_const` | World Bank WDI, `NY.GDP.PCAP.KD` | konstante US-Dollar (2015) | 1032 Länderjahre |
| Zugang zu Elektrizität | `elec_access_pct` | World Bank WDI, `EG.ELC.ACCS.ZS` | % der Bevölkerung | 1040 Länderjahre |
| Index der menschlichen Entwicklung | `hdi` | UNDP HDR 2025 | Index 0–1 | 985 Länderjahre |
| Abschöpfungsquote | `capture_ratio` | eigene Berechnung: `res_rev_pct_gdp / rents_pct_gdp` | einheitenlos | 455 Länderjahre |

Grundgesamtheit: 48 Länder der World-Bank-Region Subsahara-Afrika, 2000–2021 (1056 Länderjahre).
Die Abschöpfungsquote wird nur für Länderjahre mit Rohstoffrenten von mindestens 1 % des BIP berechnet, da der Quotient bei kleinerem Nenner instabil wird.

Quelle: World Bank WDI, UNU-WIDER GRD 2025, UNDP HDI; eigene Berechnung.

## D.2 Datenabdeckung je Land (2000–2021)

**Tabelle D.2**
*Datenabdeckung je Land (2000–2021)*

Erzeugt von: `src/02_abdeckung.py`

Gezählt werden Jahre mit vorhandenem Wert; `*` markiert eine nicht lückenlose Spanne. „Jahre beides" = Jahre mit Renten **und** Ressourceneinnahmen; „Jahre Capture Ratio" zusätzlich eingeschränkt auf Renten ≥ 1 % BIP.

### Entscheidung GRD vs. Plan B

Kriterium (`docs/Forschungsdesign.md` §5.7): mindestens **3** der fünf Sahel-Kernländer mit mindestens **10** Jahren Renten *und* GRD-Ressourceneinnahmen.

Erfüllt: **4 von 5** (NER, BFA, MRT, TCD).

**Ergebnis: Hauptplan — Analyse auf Basis des GRD.**

### Abdeckung je Land

| Land | ISO3 | Gruppe | Jahre Renten | Jahre Ressourceneinnahmen | Jahre beides | Jahre Capture Ratio | Jahre HDI | Spanne Renten | Spanne Einnahmen |
|---|---|---|---|---|---|---|---|---|---|
| Niger | NER | Sahel | 22 | 22 | 22 | 22 | 22 | 2000–2021 | 2000–2021 |
| Burkina Faso | BFA | Sahel | 22 | 21 | 21 | 21 | 17 | 2000–2021 | 2000–2020 |
| Mauritania | MRT | Sahel | 22 | 18 | 18 | 18 | 22 | 2000–2021 | 2000–2021* |
| Chad | TCD | Sahel | 22 | 18 | 18 | 18 | 22 | 2000–2021 | 2004–2021 |
| Mali | MLI | Sahel | 22 | 4 | 4 | 4 | 22 | 2000–2021 | 2013–2016 |
| Sudan | SDN | Sahel (erw.) | 22 | 21 | 21 | 21 | 14 | 2000–2021 | 2000–2020 |
| Senegal | SEN | Sahel (erw.) | 22 | 17 | 17 | 17 | 22 | 2000–2021 | 2005–2021 |
| Angola | AGO | übriges SSA | 22 | 22 | 22 | 22 | 22 | 2000–2021 | 2000–2021 |
| Botswana | BWA | übriges SSA | 22 | 22 | 22 | 14 | 22 | 2000–2021 | 2000–2021 |
| Cameroon | CMR | übriges SSA | 22 | 22 | 22 | 22 | 22 | 2000–2021 | 2000–2021 |
| Congo, Rep. | COG | übriges SSA | 22 | 22 | 22 | 22 | 22 | 2000–2021 | 2000–2021 |
| Gabon | GAB | übriges SSA | 22 | 22 | 22 | 22 | 22 | 2000–2021 | 2000–2021 |
| Ghana | GHA | übriges SSA | 22 | 22 | 22 | 22 | 22 | 2000–2021 | 2000–2021 |
| Guinea | GIN | übriges SSA | 22 | 22 | 22 | 22 | 22 | 2000–2021 | 2000–2021 |
| Namibia | NAM | übriges SSA | 22 | 22 | 22 | 17 | 22 | 2000–2021 | 2000–2021 |
| Nigeria | NGA | übriges SSA | 22 | 22 | 22 | 22 | 22 | 2000–2021 | 2000–2021 |
| Sierra Leone | SLE | übriges SSA | 22 | 22 | 22 | 22 | 22 | 2000–2021 | 2000–2021 |
| Zambia | ZMB | übriges SSA | 22 | 22 | 22 | 22 | 22 | 2000–2021 | 2000–2021 |
| Madagascar | MDG | übriges SSA | 22 | 21 | 21 | 21 | 22 | 2000–2021 | 2000–2020 |
| Uganda | UGA | übriges SSA | 22 | 19 | 19 | 19 | 22 | 2000–2021 | 2003–2021 |
| Equatorial Guinea | GNQ | übriges SSA | 18 | 22 | 18 | 18 | 22 | 2000–2021* | 2000–2021 |
| Sao Tome and Principe | STP | übriges SSA | 21 | 12 | 12 | 12 | 17 | 2001–2021 | 2005–2021* |
| Cote d'Ivoire | CIV | übriges SSA | 22 | 11 | 11 | 11 | 22 | 2000–2021 | 2000–2010 |
| Congo, Dem. Rep. | COD | übriges SSA | 22 | 11 | 11 | 11 | 22 | 2000–2021 | 2010–2021* |
| Liberia | LBR | übriges SSA | 22 | 4 | 4 | 4 | 22 | 2000–2021 | 2012–2015 |
| South Sudan | SSD | übriges SSA | 8 | 10 | 4 | 4 | 12 | 2008–2015 | 2012–2021 |
| Zimbabwe | ZWE | übriges SSA | 22 | 3 | 3 | 3 | 22 | 2000–2021 | 2011–2013 |
| Togo | TGO | übriges SSA | 22 | 2 | 2 | 2 | 22 | 2000–2021 | 2000–2001 |
| Burundi | BDI | übriges SSA | 22 | 0 | 0 | 0 | 22 | 2000–2021 | — |
| Benin | BEN | übriges SSA | 22 | 0 | 0 | 0 | 22 | 2000–2021 | — |
| Central African Republic | CAF | übriges SSA | 22 | 0 | 0 | 0 | 21 | 2000–2021 | — |
| Comoros | COM | übriges SSA | 22 | 0 | 0 | 0 | 22 | 2000–2021 | — |
| Cabo Verde | CPV | übriges SSA | 22 | 0 | 0 | 0 | 22 | 2000–2021 | — |
| Eritrea | ERI | übriges SSA | 12 | 0 | 0 | 0 | 17 | 2000–2011 | — |
| Ethiopia | ETH | übriges SSA | 22 | 0 | 0 | 0 | 22 | 2000–2021 | — |
| Gambia, The | GMB | übriges SSA | 22 | 0 | 0 | 0 | 22 | 2000–2021 | — |
| Guinea-Bissau | GNB | übriges SSA | 22 | 0 | 0 | 0 | 17 | 2000–2021 | — |
| Kenya | KEN | übriges SSA | 22 | 0 | 0 | 0 | 22 | 2000–2021 | — |
| Lesotho | LSO | übriges SSA | 22 | 0 | 0 | 0 | 22 | 2000–2021 | — |
| Mozambique | MOZ | übriges SSA | 22 | 0 | 0 | 0 | 22 | 2000–2021 | — |
| Mauritius | MUS | übriges SSA | 22 | 0 | 0 | 0 | 22 | 2000–2021 | — |
| Malawi | MWI | übriges SSA | 22 | 0 | 0 | 0 | 22 | 2000–2021 | — |
| Rwanda | RWA | übriges SSA | 22 | 0 | 0 | 0 | 22 | 2000–2021 | — |
| Somalia, Fed. Rep. | SOM | übriges SSA | 9 | 0 | 0 | 0 | 0 | 2013–2021 | — |
| Eswatini | SWZ | übriges SSA | 22 | 0 | 0 | 0 | 22 | 2000–2021 | — |
| Seychelles | SYC | übriges SSA | 22 | 0 | 0 | 0 | 12 | 2000–2021 | — |
| Tanzania | TZA | übriges SSA | 22 | 0 | 0 | 0 | 22 | 2000–2021 | — |
| South Africa | ZAF | übriges SSA | 22 | 0 | 0 | 0 | 22 | 2000–2021 | — |

### Zusammenfassung nach Gruppen

| Gruppe | Länder | Ø Jahre Renten | Ø Jahre Einnahmen | Ø Jahre beides |
|---|---|---|---|---|
| Sahel | 5 | 22.0 | 16.6 | 16.6 |
| Sahel (erw.) | 2 | 22.0 | 19.0 | 19.0 |
| übriges SSA | 41 | 21.0 | 8.7 | 8.5 |

Quelle: World Bank WDI, UNU-WIDER GRD 2025, UNDP HDI; eigene Berechnung.

## D.3 Capture Ratio: Sahel vs. übriges Subsahara-Afrika

**Tabelle D.3**
*Capture Ratio: Sahel vs. übriges Subsahara-Afrika*

Erzeugt von: `src/04_gruppenvergleich.py`

Einheit der Analyse: **Länder-Periodenmittel** der zentriert 3-jährig geglätteten Capture Ratio (Forschungsdesign §3; ein Wert je Land und Periode, Länder mit weniger als 3 gültigen Jahren in einer Periode bleiben für diese Periode unberücksichtigt). Test: Mann-Whitney-U (zweiseitig). Effektgröße: Cliff's Delta (negativ = Sahel niedriger). Eine Einordnung nach Romano et al. (2006) entfällt, weil sie bei vier Ländern je Periode eine Genauigkeit suggerieren würde, die die Datenlage nicht hergibt.

| Periode | n Sahel | Median Sahel | IQR Sahel | n übr. SSA | Median übr. SSA | IQR übr. SSA | U | p | Cliff's δ |
|---|---|---|---|---|---|---|---|---|---|
| 2000–2007 | 4 | 0,10 | 0,03–0,28 | 18 | 0,51 | 0,10–0,71 | 21,0 | 0,227 | -0,42 (n zu klein für Einordnung) |
| 2008–2014 | 4 | 0,21 | 0,04–0,38 | 22 | 0,35 | 0,09–0,76 | 25,0 | 0,197 | -0,43 (n zu klein für Einordnung) |
| 2015–2021 | 4 | 0,16 | 0,06–0,32 | 17 | 0,26 | 0,11–0,45 | 25,0 | 0,462 | -0,26 (n zu klein für Einordnung) |

**Lesehilfe:** Die Capture Ratio ist einheitenlos und gibt den Anteil der Rohstoffrenten an, der als Ressourceneinnahme im Staatshaushalt ankommt (0,30 = 30 %). Cliff's δ = −0,50 bedeutet: In 75 % der Länderpaare liegt das Sahel-Land unter dem Vergleichsland.

**Hinweise zur Interpretation:**
- Der Test prüft, ob ein zufällig gezogenes Sahel-Land über einem zufällig gezogenen Vergleichsland liegt, nicht Kausalität. Alle Befunde sind **Assoziationen**.
- Mit n = 4 Sahel-Ländern je Periode ist die Teststärke gering. Ein nicht signifikantes Ergebnis heißt „für eine Aussage reichen die Daten nicht", nicht „kein Unterschied". Deshalb steht die Effektgröße vor dem p-Wert.
- Länderjahre mit Rohstoffrenten < 1 % BIP erhalten in `panel.csv` keine Capture Ratio (kleiner Nenner) und gehen daher nicht ein.
- Die Vergleichsgruppe enthält Sudan und Senegal; Variante (b) in Tab. D.5 ordnet sie dem erweiterten Sahel zu.
- Der Interquartilsabstand beruht bei n = 4 auf Interpolation zwischen wenigen Werten und ist nur illustrativ.
- Nicht in allen Perioden vertretene Sahel-Länder: MLI (fehlt in 2000–2007, 2008–2014, 2015–2021).
- 19 Länderjahre mit Capture Ratio > 1,5 sind enthalten und geflaggt (`flag_ratio_high`); sie entstehen durch Timing zwischen Rentenanfall und Zahlungseingang sowie durch Preisschocks und wurden nicht entfernt.

Quelle: World Bank WDI, UNU-WIDER GRD 2025, UNDP HDI; eigene Berechnung.

## D.4 Capture Ratio und menschliche Entwicklung

**Tabelle D.4**
*Capture Ratio und menschliche Entwicklung*

Erzeugt von: `src/05_zusammenhang_hdi.py`

Spearman-Rangkorrelation auf **Länder-Periodenmitteln** (ein Wert je Land und Periode, mindestens 3 gültige Jahre). Rangbasiert, weil beide Größen schief verteilt sind und der Zusammenhang nicht linear sein muss.

### Capture Ratio ↔ HDI

| Ebene | n | Spearman ρ | p |
|---|---|---|---|
| Querschnitt (ein Wert je Land) | 26 | 0,517 | 0,007 |
| 2000–2007 | 21 | 0,577 | 0,006 |
| 2008–2014 | 26 | 0,456 | 0,019 |
| 2015–2021 | 21 | 0,679 | < 0,001 |

### Capture Ratio ↔ Stromzugang (% der Bevölkerung)

| Ebene | n | Spearman ρ | p |
|---|---|---|---|
| Querschnitt (ein Wert je Land) | 26 | 0,410 | 0,038 |
| 2000–2007 | 22 | 0,456 | 0,033 |
| 2008–2014 | 26 | 0,355 | 0,076 |
| 2015–2021 | 21 | 0,551 | 0,010 |

### Two-way-Fixed-Effects-OLS (Ergänzung)

Modell: `hdi ~ capture_ratio + log(BIP pro Kopf) + Land-FE + Jahr-FE`, Standardfehler geclustert nach Land.

Koeffizient der Capture Ratio: **0,0007** (SE 0,0005, p 0,177, 95-%-KI [-0,0003; 0,0017]), n = 442 Länderjahre aus 28 Ländern, R² = 0,985 — dieses R² stammt fast vollständig aus den Länder-Fixed-Effects; das inkrementelle R² der Capture Ratio beträgt etwa 0,00005.

**Diese Schätzung ist nicht belastbar und wird nur exploratorisch berichtet.** Drei Gründe: Das Vorzeichen wechselt mit der Spezifikation (nur Länder-Fixed-Effects: −0,0019, p = 0,041, also negativ und nominell signifikant). Die scheinbare Präzision stammt von wenigen Extremwerten: Ohne die 19 geflaggten Beobachtungen — 14 davon Botswana — steigt der Standardfehler um das Achtzehnfache auf 0,0090, das Konfidenzintervall umspannt [−0,015; +0,021]. Und die Clusterzahl ist klein, fünf Länder haben weniger als fünf Beobachtungen. Aus dem Nullbefund folgt daher **nicht**, dass es innerhalb der Länder keinen Zusammenhang gibt — es folgt, dass diese Daten die Frage nicht beantworten.

### Einordnung

- **Assoziation, keine Kausalität.** Eine höhere Abschöpfungsquote und ein höherer HDI können beide Folge einer dritten Größe sein — etwa staatlicher Verwaltungskapazität oder der Qualität fiskalischer Institutionen. Auch die umgekehrte Richtung ist denkbar: entwickeltere Staaten können Renten besser besteuern.
- Die Capture Ratio sagt nichts darüber, **wofür** die Einnahmen verwendet werden. Ein hoher Wert bedeutet nicht, dass die Mittel entwicklungswirksam eingesetzt werden; die Verteilung innerhalb des Staates bleibt außerhalb der Reichweite dieser Daten.
- Der Nullbefund der Fixed-Effects-Schätzung liegt **nicht** daran, dass der Koeffizient nicht identifiziert wäre: Die Capture Ratio behält nach Abzug der Länder- und Jahreseffekte rund ein Drittel ihrer Streuung. Er liegt an der Hebelwirkung weniger Extremwerte und an der Spezifikationsabhängigkeit — siehe oben.
- Die Tests der Gruppenvergleiche laufen auf Länder-Periodenmitteln, diese Schätzung auf Länderjahren. Fixed Effects benötigen Variation innerhalb der Länder, die drei Periodenmittel je Land nicht hergeben; die geclusterten Standardfehler adressieren die Abhängigkeit der Jahre eines Landes. Diese Abweichung von der Analyseeinheit ist bewusst und in Abschnitt 4 benannt.

Quelle: World Bank WDI, UNU-WIDER GRD 2025, UNDP HDI; eigene Berechnung.

## D.5 Robustheitsprüfungen

**Tabelle D.5**
*Robustheitsprüfungen*

Erzeugt von: `src/06_robustheit.py`

Der Gruppenvergleich aus Tab. D.3 wird unter veränderten Spezifikationen wiederholt. Einheit bleibt das **Länder-Periodenmittel**; Test ist der zweiseitige Mann-Whitney-U, Effektgröße Cliff's δ (negativ = Sahel niedriger).

### Kernkontrast: mit und ohne Ölstaaten in der Vergleichsgruppe

Die Vergleichsgruppe enthält je Periode bis zu sechs Ölstaaten (NGA, AGO, COG, GAB, GNQ, SSD; Südsudan erreicht nur 2008–2014 die Mindestzahl Jahre). Werden sie entfernt, während die Sahel-Gruppe unverändert bleibt, schrumpft der Gruppenabstand erheblich. Das ist kein Nebenergebnis, sondern die zentrale Einschränkung des Regionsvergleichs.

| Periode | Median Sahel | Median Vergleich (mit Öl) | δ | p | Median Vergleich (ohne Öl) | δ | p |
|---|---|---|---|---|---|---|---|
| 2000–2007 | 0,10 | 0,51 | -0,42 | 0,227 | 0,14 | -0,27 | 0,477 |
| 2008–2014 | 0,21 | 0,35 | -0,43 | 0,197 | 0,15 | -0,22 | 0,554 |
| 2015–2021 | 0,16 | 0,26 | -0,26 | 0,462 | 0,16 | -0,08 | 0,862 |

### Abschöpfung nach Rohstofftyp (alle Länder, ohne Regionsbezug)

Diese Aufschlüsselung lässt die Sahel-Zugehörigkeit außer Acht. Positives Cliff's δ bedeutet: Länder mit Ölförderung schöpfen mehr ab.

**Diese Auswertung ist post hoc**: Sie ist im Forschungsdesign §5.6 nicht vorgesehen und wurde nach Sichtung der Regionsergebnisse ergänzt. Die p-Werte sind nicht für multiples Testen adjustiert (siehe unten).

Erste Abgrenzung nach der Panelspalte `oil_state` (NGA, AGO, GNQ, COG, GAB, SSD, TCD). Diese Spalte wurde für den Robustheits-Ausschluss definiert und ist als Öl-Kennzeichnung unvollständig:

| Periode | n Öl | Median Öl | n ohne Öl | Median ohne Öl | Cliff's δ | p |
|---|---|---|---|---|---|---|
| 2000–2007 | 6 | 0,52 | 16 | 0,12 | 0,31 | 0,294 |
| 2008–2014 | 7 | 0,74 | 19 | 0,15 | 0,74 | 0,003 |
| 2015–2021 | 6 | 0,46 | 15 | 0,14 | 0,64 | 0,023 |

Mit erweiterter Abgrenzung (zusätzlich Kamerun, Sudan und Mauretanien, die ebenfalls Erdöl fördern):

| Periode | n Öl | Median Öl | n ohne Öl | Median ohne Öl | Cliff's δ | p |
|---|---|---|---|---|---|---|
| 2000–2007 | 9 | 0,62 | 13 | 0,11 | 0,54 | 0,038 |
| 2008–2014 | 10 | 0,66 | 16 | 0,10 | 0,76 | 0,001 |
| 2015–2021 | 9 | 0,44 | 12 | 0,10 | 0,78 | 0,003 |

Der Kontrast nach Rohstofftyp ist deskriptiv deutlicher als der nach Region und unter beiden Abgrenzungen gleichgerichtet; mit der erweiterten Abgrenzung fällt er stärker aus. Er hält auch der Holm-Korrektur über alle 17 in dieser Arbeit berichteten Tests stand (erweiterte Abgrenzung: p_Holm = 0,020 für 2008–2014 und 0,038 für 2015–2021).

Einschränkungen: Die Auswertung ist post hoc, und die drei Periodentests beruhen auf denselben wenigen Ländern — sie sind keine drei unabhängigen Belege. Die Klassifikation nach Rohstofftyp ist eine Vereinfachung; die Länder fördern jeweils mehrere Rohstoffe in unterschiedlichem Anteil.

### Ergebnisse je Spezifikation

| Spezifikation | Periode | n Sahel | Median Sahel | n Vergleich | Median Vergleich | p | Cliff's δ |
|---|---|---|---|---|---|---|---|
| **Haupt** — Hauptspezifikation (Sahel-Definition 5 Länder, ≥ 3 gültige Jahre) | 2000–2007 | 4 | 0,10 | 18 | 0,51 | 0,227 | -0,42 (n zu klein für Einordnung) |
|  | 2008–2014 | 4 | 0,21 | 22 | 0,35 | 0,197 | -0,43 (n zu klein für Einordnung) |
|  | 2015–2021 | 4 | 0,16 | 17 | 0,26 | 0,462 | -0,26 (n zu klein für Einordnung) |
| **a1** — Vergleichsgruppe ohne Ölstaaten (Sahel unverändert, inkl. TCD) | 2000–2007 | 4 | 0,10 | 13 | 0,14 | 0,477 | -0,27 (n zu klein für Einordnung) |
|  | 2008–2014 | 4 | 0,21 | 16 | 0,15 | 0,554 | -0,22 (n zu klein für Einordnung) |
|  | 2015–2021 | 4 | 0,16 | 12 | 0,16 | 0,862 | -0,08 (n zu klein für Einordnung) |
| **a2** — ohne Ölstaaten in beiden Gruppen (ohne TCD, Sahel n = 3) | 2000–2007 | 3 | 0,03 | 13 | 0,14 | 0,364 | -0,38 (n zu klein für Einordnung) |
|  | 2008–2014 | 3 | 0,05 | 16 | 0,15 | 0,303 | -0,42 (n zu klein für Einordnung) |
|  | 2015–2021 | 3 | 0,07 | 12 | 0,16 | 0,734 | -0,17 (n zu klein für Einordnung) |
| **b** — Sahel erweitert (+ SDN, SEN) | 2000–2007 | 6 | 0,13 | 16 | 0,51 | 0,367 | -0,27 (klein) |
|  | 2008–2014 | 6 | 0,23 | 20 | 0,35 | 0,196 | -0,37 (mittel) |
|  | 2015–2021 | 6 | 0,18 | 15 | 0,37 | 0,381 | -0,27 (klein) |
| **c** — 5- statt 3-Jahres-Glättung | 2000–2007 | 4 | 0,11 | 18 | 0,51 | 0,262 | -0,39 (n zu klein für Einordnung) |
|  | 2008–2014 | 4 | 0,21 | 22 | 0,35 | 0,197 | -0,43 (n zu klein für Einordnung) |
|  | 2015–2021 | 4 | 0,16 | 17 | 0,26 | 0,462 | -0,26 (n zu klein für Einordnung) |
| **c0** — ungeglättete Jahreswerte (ohne Glättung) | 2000–2007 | 4 | 0,10 | 18 | 0,51 | 0,300 | -0,36 (n zu klein für Einordnung) |
|  | 2008–2014 | 4 | 0,21 | 22 | 0,25 | 0,252 | -0,39 (n zu klein für Einordnung) |
|  | 2015–2021 | 4 | 0,15 | 17 | 0,27 | 0,517 | -0,24 (n zu klein für Einordnung) |
| **f** — Quotient der Periodensummen statt Mittel der Jahresquotienten | 2000–2007 | 4 | 0,09 | 18 | 0,49 | 0,166 | -0,47 (n zu klein für Einordnung) |
|  | 2008–2014 | 4 | 0,21 | 22 | 0,26 | 0,252 | -0,39 (n zu klein für Einordnung) |
|  | 2015–2021 | 4 | 0,15 | 17 | 0,21 | 0,410 | -0,29 (n zu klein für Einordnung) |
| **g0,5** — fehlende Ressourceneinnahmen mit 0.5 % BIP imputiert | 2000–2007 | 5 | 0,10 | 39 | 0,13 | 0,366 | -0,26 (klein) |
|  | 2008–2014 | 5 | 0,11 | 40 | 0,12 | 0,766 | -0,09 (vernachlässigbar) |
|  | 2015–2021 | 5 | 0,09 | 38 | 0,12 | 0,898 | -0,04 (vernachlässigbar) |
| **g0,8** — fehlende Ressourceneinnahmen mit 0.8 % BIP imputiert | 2000–2007 | 5 | 0,12 | 39 | 0,18 | 0,311 | -0,29 (klein) |
|  | 2008–2014 | 5 | 0,13 | 40 | 0,15 | 0,314 | -0,29 (klein) |
|  | 2015–2021 | 5 | 0,12 | 38 | 0,17 | 0,672 | -0,13 (vernachlässigbar) |
| **d** — ohne geflaggte Länderjahre (Capture Ratio > 1,5) | 2000–2007 | 4 | 0,10 | 16 | 0,37 | 0,335 | -0,34 (n zu klein für Einordnung) |
|  | 2008–2014 | 4 | 0,21 | 19 | 0,17 | 0,324 | -0,34 (n zu klein für Einordnung) |
|  | 2015–2021 | 4 | 0,16 | 17 | 0,26 | 0,462 | -0,26 (n zu klein für Einordnung) |
| **e** — mindestens 5 statt 3 gültige Jahre je Periode | 2000–2007 | 3 | 0,03 | 14 | 0,37 | 0,362 | -0,38 (n zu klein für Einordnung) |
|  | 2008–2014 | 3 | 0,05 | 17 | 0,47 | 0,118 | -0,61 (n zu klein für Einordnung) |
|  | 2015–2021 | 4 | 0,16 | 17 | 0,26 | 0,462 | -0,26 (n zu klein für Einordnung) |

### Vorzeichenstabilität der Effektgröße

Entscheidend ist nicht, ob p unter 0,05 bleibt — bei vier Sahel-Ländern ist die Teststärke dafür zu gering —, sondern ob die **Richtung** des Unterschieds erhalten bleibt. Zu beachten: Die Zellen sind **keine unabhängigen Replikationen**, da sie auf denselben vier Sahel-Ländern beruhen. In Variante (a1) fällt die Effektgröße 2015–2021 auf −0,08 und ist damit vernachlässigbar klein; als Bestätigung einer Richtung trägt sie kaum.

| Variante | Beschreibung | 2000–2007 | 2008–2014 | 2015–2021 |
|---|---|---|---|---|
| a1 | Vergleichsgruppe ohne Ölstaaten (Sahel unverändert, inkl. TCD) | ja | ja | ja |
| a2 | ohne Ölstaaten in beiden Gruppen (ohne TCD, Sahel n = 3) | ja | ja | ja |
| b | Sahel erweitert (+ SDN, SEN) | ja | ja | ja |
| c | 5- statt 3-Jahres-Glättung | ja | ja | ja |
| c0 | ungeglättete Jahreswerte (ohne Glättung) | ja | ja | ja |
| f | Quotient der Periodensummen statt Mittel der Jahresquotienten | ja | ja | ja |
| g0,5 | fehlende Ressourceneinnahmen mit 0.5 % BIP imputiert | ja | ja | ja |
| g0,8 | fehlende Ressourceneinnahmen mit 0.8 % BIP imputiert | ja | ja | ja |
| d | ohne geflaggte Länderjahre (Capture Ratio > 1,5) | ja | ja | ja |
| e | mindestens 5 statt 3 gültige Jahre je Periode | ja | ja | ja |

### Einordnung

- Variante **(a1)** hält die Sahel-Gruppe konstant und entfernt die Ölstaaten nur aus der Vergleichsgruppe. Sie isoliert damit den Beitrag des Rohstofftyps zum Gruppenabstand. Das Vorzeichen bleibt negativ, die Effektgröße fällt jedoch deutlich — der sichtbare Abstand zwischen Sahel und übrigem Subsahara-Afrika erklärt sich weitgehend daraus, dass die Vergleichsgruppe Ölstaaten enthält.
- Variante **(a2)** entfernt die Ölstaaten aus beiden Gruppen und damit auch Tschad aus dem Sahel. Die Sahel-Gruppe schrumpft auf drei Länder; Unterschiede sind hier teils Folge der kleineren Gruppe.
- Variante **(c)** glättet stärker und reduziert Timing-Rauschen zwischen Rentenanfall und Zahlungseingang, verliert aber Randjahre und damit Beobachtungen in den Außenperioden.
- Variante **(c0)** rechnet ohne Glättung und zeigt, dass der Befund nicht durch die Glättung entsteht. Bis 14:20 war diese Variante versehentlich die Hauptspezifikation; die Umstellung auf die im Design vorgesehene 3-Jahres-Glättung verstärkt den Befund leicht.
- Variante **(d)** prüft, ob der Befund von einzelnen Länderjahren mit Capture Ratio > 1,5 getragen wird. Diese Werte sind nicht unplausibel (Nachzahlungen, Preisverfall bei nachlaufenden Zahlungen), verzerren Mittelwerte aber stark. Zu beachten: Botswana verliert dadurch alle 14 gültigen Jahre und fällt vollständig aus der Vergleichsgruppe; (d) ist faktisch ein Länderausschluss, keine bloße Ausreißerbereinigung.
- Variante **(f)** bildet die Capture Ratio als Quotient der Periodensummen. Das gewichtet Jahre mit kleinem Nenner nicht über, ist inhaltlich näher an der Forschungsfrage und stützt den Befund.
- **Multiples Testen:** Diese Arbeit berichtet 17 Signifikanztests. Die p-Werte in dieser Tabelle sind nicht adjustiert; nach Holm-Korrektur über alle berichteten Tests bleibt kein Regionstest signifikant — er ist es auch unadjustiert nicht.
- Alle Befunde sind **Assoziationen**, keine Kausalität. Die Robustheitsprüfung sagt etwas über die Stabilität des deskriptiven Musters, nicht über dessen Ursachen.

Quelle: World Bank WDI, UNU-WIDER GRD 2025, UNDP HDI; eigene Berechnung.
