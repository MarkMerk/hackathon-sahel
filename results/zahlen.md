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
| übriges Subsahara-Afrika | 372 | 23 | 0,299 | 0,079 | 0,644 |

> Hinweis: Tests laufen auf Länder-Periodenmitteln (`src/04_gruppenvergleich.py`), nicht auf diesen gepoolten Werten. Die Tabelle dient nur der Beschreibung.

### Entwicklung über die Perioden (Median der Länder-Periodenmittel)

| Periode | Sahel: Median | n Länder | übriges SSA: Median | n Länder |
|---|---|---|---|---|
| 2000–2007 | 0,097 | 4 | 0,506 | 18 |
| 2008–2014 | 0,214 | 4 | 0,252 | 22 |
| 2015–2021 | 0,154 | 4 | 0,265 | 17 |

### Niveau von Renten und Einnahmen (Mittelwert der Länderjahre, % BIP)

| Gruppe | Renten (WDI) | Ressourceneinnahmen (GRD) |
|---|---|---|
| Sahel | 12,30 | 2,62 |
| übriges SSA | 15,19 | 7,22 |

### Geflaggte Länderjahre (Capture Ratio > 1,5)

Nicht gelöscht, sondern gekennzeichnet. Ursachen sind zeitliche Verschiebungen zwischen Rentenentstehung und Einnahmeverbuchung sowie Einnahmen, die nicht als Rente im Sinne der WDI-Definition erfasst werden (etwa Dividenden aus staatlichen Beteiligungen).

| Land | ISO3 | betroffene Jahre | Median der Quote |
|---|---|---|---|
| Botswana | BWA | 14 | 7,38 |
| Namibia | NAM | 2 | 1,72 |
| South Sudan | SSD | 1 | 5,36 |
| Sao Tome and Principe | STP | 2 | 10,15 |

Davon im Sahel: **keines**.

### Rohstoffrenten 2021 je Sahel-Kernland (Abb. 1)

Grundlage: 46 Länder der Region mit vorhandenem Wert für 2021.

| Land | ISO3 | Renten (% BIP) | Rang in der Region |
|---|---|---|---|
| Mali | MLI | 18,4 | 10 von 46 |
| Burkina Faso | BFA | 20,1 | 8 von 46 |
| Niger | NER | 6,4 | 26 von 46 |
| Chad | TCD | 21,3 | 7 von 46 |
| Mauritania | MRT | 11,4 | 16 von 46 |

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
- Vergleichsgruppe der Analyse: **23 Länder**, davon **6 Ölstaaten** (NGA, AGO, COG, GAB, GNQ, SSD), die 26 % der Länder und 30 % der Länderjahre stellen.

### Abschöpfung nach Rohstofftyp statt nach Region

Die Ölstaaten prägen den Gruppenunterschied. Ihre Abschöpfungsquote liegt deutlich über der aller übrigen Länder, und der Sahel fördert überwiegend Gold und Uran.

| Gruppe | n Länder | n Länderjahre | Median | 1. Quartil | 3. Quartil |
|---|---|---|---|---|---|
| Sahel (Kernländer) | 5 | 83 | 0,075 | 0,036 | 0,285 |
| übriges SSA: Ölstaaten | 6 | 110 | 0,615 | 0,447 | 0,742 |
| übriges SSA: ohne Ölstaaten | 17 | 262 | 0,145 | 0,049 | 0,424 |

Auf Ebene der Länder-Periodenmittel (Einheit der Tests):

| Vergleich | Sahel | Vergleichsgruppe |
|---|---|---|
| gegen das gesamte übrige SSA | 0,116 (n = 4 Länder) | 0,265 (n = 22) |
| gegen das übrige SSA ohne Ölstaaten | 0,116 (n = 4) | 0,145 (n = 16) |

> **Einordnung:** Der Abstand zwischen Sahel und übrigem Subsahara-Afrika geht weitgehend auf die Ölstaaten zurück. Ohne sie liegen die Mediane nahe beieinander. Innerhalb des Sahel ist die Spannweite größer als der Gruppenunterschied: Tschad und Mauretanien (beide mit Erdölförderung) erreichen 0,26 bzw. 0,39, Burkina Faso (Gold) 0,02 und Niger (Uran) 0,04. Die Signifikanztests dazu stehen in Tab. 2 und Tab. 3 (Philip).

Quelle: World Bank WDI, UNU-WIDER GRD 2025, UNDP HDR; eigene Berechnung.

## Philip

_Erzeugt von `src/04_gruppenvergleich.py`, `src/05_zusammenhang_hdi.py` und
`src/06_robustheit.py` aus `data/processed/panel.csv` (Stand 14:45, nach
Befunden des Subagenten `statistik-pruefer`)._

> **Änderung 14:45:** Die Hauptspezifikation verwendet jetzt die im
> Forschungsdesign §3 vorgeschriebene zentrierte 3-Jahres-Glättung
> (`capture_ratio_3y`). Bis 14:20 rechneten die Skripte auf ungeglätteten
> Jahreswerten — ein Abweichen vom Design, das der Prüfer gefunden hat. Die
> ungeglättete Variante läuft weiter als Robustheitsvariante (c0). Der Befund
> wird durch die Korrektur leicht **stärker**.

### Gruppenvergleich je Periode (Tab. 2, Abb. 4)

Einheit: **Länder-Periodenmittel** der Capture Ratio, nur Länder mit ≥ 3
gültigen Jahren je Periode. Test: Mann-Whitney-U, zweiseitig.
Effektgröße: Cliff's δ (negativ = Sahel niedriger).

| Periode | n Sahel | Median Sahel | IQR Sahel | n übr. SSA | Median übr. SSA | IQR übr. SSA | U | p | Cliff's δ |
|---|---|---|---|---|---|---|---|---|---|
| 2000–2007 | 4 | 0,10 | 0,03–0,28 | 18 | 0,51 | 0,10–0,71 | 21,0 | 0,227 | −0,42 |
| 2008–2014 | 4 | 0,21 | 0,04–0,38 | 22 | 0,35 | 0,09–0,76 | 25,0 | 0,197 | −0,43 |
| 2015–2021 | 4 | 0,16 | 0,06–0,32 | 17 | 0,26 | 0,11–0,45 | 25,0 | 0,462 | −0,26 |

Keine Einordnung von Cliff's δ nach Romano et al. (2006): Bei vier Ländern je
Periode umspannt das Bootstrap-Konfidenzintervall praktisch den gesamten
Wertebereich, ein Label wie „mittel" wäre Scheingenauigkeit. Der IQR beruht
bei n = 4 auf Interpolation und ist nur illustrativ.

- **Kernbefund:** Cliff's δ ist in allen drei Perioden negativ, kein p-Wert
  unterschreitet 0,05. Formulierung im Text: durchgängig niedrigere
  Abschöpfung im Sahel, statistisch nicht abgesichert.
- **Wichtige Einschränkung (siehe Tab. 3):** Dieser Abstand geht weitgehend
  auf die Ölstaaten in der Vergleichsgruppe zurück. Er darf nicht als
  Regionsbefund formuliert werden.
- **Mali ist in keiner Periode vertreten** (nur 4 Länderjahre mit Renten und
  Ressourceneinnahmen, davon max. 2 je Periode — Schwelle ≥ 3 verfehlt).
  Die Sahel-Gruppe besteht in allen Tests aus BFA, NER, TCD, MRT (n = 4).
  In 18 Länderjahren hat Mali Renten ≥ 1 % BIP, aber keinen GRD-Wert.
- 19 Länderjahre mit Capture Ratio > 1,5 sind geflaggt, **keines im Sahel**.

### Zusammenhang mit Entwicklung (Tab. 2b, Abb. 5)

Spearman-Rangkorrelation auf Länder-Periodenmitteln:

| Ziel | Ebene | n | ρ | p |
|---|---|---|---|---|
| HDI | Querschnitt (ein Wert je Land) | 26 | 0,517 | 0,007 |
| HDI | 2000–2007 | 21 | 0,577 | 0,006 |
| HDI | 2008–2014 | 26 | 0,456 | 0,019 |
| HDI | 2015–2021 | 21 | 0,679 | < 0,001 |
| Stromzugang | Querschnitt (ein Wert je Land) | 26 | 0,410 | 0,038 |
| Stromzugang | 2000–2007 | 22 | 0,456 | 0,033 |
| Stromzugang | 2008–2014 | 26 | 0,355 | 0,076 |
| Stromzugang | 2015–2021 | 21 | 0,551 | 0,010 |

Die frühere Zeile „alle Perioden" (n = 68, ρ = 0,515) ist durch den
Querschnitt ersetzt: Sie zählte dasselbe Land bis zu dreimal und erzeugte
damit dieselbe Pseudoreplikation, die die Gruppentests vermeiden. Der
Querschnitt bestätigt den Befund bei korrekter Fallzahl.

- Two-way-FE-OLS `hdi ~ capture_ratio + log(BIP p. c.) + Land-FE + Jahr-FE`,
  Cluster-SE nach Land: Koeffizient **0,0007** (SE 0,0005, p = 0,177,
  95-%-KI [−0,0003; 0,0017]), n = 442 Länderjahre aus 28 Ländern.
- **Die FE-Schätzung ist nicht belastbar und nur exploratorisch zu
  berichten.** Sie darf **nicht** als „innerhalb der Länder kein
  Zusammenhang" ausgelegt werden — das war die Formulierung bis 14:45 und
  ist falsch. Drei Gründe: (1) Das Vorzeichen wechselt mit der
  Spezifikation — nur mit Länder-Fixed-Effects ergibt sich −0,0019 bei
  p = 0,041, also negativ und nominell signifikant. (2) Die scheinbare
  Präzision stammt von wenigen Extremwerten: Ohne die 19 geflaggten
  Beobachtungen (14 davon Botswana) steigt der Standardfehler von 0,0005 auf
  0,0090, das Konfidenzintervall umspannt [−0,015; +0,021]. (3) Fünf der 28
  Cluster haben weniger als fünf Beobachtungen. Korrekte Aussage: Zwischen
  den Ländern besteht ein mittlerer positiver Zusammenhang (ρ = 0,36–0,68);
  über die Zeit innerhalb der Länder lassen diese Daten keine Aussage zu.
- Das hohe R² von 0,985 stammt fast vollständig aus den Länder-Fixed-Effects;
  das inkrementelle R² der Capture Ratio beträgt etwa 0,00005. Es ist kein
  Hinweis auf Erklärungskraft der Kennzahl.

### Robustheit (Tab. 3)

Cliff's δ je Periode, Hauptspezifikation und acht Varianten:

| Variante | 2000–2007 | 2008–2014 | 2015–2021 |
|---|---|---|---|
| Hauptspezifikation (3-Jahres-Glättung) | −0,42 | −0,43 | −0,26 |
| (a1) Vergleichsgruppe ohne Ölstaaten, Sahel unverändert | −0,27 | −0,22 | −0,08 |
| (a2) ohne Ölstaaten in beiden Gruppen (ohne TCD) | −0,38 | −0,42 | −0,17 |
| (b) Sahel erweitert (+ SDN, SEN) | −0,27 | −0,37 | −0,27 |
| (c) 5- statt 3-Jahres-Glättung | −0,39 | −0,43 | −0,26 |
| (c0) ungeglättete Jahreswerte | −0,36 | −0,39 | −0,24 |
| (d) ohne geflaggte Länderjahre | −0,34 | −0,34 | −0,26 |
| (e) ≥ 5 gültige Jahre je Periode | −0,38 | −0,61 | −0,26 |
| (f) Quotient der Periodensummen | −0,47 | −0,39 | −0,29 |

- **Alle 27 Zellen negativ.** Kein p-Wert unter 0,05 in irgendeiner
  Regionsvariante (kleinster Wert 0,118 in Variante e, 2008–2014). Die
  Zellen sind **keine unabhängigen Replikationen**: Sie beruhen alle auf
  denselben vier Sahel-Ländern.
- **Kernkontrast mit/ohne Ölstaaten (Tab. 3, oberste Tabelle):** Bleibt die
  Sahel-Gruppe unverändert und werden nur die Ölstaaten aus der
  Vergleichsgruppe entfernt, fällt der Median der Vergleichsgruppe von 0,51 /
  0,35 / 0,26 auf 0,14 / 0,15 / 0,16 und Cliff's δ von −0,42 / −0,43 / −0,26
  auf −0,27 / −0,22 / −0,08. Der Regionsabstand ist also überwiegend ein
  Rohstofftyp-Effekt. In 2015–2021 ist δ = −0,08 vernachlässigbar.
- In den Varianten (a2) und (e) sinkt n Sahel auf 3; (a2) entfernt mit den
  Ölstaaten auch Tschad aus der Sahel-Gruppe.
- Variante (d) entfernt faktisch ganze Länder: Botswana verliert alle 14
  gültigen Jahre und fällt aus der Vergleichsgruppe.
- Die Robustheitsprüfung stützt die **Richtung** des deskriptiven Musters,
  nicht dessen Höhe und nicht dessen statistische Signifikanz.

### Abschöpfung nach Rohstofftyp (Tab. 3, ohne Regionsbezug)

**Post hoc:** Diese Auswertung ist im Forschungsdesign §5.6 nicht vorgesehen
und nach Sichtung der Regionsergebnisse ergänzt worden. Das ist beim
Berichten zu deklarieren. Positives δ = Länder mit Ölförderung schöpfen mehr ab.

Abgrenzung nach der Panelspalte `oil_state` (NGA, AGO, GNQ, COG, GAB, SSD, TCD):

| Periode | n Öl | Median Öl | n ohne Öl | Median ohne Öl | Cliff's δ | p |
|---|---|---|---|---|---|---|
| 2000–2007 | 6 | 0,52 | 16 | 0,12 | +0,31 | 0,294 |
| 2008–2014 | 7 | 0,74 | 19 | 0,15 | +0,74 | 0,003 |
| 2015–2021 | 6 | 0,46 | 15 | 0,14 | +0,64 | 0,023 |

**Erweiterte Abgrenzung** (zusätzlich CMR, SDN und MRT, die ebenfalls Erdöl
fördern). Diese Fassung ist sachlich korrekter — die Spalte `oil_state` wurde
für den Robustheits-Ausschluss definiert und ist als Öl-Kennzeichnung
unvollständig:

| Periode | n Öl | Median Öl | n ohne Öl | Median ohne Öl | Cliff's δ | p |
|---|---|---|---|---|---|---|
| 2000–2007 | 9 | 0,62 | 13 | 0,11 | +0,54 | 0,038 |
| 2008–2014 | 10 | 0,66 | 16 | 0,10 | +0,76 | 0,001 |
| 2015–2021 | 9 | 0,45 | 12 | 0,10 | +0,78 | 0,003 |

- **Deskriptiv deutlichster Kontrast der Arbeit** — nicht „stärkster Befund":
  Die Auswertung ist post hoc, und die drei Periodentests beruhen auf
  denselben wenigen Ländern, sind also keine drei unabhängigen Belege.
- Er hält jedoch der **Holm-Korrektur über alle 17 berichteten Tests** stand:
  erweiterte Abgrenzung p_Holm = 0,020 (2008–2014) und 0,038 (2015–2021).
  Mit der unvollständigen Abgrenzung `oil_state` wäre das nicht der Fall.
- Dasselbe Muster innerhalb des Sahel (Zahlen von Mark): TCD 0,26 und MRT 0,39
  (Erdöl) gegenüber BFA 0,02 (Gold) und NER 0,04 (Uran) — die Spannweite im
  Sahel übersteigt den Gruppenunterschied.
- Auch dies bleibt eine Assoziation. Plausible Mechanismen (Konzentration der
  Förderung, Erfassbarkeit, Vertragsregime) sind mit diesen Daten nicht
  prüfbar und gehören in die Diskussion.
- Die Klassifikation nach Rohstofftyp ist eine Vereinfachung: Die Länder
  fördern jeweils mehrere Rohstoffe in unterschiedlichem Anteil.

### Multiples Testen

Diese Arbeit berichtet 17 Signifikanztests (3 Regionstests der
Hauptspezifikation, 6 Typtests, 8 Spearman-Korrelationen). Die in den
Tabellen ausgewiesenen p-Werte sind **nicht adjustiert**. Nach
Holm-Korrektur über alle 17 bleiben sechs signifikant: die vier
Spearman-Korrelationen mit HDI beziehungsweise Stromzugang im Querschnitt
und 2015–2021 sowie die beiden Typtests 2008–2014 und 2015–2021 in
erweiterter Abgrenzung. Kein Regionstest ist betroffen, da keiner auch
unadjustiert die Schwelle erreicht.

Quelle: World Bank WDI, UNU-WIDER GRD 2025, UNDP HDI; eigene Berechnung.