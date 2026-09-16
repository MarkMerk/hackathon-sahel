# Zahlen für den Text

> Verbindliche Quelle für alle Zahlenangaben in der Abhandlung. Keine Zahl in einen Textentwurf, die nicht hier steht. Erzeugt am 16.09.2026.

## Mark

_Erzeugt von `src/03_capture_ratio.py` aus `data/processed/panel.csv` am 16.09.2026._

### Datengrundlage

- Analysefenster: 2000–2021
- Länder der World-Bank-Region Subsahara-Afrika im Panel: **48**
- Länderjahre insgesamt: **1056**
- davon mit Rohstoffrenten (WDI): **1014**
- davon mit Ressourceneinnahmen (GRD): **478**
- davon mit berechenbarer Capture Ratio (Renten ≥ 1 % BIP): **455** in 28 Ländern
- geflaggte Werte > 1,5: **19** (4,2 % der gültigen Werte)

### Capture Ratio je Sahel-Kernland (alle Jahre)

| Land | ISO3 | n Jahre | Median | Mittelwert | Minimum | Maximum |
|---|---|---|---|---|---|---|
| Mali | MLI | 4 | 0,200 | 0,208 | 0,172 | 0,258 |
| Burkina Faso | BFA | 21 | 0,022 | 0,033 | 0,001 | 0,112 |
| Niger | NER | 22 | 0,038 | 0,040 | 0,022 | 0,072 |
| Chad | TCD | 18 | 0,260 | 0,285 | 0,046 | 0,499 |
| Mauritania | MRT | 18 | 0,394 | 0,542 | 0,138 | 1,355 |

### Gruppenvergleich (gepoolte Länderjahre, nur deskriptiv)

| Gruppe | n Länderjahre | n Länder | Median | 1. Quartil | 3. Quartil |
|---|---|---|---|---|---|
| Sahel (5 Kernländer) | 83 | 5 | 0,075 | 0,036 | 0,285 |
| übriges Subsahara-Afrika | 334 | 21 | 0,320 | 0,075 | 0,654 |

> Hinweis: Tests laufen auf Länder-Periodenmitteln (`src/04_gruppenvergleich.py`), nicht auf diesen gepoolten Werten. Die Tabelle dient nur der Beschreibung.

### Entwicklung über die Perioden (Median der Länder-Periodenmittel)

| Periode | Sahel: Median | n Länder | übriges SSA: Median | n Länder |
|---|---|---|---|---|
| 2000–2007 | 0,097 | 4 | 0,506 | 16 |
| 2008–2014 | 0,214 | 4 | 0,252 | 20 |
| 2015–2021 | 0,154 | 4 | 0,365 | 15 |

### Niveau von Renten und Einnahmen (Mittelwert der Länderjahre, % BIP)

| Gruppe | Renten (WDI) | Ressourceneinnahmen (GRD) |
|---|---|---|
| Sahel | 12,30 | 2,62 |
| übriges SSA | 16,19 | 7,70 |

### Geflaggte Länderjahre (Capture Ratio > 1,5)

Nicht gelöscht, sondern gekennzeichnet. Ursachen sind zeitliche Verschiebungen zwischen Rentenentstehung und Einnahmeverbuchung sowie Einnahmen, die nicht als Rente im Sinne der WDI-Definition erfasst werden (etwa Dividenden aus staatlichen Beteiligungen).

| Land | ISO3 | betroffene Jahre | Median der Quote |
|---|---|---|---|
| Botswana | BWA | 14 | 7,38 |
| Namibia | NAM | 2 | 1,72 |
| South Sudan | SSD | 1 | 5,36 |
| Sao Tome and Principe | STP | 2 | 10,15 |

Davon im Sahel: **keines**.

### Datenabdeckung der Sahel-Kernländer

| ISO3 | Jahre mit Renten und Ressourceneinnahmen |
|---|---|
| MLI | 4 |
| BFA | 21 |
| NER | 22 |
| TCD | 18 |
| MRT | 18 |

### Zusammensetzung der Vergleichsgruppe

- Länder der Region insgesamt: **48**; davon mit mindestens einem GRD-Wert: **28**
- **20 Länder ohne jeden GRD-Wert** und damit nicht in der Analyse: BDI, BEN, CAF, COM, CPV, ERI, ETH, GMB, GNB, KEN, LSO, MOZ, MUS, MWI, RWA, SOM, SWZ, SYC, TZA, ZAF
- Länderjahre ohne GRD-Wert weisen im Mittel **8,97 % BIP** Renten auf, solche mit GRD-Wert **14,28 % BIP** — die Lücken liegen also systematisch bei den rentenärmeren Ländern, wie es der GRD User Guide beschreibt.
- Vergleichsgruppe der Analyse: **21 Länder**, davon **6 Ölstaaten** (NGA, AGO, COG, GAB, GNQ, SSD), die 29 % der Länder und 33 % der Länderjahre stellen.

### Abschöpfung nach Rohstofftyp statt nach Region

Die Ölstaaten prägen den Gruppenunterschied. Ihre Abschöpfungsquote liegt deutlich über der aller übrigen Länder, und der Sahel fördert überwiegend Gold und Uran.

| Gruppe | n Länder | n Länderjahre | Median | 1. Quartil | 3. Quartil |
|---|---|---|---|---|---|
| Sahel (Kernländer) | 5 | 83 | 0,075 | 0,036 | 0,285 |
| übriges SSA: Ölstaaten | 6 | 110 | 0,615 | 0,447 | 0,742 |
| übriges SSA: ohne Ölstaaten | 15 | 224 | 0,131 | 0,043 | 0,413 |

Auf Ebene der Länder-Periodenmittel (Einheit der Tests):

| Vergleich | Sahel | Vergleichsgruppe |
|---|---|---|
| gegen das gesamte übrige SSA | 0,116 (n = 4 Länder) | 0,365 (n = 20) |
| gegen das übrige SSA ohne Ölstaaten | 0,116 (n = 4) | 0,145 (n = 14) |

> **Einordnung:** Der Abstand zwischen Sahel und übrigem Subsahara-Afrika geht weitgehend auf die Ölstaaten zurück. Ohne sie liegen die Mediane nahe beieinander. Innerhalb des Sahel ist die Spannweite größer als der Gruppenunterschied: Tschad und Mauretanien (beide mit Erdölförderung) erreichen 0,26 bzw. 0,39, Burkina Faso (Gold) 0,02 und Niger (Uran) 0,04. Die Signifikanztests dazu stehen in Tab. 2 und Tab. 3 (Philip).

Quelle: World Bank WDI, UNU-WIDER GRD 2025, UNDP HDR; eigene Berechnung.

## Philip

_Erzeugt von `src/04_gruppenvergleich.py`, `src/05_zusammenhang_hdi.py` und
`src/06_robustheit.py` aus `data/processed/panel.csv` (Stand 13:20)._

### Gruppenvergleich je Periode (Tab. 2, Abb. 4)

Einheit: **Länder-Periodenmittel** der Capture Ratio, nur Länder mit ≥ 3
gültigen Jahren je Periode. Test: Mann-Whitney-U, zweiseitig.
Effektgröße: Cliff's δ (negativ = Sahel niedriger).

| Periode | n Sahel | Median Sahel | IQR Sahel | n übr. SSA | Median übr. SSA | IQR übr. SSA | U | p | Cliff's δ |
|---|---|---|---|---|---|---|---|---|---|
| 2000–2007 | 4 | 0,10 | 0,03–0,28 | 18 | 0,51 | 0,11–0,71 | 23,0 | 0,300 | −0,36 (mittel) |
| 2008–2014 | 4 | 0,21 | 0,04–0,39 | 22 | 0,25 | 0,10–0,74 | 27,0 | 0,252 | −0,39 (mittel) |
| 2015–2021 | 4 | 0,15 | 0,06–0,31 | 17 | 0,27 | 0,11–0,44 | 26,0 | 0,517 | −0,24 (klein) |

- **Kernbefund:** Cliff's δ ist in allen drei Perioden negativ, kein p-Wert
  unterschreitet 0,05. Formulierung im Text: durchgängig niedrigere
  Abschöpfung im Sahel, statistisch nicht abgesichert.
- **Mali ist in keiner Periode vertreten** (nur 4 Länderjahre mit Renten und
  Ressourceneinnahmen, davon max. 2 je Periode — Schwelle ≥ 3 verfehlt).
  Die Sahel-Gruppe besteht in allen Tests aus BFA, NER, TCD, MRT (n = 4).
  In 18 Länderjahren hat Mali Renten ≥ 1 % BIP, aber keinen GRD-Wert.
- 19 Länderjahre mit Capture Ratio > 1,5 sind geflaggt, **keines im Sahel**.

### Zusammenhang mit Entwicklung (Tab. 2b, Abb. 5)

Spearman-Rangkorrelation auf Länder-Periodenmitteln:

| Ziel | Ebene | n | ρ | p |
|---|---|---|---|---|
| HDI | alle Perioden | 68 | 0,515 | < 0,001 |
| HDI | 2000–2007 | 21 | 0,577 | 0,006 |
| HDI | 2008–2014 | 26 | 0,456 | 0,019 |
| HDI | 2015–2021 | 21 | 0,679 | < 0,001 |
| Stromzugang | alle Perioden | 69 | 0,429 | < 0,001 |
| Stromzugang | 2000–2007 | 22 | 0,456 | 0,033 |
| Stromzugang | 2008–2014 | 26 | 0,355 | 0,076 |
| Stromzugang | 2015–2021 | 21 | 0,551 | 0,010 |

- Two-way-FE-OLS `hdi ~ capture_ratio + log(BIP p. c.) + Land-FE + Jahr-FE`,
  Cluster-SE nach Land: Koeffizient **0,0007** (SE 0,0005, p = 0,177,
  95-%-KI [−0,0003; 0,0017]), n = 442 Länderjahre aus 28 Ländern.
- **Wichtig für die Interpretation:** Zwischen den Ländern besteht ein
  mittlerer positiver Zusammenhang (ρ ≈ 0,43–0,68), innerhalb der Länder
  über die Zeit praktisch keiner (FE-Koeffizient nahe null, nicht
  signifikant). Der Querschnittszusammenhang spiegelt also stabile
  Länderunterschiede, nicht eine Entwicklung, die einer veränderten
  Abschöpfung folgt. Ausschließlich als Assoziation formulieren.

### Robustheit (Tab. 3)

Cliff's δ je Periode, sechs Spezifikationen:

| Variante | 2000–2007 | 2008–2014 | 2015–2021 |
|---|---|---|---|
| Hauptspezifikation | −0,36 | −0,39 | −0,24 |
| (a) ohne Ölstaaten | −0,39 | −0,38 | −0,17 |
| (b) Sahel erweitert (+ SDN, SEN) | −0,21 | −0,32 | −0,24 |
| (c) 5-Jahres-Mittel | −0,34 | −0,36 | −0,22 |
| (d) ohne geflaggte Länderjahre | −0,28 | −0,33 | −0,24 |
| (e) ≥ 5 gültige Jahre je Periode | −0,33 | −0,61 | −0,24 |

- **Alle 18 Zellen negativ** — vollständige Vorzeichenstabilität. Kein
  p-Wert unter 0,05 in irgendeiner Variante (kleinster Wert: 0,118 in
  Variante e, Periode 2008–2014).
- In den Varianten (a) und (e) sinkt n Sahel auf 3; Variante (a) entfernt
  mit den Ölstaaten auch Tschad aus der Sahel-Gruppe.
- Die Robustheitsprüfung stützt die **Richtung** des deskriptiven Musters,
  nicht dessen statistische Signifikanz.

Quelle: World Bank WDI, UNU-WIDER GRD 2025, UNDP HDI; eigene Berechnung.