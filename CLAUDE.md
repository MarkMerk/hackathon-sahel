# CLAUDE.md — hackathon-sahel

> Wird von jeder Claude-Code-Sitzung zuerst gelesen. Rangfolge bei Widerspruch: `docs/Arbeitsauftrag.pdf` > `docs/Forschungsdesign.md` > diese Datei > Chat.
> Team: Mark, Leon, Philip (Data Science, JLU Gießen). 16.09.2026, **Abgabe 17:00 in Stud.IP, intern 16:40.** Zu Sitzungsbeginn fragen, wer am Rechner sitzt, und `sessions/<NAME>.md` lesen.

## 0. Harte Grenzen
- **Nur in diesem Repository arbeiten.** Keine Dateien außerhalb lesen, schreiben oder durchsuchen (kein Home-Verzeichnis, kein `~/Library`, kein `~/Documents`, keine Obsidian-Vaults).
- **Zugangsdaten (`.hrz.env`, `.env`) niemals lesen, ausgeben, kopieren oder committen.**
- `data/raw/` nie überschreiben oder löschen; neue Version = neue Datei.
- Nur Dateien der eigenen Rolle ändern (§5). Fremde Dateien nur lesen.
- Kein `git push --force`, kein Rebase fremder Commits, kein Löschen von Branches.

## 1. Abgabe
1. **Wissenschaftliche Abhandlung (PDF)** — ≤ 37.500 Zeichen inkl. Leerzeichen (Fließtext inkl. Abstract; Deckblatt, Inhaltsverzeichnis, Literaturverzeichnis und Anhang sind Pflicht, zählen aber nicht).
2. **Dokumentation & Reflexion (PDF)** — ≤ 12.500 Zeichen, Einordnung in den Studienstand + Reflexion des Arbeits- und KI-Nutzungsprozesses.
Format: Arial 12 pt, Zeilenabstand 1,5, Ränder 2,5 cm, **APA 7** durchgängig, **Deutsch**. Anhang = Supplements, im Text referenziert. Fließtext entsteht im gemeinsamen Google Doc.

## 2. Forschungsfrage
**Wer schöpft die Rohstoffrenten ab? Der Anteil staatlicher Ressourceneinnahmen an den Rohstoffrenten in den Sahel-Staaten im Vergleich zu Subsahara-Afrika (2000–2021)**
Teilfragen, Operationalisierung, Abbildungsplan und Zeichenbudget: `docs/Forschungsdesign.md`.
**Fachlicher Kontext:** Data Science — deskriptiv-vergleichende Panelanalyse offener Sekundärdaten.

## 3. Kernfestlegungen
- Analysefenster **2000–2021**. Sahel: MLI, BFA, NER, TCD, MRT (Sensitivität + SDN, SEN). Vergleich: übrige WB-Region SSF.
- **Capture Ratio** = GRD Total Resource Revenue (% BIP) ÷ WDI `NY.GDP.TOTL.RT.ZS` (% BIP); nur bei Renten ≥ 1 % BIP; > 1,5 flaggen; zentriertes 3-Jahres-Mittel.
- Tests auf **Länder-Periodenmitteln** (2000–07, 2008–14, 2015–21), nie auf gepoolten Länderjahren.
- **Datenschema `data/processed/panel.csv`** ist in `docs/Forschungsdesign.md` §4 festgelegt. Alle Skripte lesen genau diese Spalten. Schema nur Mark ändert — nach Absprache.
- Plan B (EITI als Zähler), wenn < 3 Sahel-Länder ≥ 10 Jahre GRD-Daten *und* Renten haben. Entscheidung spätestens 12:15.

## 4. Verzeichnisse
```
docs/               Arbeitsauftrag.pdf, Forschungsdesign.md
sessions/           MARK.md, PHILIP.md, LEON.md
data/raw/           manuell geladene Rohdaten (GRD nicht committen, siehe .gitignore)
data/processed/     panel.csv (+ Dummy: panel_dummy.csv)
src/                nummerierte, einzeln lauffähige Skripte
figures/            PNG 300 dpi + captions.md
tables/             Markdown-Tabellen
results/zahlen.md   ALLE Zahlen für den Text, je mit Skriptverweis
text/abschnitte/    Entwürfe je Abschnitt (werden ins Google Doc übernommen)
text/anhang/        A_code.md B_datenquellen.md C_suchprotokoll.md D_tabellen.md E_prompts.md
text/quellen.bib    nur DOI-geprüfte Quellen
text/reflexion.md   Entwurf Dokumentation & Reflexion
logs/               LOG_<name>.md (manuell/Claude), prompts_<name>.md (automatisch per Hook)
.claude/hooks/      Protokoll-Hooks (nicht verändern)
.claude/agents/     Projekt-Subagenten
```

## 5. Dateihoheit
| Person | Schreibt in |
|---|---|
| Mark | `src/01_*`–`src/03_*`, `data/processed/panel.csv`, `figures/fig1–3*`, `tables/tab1*`, `tables/abdeckung.md`, `results/zahlen.md` Abschnitt „Mark“, `text/abschnitte/00_abstract.md`, `04_methodik.md`, `05_1_*.md`, `08_fazit.md`, `text/anhang/A_*`, `B_*`, `D_*`, `E_*`, `logs/LOG_mark.md`, `logs/prompts_mark.md` |
| Philip | `src/00_dummy_panel.py`, `data/processed/panel_dummy.csv`, `src/04_*`–`src/06_*`, `figures/fig4–5*`, `tables/tab2*`, `tables/tab3*`, `results/zahlen.md` Abschnitt „Philip“, `text/abschnitte/05_2_*`–`05_4_*`, `07_limitationen.md`, `text/reflexion.md`, `logs/LOG_philip.md`, `logs/prompts_philip.md` |
| Leon | `text/abschnitte/01_einleitung.md`, `02_theorie.md`, `03_forschungsstand.md`, `06_diskussion.md`, `text/quellen.bib`, `text/anhang/C_suchprotokoll.md`, `logs/LOG_leon.md`, `logs/prompts_leon.md` |
`figures/captions.md` und `results/zahlen.md`: jede Person nur ihren eigenen Abschnitt.

## 6. Arbeitsregeln
1. **Keine Quelle erfinden.** Nur zitieren, was mit DOI/URL geprüft ist; sonst in `text/anhang/C_suchprotokoll.md` als „nicht verifiziert“.
2. **Keine Zahl in einem Textentwurf, die nicht in `results/zahlen.md` steht.**
3. Abbildungen: matplotlib, `dpi=300`, `bbox_inches="tight"`, deutsche Achsenbeschriftung mit Einheit, Legende, Quelle in `figures/captions.md` („Quelle: World Bank WDI, ICTD/UNU-WIDER GRD 2023; eigene Berechnung und Darstellung.“). Keine Screenshots.
4. Statistik: n immer angeben; Assoziation ≠ Kausalität; Effektgrößen vor p-Werten.
5. Textentwürfe: wissenschaftliches Deutsch, nüchtern, „wir“ bzw. „die vorliegende Arbeit“, Zitate APA 7 im Format (Autor, Jahr), Zeichenbudget laut Forschungsdesign §8, danach gegen `STRAWBERRY.md` prüfen.
6. **Log (Pflicht, Grundlage der Reflexion):** Nach jeder abgeschlossenen Teilaufgabe, jedem Subagenten-Einsatz, jeder verworfenen Idee und jedem entdeckten KI-Fehler eine Zeile in `logs/LOG_<name>.md`: `HH:MM · Aufgabe · Modell/Subagent · Ergebnis oder „verworfen, weil …“`. KI-Fehler zusätzlich unter „## KI-Fehler und Korrekturen“. **Automatisch per Hook** (`.claude/settings.json`): jeder Prompt landet mit Uhrzeit in `logs/prompts_<name>.md`; beim Sitzungsstart wird an die Pflicht erinnert; wenn das Log > 25 Min. nicht aktualisiert wurde, fordert der Stop-Hook einmal zum Nachtragen auf. Log-Dateien mit der jeweiligen Arbeit committen.
7. **Git:** kleine Commits nur mit eigenen Dateien, `git pull --rebase` vor `git push`, Nachricht `<name>: <was>` auf Deutsch.
8. Subagenten (`.claude/agents/`) für abgegrenzte Aufgaben nutzen; nie zwei Agenten parallel dieselbe Datei schreiben lassen.
9. Bei Unklarheit zur Aufgabe: `docs/Arbeitsauftrag.pdf` lesen, nicht raten.

## 7. Befehle
```bash
pip install -r requirements.txt
python src/01_laden.py && python src/02_abdeckung.py && python src/03_capture_ratio.py
python count_chars.py text/abschnitte            # Summe der Entwürfe, Limit 37.500
python count_chars.py export_abhandlung.txt 37500 # Google-Doc-Export (Nur Text) prüfen
python count_chars.py text/reflexion.md 12500
```
