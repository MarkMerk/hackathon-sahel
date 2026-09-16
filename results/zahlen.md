# Zahlen für den Text

> Verbindliche Quelle für alle Zahlenangaben in der Abhandlung. Keine Zahl in einen Textentwurf, die nicht hier steht. Erzeugt am 16.09.2026.

## Mark

_Erzeugt von `src/03_capture_ratio.py` aus `data/processed/panel.csv`._

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

Quelle: World Bank WDI, UNU-WIDER GRD 2025, UNDP HDR; eigene Berechnung.
