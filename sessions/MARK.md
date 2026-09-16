# Sitzungsleitfaden — Mark (Daten, Pipeline, Capture Ratio, Methodik, Integration)

> Für Claude Code in Marks Terminal. Mark arbeitet routiniert mit **Subagenten** — nutze sie aktiv für parallele, klar abgegrenzte Aufgaben. Mark hat zusätzlich **Claude Science** (lokal) für Literaturprüfung und das finale Review.

## Rolle
Datenverantwortung und Integration: Downloads, `panel.csv` nach Schema, Abdeckungsentscheidung GRD/EITI, Capture Ratio, Abb. 1–3, Tab. 1, Methodik, Ergebnisse 5.1, Abstract, Fazit, Anhang A/B/D/E, finaler PDF-Export und Upload.

## Subagenten (`.claude/agents/`)
| Agent | Einsatz | Modell |
|---|---|---|
| `daten-pruefer` | Rohdateien inspizieren, Spalten/ISO-Codes/Abdeckung prüfen, keine Änderungen | sonnet |
| `abbildungen` | genau eine Abbildung aus `panel.csv` erzeugen, inkl. Caption | sonnet |
| `statistik-pruefer` | Philips Tests/Robustheit adversarial prüfen (Pseudoreplikation, n, Interpretation) | opus |
| `strawberry-reviewer` | Textentwurf gegen `STRAWBERRY.md` prüfen, nur Befund, keine Umschreibung | opus |
| `quellen-pruefer` | `text/quellen.bib` auf Vollständigkeit/APA/DOI-Plausibilität prüfen | sonnet |
**Parallelisierungsregeln:** Jeder Subagent bekommt eine Zieldatei und liefert eine Zusammenfassung ≤ 10 Zeilen zurück. Nie zwei Agenten auf dieselbe Datei. Ergebnisse der Agenten vor dem Commit selbst gegenlesen. Jeden Agenteneinsatz in `logs/LOG_mark.md` protokollieren (Name des Agenten, Auftrag, Ergebnis, ggf. Fehler).

## Ablauf

### Schritt 1 — Repo steht (11:15–11:25)
- Prüfe `git status`, lies `docs/Forschungsdesign.md`. Log-Zeile anlegen.

### Schritt 2 — Downloads (11:25–11:45, Mark im Browser)
- Dateien laut `DATA_DOWNLOAD.md` nach `data/raw/`. Währenddessen nichts analysieren.
- Danach **parallel drei `daten-pruefer`-Agenten**: (a) WDI-Dateien, (b) GRD-Datei, (c) HDI-Datei. Auftrag je: Spaltennamen, Ländercodes (ISO3 vorhanden? Mapping nötig?), Jahresbereich, Werte für MLI/BFA/NER/TCD/MRT/SDN/SEN 2000–2021 nicht-leer zählen. Rückgabe als kurze Tabelle.

### Schritt 3 — Panel und Entscheidung (11:45–12:15)
Prompt:
```
Schreibe src/01_laden.py: lädt WDI (NY.GDP.TOTL.RT.ZS, NY.GDP.PCAP.KD, EG.ELC.ACCS.ZS; Regionszuordnung aus der WDI-Metadatendatei), GRD (Total Resource Revenue, Resource taxes; Länder auf ISO3 mappen), UNDP HDI; filtert WB-Region Subsahara-Afrika und 2000–2021; erzeugt data/processed/panel.csv exakt nach Schema in docs/Forschungsdesign.md §4 (inkl. sahel, sahel_ext, oil_state, capture_ratio, capture_ratio_3y, flag_ratio_high, period). Ohne Interpolation.
Schreibe src/02_abdeckung.py: tables/abdeckung.md mit nicht-leeren Jahren je Land für rents, res_rev, hdi; Sahel-Länder oben.
Führe beide aus und nenne: Wie viele der fünf Sahel-Kernländer haben ≥ 10 Jahre mit rents UND res_rev?
```
- **≥ 3 Länder → GRD.** Sonst Plan B: EITI laden, `res_rev_pct_gdp` aus EITI (Staatseinnahmen ÷ BIP) füllen, im Log und in `text/anhang/B_datenquellen.md` begründen.
- **Sofort committen und pushen** (`mark: panel.csv und Abdeckung`), Philip Bescheid geben — er wechselt von Dummy auf echte Daten.

### Schritt 4 — Capture Ratio und Abbildungen (12:15–13:30)
- `src/03_capture_ratio.py`: deskriptive Kennzahlen je Land und Gruppe → `results/zahlen.md` (Abschnitt „Mark“), `tables/tab1_datenquellen.md`.
- **Parallel drei `abbildungen`-Agenten:** Abb. 1 (Renten 2021 je SSA-Land, Sahel markiert), Abb. 2 (Zeitreihen Capture Ratio 3y Sahel vs. SSA-Median/IQR), Abb. 3 (Scatter Renten vs. Einnahmen, 45°-Linie, Länder-Periodenmittel, Sahel beschriftet). Jeder schreibt eine Datei in `src/`, eine PNG und seinen Caption-Eintrag.
- Mark prüft alle drei Grafiken visuell, dann Commit.

### Schritt 5 — Texte (13:30–15:00)
- Entwürfe `text/abschnitte/04_methodik.md` (5.500 Zeichen, BURNS) und `05_1_deskriptiv.md` (Anteil an 7.500, ELVIRA) mit Prompt P3 aus `PROMPTS.md`.
- Nach jedem Entwurf `strawberry-reviewer` im Hintergrund starten, währenddessen weiterarbeiten.
- Wenn Philip pusht: `statistik-pruefer` auf `src/04_*`–`06_*` und `tables/tab2*`, `tab3*`. Befunde an Philip weitergeben, nicht selbst ändern.
- **Claude Science (parallel, außerhalb von Claude Code):** Leons `text/quellen.bib` verifizieren lassen — existiert jede Quelle, stimmen Autor/Jahr/DOI, stützt sie die Aussage? Ergebnis in `logs/LOG_mark.md`, Korrekturen an Leon.

### Schritt 6 — Abschluss (15:00–16:25)
- `00_abstract.md` (1.200, The-5-S) und `08_fazit.md` (2.000, RIB) — erst wenn Ergebnisse und Diskussion stehen.
- `strawberry-reviewer` über den gesamten Google-Doc-Export (Datei → Herunterladen → Nur Text → `export_abhandlung.txt`, nicht committen).
- **Claude Science Reviewer** über das exportierte PDF: Zitate und Zahlen gegen `results/zahlen.md` prüfen.
- Anhang: `A_code.md` (Skriptübersicht + Link/Repo-Stand), `B_datenquellen.md` (URLs, Abrufdatum, Versionen), `D_tabellen.md`, `E_prompts.md` (aus allen drei Logs die wichtigsten Prompts).
- `python count_chars.py export_abhandlung.txt 37500`.

### Schritt 7 — Export und Upload (16:25–16:40)
- Beide PDFs aus Google Docs exportieren, Schrift/Abstand/Ränder im PDF prüfen, in Stud.IP-Gruppenordner hochladen, Bestätigung als Screenshot.
