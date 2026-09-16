# Anhang A — Code und Reproduktion

Der vollständige Quellcode liegt im Repositorium des Projekts. Sämtliche Zahlen, Tabellen und Abbildungen der Arbeit werden von den unten aufgeführten Skripten erzeugt; keine davon wurde von Hand eingetragen oder nachbearbeitet.

## A.1 Reproduktion

Voraussetzung sind Python 3.10 oder neuer und die in `requirements.txt` verzeichneten Bibliotheken (`pandas`, `numpy`, `matplotlib`, `scipy`, `statsmodels`, `openpyxl`, `pyreadstat`). Die Rohdaten sind wie in Anhang B beschrieben in `data/raw/` abzulegen; das Government Revenue Dataset ist aus lizenzrechtlichen Gründen nicht Teil des Repositoriums und muss einmalig selbst bezogen werden.

```bash
pip install -r requirements.txt

python src/01_laden.py           # erzeugt data/processed/panel.csv
python src/02_abdeckung.py       # Abdeckung je Land, Entscheidung GRD oder Plan B
python src/03_capture_ratio.py   # deskriptive Kennzahlen, Tab. 1
python src/04_gruppenvergleich.py
python src/05_zusammenhang_hdi.py
python src/06_robustheit.py
python src/fig1_renten_2021.py
python src/fig2_zeitreihen.py
python src/fig3_streudiagramm.py
```

Die Skripte sind einzeln lauffähig und lesen ausschließlich `data/processed/panel.csv`; einzige Ausnahme ist `01_laden.py`, das dieses Panel aus den Rohdaten erzeugt. Alle Schritte sind deterministisch, es kommen keine Zufallszahlen zum Einsatz.

## A.2 Übersicht der Skripte

| Skript | Aufgabe | Erzeugt |
|---|---|---|
| `01_laden.py` | Liest die drei Indikatoren der Weltbank, die Ländermetadaten, das Government Revenue Dataset und den Index der menschlichen Entwicklung; führt sie über ISO-3-Code und Jahr zusammen, grenzt auf die Region Subsahara-Afrika und den Zeitraum 2000–2021 ein und berechnet Abschöpfungsquote, Dreijahresmittel, Gruppenkennzeichen und Periodenzuordnung. | `data/processed/panel.csv` |
| `02_abdeckung.py` | Zählt je Land die Jahre mit Renten, Ressourceneinnahmen und Index der menschlichen Entwicklung und prüft, ob mindestens drei Sahel-Kernländer über mindestens zehn gemeinsame Jahre verfügen. | `tables/abdeckung.md` |
| `03_capture_ratio.py` | Deskriptive Kennzahlen je Land, Gruppe und Periode; Zusammensetzung der Vergleichsgruppe; Abschöpfung nach Rohstoffart. | `results/zahlen.md` (Abschnitt Mark), `tables/tab1_datenquellen.md` |
| `04_gruppenvergleich.py` | Gruppenvergleich auf Länder-Periodenmitteln mit Mann-Whitney-U-Test und Cliffs Delta. | `tables/tab2_gruppenvergleich.md`, `figures/fig4_boxplot.png` |
| `05_zusammenhang_hdi.py` | Spearman-Rangkorrelationen zwischen Abschöpfungsquote und Entwicklungsindikatoren, ergänzt um eine Fixed-Effects-Schätzung. | `tables/tab2b_zusammenhang.md`, `figures/fig5_hdi.png` |
| `06_robustheit.py` | Robustheitsprüfungen ohne Ölstaaten, mit und ohne die erweiterten Sahel-Länder sowie mit Fünfjahresmittel; zusätzlich der Vergleich nach Rohstoffart. | `tables/tab3_robustheit.md` |
| `fig1_renten_2021.py` | Rohstoffrenten 2021 je Land der Region. | `figures/fig1_renten_2021.png` |
| `fig2_zeitreihen.py` | Verlauf der Abschöpfungsquote im Sahel gegen Median und Interquartilsband der Vergleichsgruppe. | `figures/fig2_zeitreihen.png` |
| `fig3_streudiagramm.py` | Renten gegen Ressourceneinnahmen mit 45-Grad-Linie auf Länder-Periodenmitteln. | `figures/fig3_streudiagramm.png` |
| `00_dummy_panel.py` | Erzeugt ein Panel mit erfundenen Werten, mit dem die Auswertungsskripte entwickelt werden konnten, solange die Rohdaten noch nicht vorlagen. Für die Ergebnisse der Arbeit nicht verwendet. | `data/processed/panel_dummy.csv` |

## A.3 Aufbau des Panels

`data/processed/panel.csv` ist die einzige Schnittstelle zwischen Datenaufbereitung und Auswertung. Jede Zeile entspricht einem Länderjahr.

| Spalte | Inhalt |
|---|---|
| `iso3`, `country`, `year` | Land und Jahr |
| `sahel`, `sahel_ext`, `oil_state` | Gruppenkennzeichen |
| `rents_pct_gdp` | Rohstoffrenten, % des Bruttoinlandsprodukts |
| `res_rev_pct_gdp`, `res_tax_pct_gdp` | staatliche Ressourceneinnahmen und Ressourcensteuern, % des Bruttoinlandsprodukts |
| `gdppc_const`, `elec_access_pct`, `hdi` | Entwicklungsindikatoren |
| `capture_ratio` | Abschöpfungsquote; leer, wenn die Renten unter einem Prozent des Bruttoinlandsprodukts liegen |
| `capture_ratio_3y` | zentriertes Dreijahresmittel, je Land getrennt gebildet |
| `flag_ratio_high` | Kennzeichen für Werte über 1,5 |
| `period` | 2000–2007, 2008–2014 oder 2015–2021 |

## A.4 Grundsätze der Umsetzung

Fehlende Werte bleiben fehlend: Es wird weder interpoliert noch fortgeschrieben, und Datenlücken werden auch in den Abbildungen nicht überbrückt. Auffällige Werte werden gekennzeichnet, nicht entfernt. Die Zusammenführung erfolgt ausschließlich über ISO-3-Codes, nicht über Ländernamen. Jede im Text verwendete Zahl ist in `results/zahlen.md` mit dem erzeugenden Skript vermerkt; Zahlen, die dort fehlen, dürfen nach der Projektvereinbarung nicht in den Text übernommen werden.
