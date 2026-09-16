# Forschungsdesign — Wer schöpft die Rohstoffrenten ab?

> Verbindliches Design der Arbeit (Team Mark, Leon, Philip; AI Hackathon, AI Summercamp 2026, JLU, 16.09.2026). Aufgabenstellung: `docs/Arbeitsauftrag.pdf`. Checkliste für den Text: `STRAWBERRY.md`.

## 1. Datenlage (geprüft am 16.09.2026)
- **World Bank WDI, `NY.GDP.TOTL.RT.ZS`** (Rohstoffrenten, % BIP; Stand 13.07.2026): Für NER, MLI, BFA, TCD, MRT, SDN liegt der letzte Wert bei **2021** (2021: TCD 21,3; BFA 20,1; MLI 18,4; SDN 12,8; MRT 11,5; NER 6,4). 2022–2024 leer.
- **ICTD/UNU-WIDER Government Revenue Dataset (GRD)**: Version 2023 deckt **1980–2021/22** ab. Relevante Variablen: *Total Resource Revenue*, *Resource taxes* sowie Ressourcenkomponenten der Einkommen-/Unternehmens-, indirekten und nichtsteuerlichen Einnahmen. Laut User Guide fehlen Werte meist, wenn Ressourceneinnahmen unter ca. 1 % des BIP liegen.
- **Konsequenz:** Analysefenster **2000–2021**. Entwicklungen nach 2021/2023 nur qualitativ und über EITI-Daten.
- **Zugriff:** APIs von World Bank und UNU-WIDER sind aus den Sandbox-Umgebungen blockiert → manueller Download (`DATA_DOWNLOAD.md`).

## 2. Forschungsfrage
**Wer schöpft die Rohstoffrenten ab? Der Anteil staatlicher Ressourceneinnahmen an den Rohstoffrenten in den Sahel-Staaten im Vergleich zu Subsahara-Afrika (2000–2021)**

Teilfragen:
1. Wie hoch ist die staatliche Abschöpfungsquote (*Capture Ratio*) im Sahel und im übrigen Subsahara-Afrika, und wie entwickelt sie sich?
2. Unterscheidet sich die Quote systematisch zwischen Sahel und Vergleichsgruppe — auch bei ähnlich hohen Renten?
3. Gehen höhere Abschöpfungsquoten mit höherer menschlicher Entwicklung (HDI, Stromzugang) einher?
4. *(nur Diskussion)* Was deuten die Politikwechsel nach 2021/2023 an — Bergbaukodex Mali 2023, Verstaatlichung von SOMAÏR in Niger 2025?

## 3. Operationalisierung
- **Capture Ratio** = Total Resource Revenue (% BIP, GRD) ÷ Rohstoffrenten (% BIP, WDI). Einheitenlos: Anteil der erzeugten Rente, der im Staatshaushalt ankommt. Der Rest verbleibt bei Unternehmen, (ausländischen) Betreibern oder geht verloren.
- **Sahel-Gruppe:** MLI, BFA, NER, TCD, MRT. Sensitivität: zusätzlich SDN, SEN.
- **Vergleichsgruppe:** übrige Länder der World-Bank-Region Subsahara-Afrika (SSF).
- **Filter/Flags:** nur Länderjahre mit Renten ≥ 1 % BIP (kleiner Nenner); Werte > 1,5 flaggen, nicht löschen (Timing, Preisschocks).
- **Glättung:** zentriertes 3-Jahres-Mittel, weil Renten weltmarktpreisgetrieben sind und Einnahmen zeitverzögert folgen.
- **Perioden:** 2000–2007, 2008–2014, 2015–2021.

## 4. Datenschema `data/processed/panel.csv` (verbindlich für alle Skripte)
| Spalte | Typ | Inhalt |
|---|---|---|
| `iso3` | str | ISO-3-Ländercode |
| `country` | str | Ländername (WDI) |
| `year` | int | 2000–2021 |
| `sahel` | bool | True für MLI, BFA, NER, TCD, MRT |
| `sahel_ext` | bool | True zusätzlich für SDN, SEN |
| `oil_state` | bool | True für NGA, AGO, GNQ, COG, GAB, SSD, TCD |
| `rents_pct_gdp` | float | WDI NY.GDP.TOTL.RT.ZS |
| `res_rev_pct_gdp` | float | GRD Total Resource Revenue |
| `res_tax_pct_gdp` | float | GRD Resource taxes |
| `gdppc_const` | float | WDI NY.GDP.PCAP.KD |
| `elec_access_pct` | float | WDI EG.ELC.ACCS.ZS |
| `hdi` | float | UNDP HDI |
| `capture_ratio` | float | res_rev / rents, NaN wenn rents < 1 |
| `capture_ratio_3y` | float | zentriertes 3-Jahres-Mittel je Land |
| `flag_ratio_high` | bool | capture_ratio > 1,5 |
| `period` | str | "2000–2007" / "2008–2014" / "2015–2021" |

## 5. Methodik
**Fachlicher Kontext:** Data Science — deskriptiv-vergleichende Panelanalyse offener Sekundärdaten.
1. Aufbereitung und Merge (ISO3 × Jahr), Abdeckungsanalyse → Anhang.
2. Deskriptiv: Zeitreihen der Capture Ratio je Sahel-Land gegen Median und Interquartilsband der übrigen SSA.
3. Streudiagramm Renten vs. Ressourceneinnahmen (% BIP) mit 45°-Linie; Abstand zur Linie = nicht abgeschöpfter Anteil; Sahel hervorgehoben.
4. Gruppenvergleich je Periode: Median, IQR, Mann-Whitney-U auf Länder-Periodenmitteln (keine Pseudoreplikation über Länderjahre).
5. Zusammenhang mit Entwicklung: Spearman-Korrelation Capture Ratio ↔ HDI bzw. Stromzugang; optional Two-way-Fixed-Effects-OLS mit länderweise geclusterten Standardfehlern — ausdrücklich als Assoziation.
6. Robustheit: ohne Ölstaaten, mit/ohne SDN und SEN, 5- statt 3-Jahres-Mittel.
7. **Plan B**, falls weniger als drei Sahel-Länder mindestens zehn Jahre mit GRD-Ressourceneinnahmen *und* Renten haben: EITI-Staatseinnahmen aus dem Rohstoffsektor als Zähler (kürzeres Fenster, dafür aktueller).

## 6. Abbildungen und Tabellen
| Nr. | Inhalt | Verantwortlich |
|---|---|---|
| Abb. 1 | Rohstoffrenten (% BIP) 2021 je SSA-Land, Sahel markiert | Mark |
| Abb. 2 | Zeitreihen Capture Ratio Sahel vs. SSA-Median/IQR | Mark |
| Abb. 3 | Streudiagramm Renten vs. Einnahmen mit 45°-Linie | Mark |
| Abb. 4 | Boxplots Capture Ratio nach Periode und Gruppe | Philip |
| Abb. 5 | Capture Ratio vs. HDI (Länder-Periodenmittel) | Philip |
| Tab. 1 | Datenquellen und Indikatoren | Mark |
| Tab. 2 | Gruppenvergleich und Tests | Philip |
| Tab. 3 | Robustheitsprüfungen | Philip |

## 7. Theoretischer Rahmen (Leon)
Rentierstaat (Beblawi & Luciani), Resource Curse (Sachs & Warner; van der Ploeg), Institutionen-Ansatz (Mehlum, Moene & Torvik), Literatur zu *government take* und fiskalischen Regimen im Bergbau (IMF), Ressourcensouveränität als Deutungsrahmen für die Politikwechsel. Alle Angaben erst nach DOI-Prüfung zitieren.

## 8. Aufbau der Abhandlung und Zeichenbudget (≤ 37.500)
| Abschnitt | Zeichen | STRaWBERRY | Entwurf |
|---|---|---|---|
| Titel | — | SPICE | Mark |
| Abstract | 1.200 | The-5-S | Mark |
| 1 Einleitung | 4.000 | WHWN | Leon |
| 2 Theoretischer Rahmen | 3.500 | — | Leon |
| 3 Forschungsstand | 3.800 | RICK | Leon |
| 4 Daten und Methodik | 5.500 | BURNS | Mark |
| 5 Ergebnisse | 7.500 | ELVIRA | Mark (5.1) / Philip (5.2–5.4) |
| 6 Diskussion inkl. Fallbeispiele Niger/Mali | 6.000 | REFLOW | Leon |
| 7 Limitationen | 2.300 | REFLOW (L) | Philip |
| 8 Fazit | 2.000 | RIB | Mark |
| **Summe** | **35.800** | | Reserve 1.700 |
| Literaturverzeichnis (APA 7) | zählt nicht | YEAR | Leon |
| Anhang A Code · B Datenquellen/Abfragen · C Suchprotokoll · D Tabellen · E Prompt-Protokoll | zählt nicht | — | alle |

**Dokumentation & Reflexion (≤ 12.500):** Einordnung in den Studienstand (B.Sc./M.Sc. Data Science, JLU), Arbeitsprozess chronologisch, konkrete KI-Nutzung inkl. Fehler und Prüfschritte, Reflexion. Entwurf: Philip, Beiträge aller aus `logs/`.
