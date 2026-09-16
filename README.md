# hackathon-sahel — Wer schöpft die Rohstoffrenten ab?

AI Hackathon im AI Summercamp 2026 (JLU Gießen) · Team: **Mark, Leon, Philip** · 16.09.2026 · **Abgabe 17:00 in Stud.IP (intern 16:40)**

Forschungsfrage: *Wer schöpft die Rohstoffrenten ab? Der Anteil staatlicher Ressourceneinnahmen an den Rohstoffrenten in den Sahel-Staaten im Vergleich zu Subsahara-Afrika (2000–2021)*

| Datei | Wofür |
|---|---|
| `CLAUDE.md` | Regeln für jede Claude-Code-Sitzung (wird automatisch geladen) |
| `docs/Forschungsdesign.md` | Verbindliches Design: Fragen, Operationalisierung, Datenschema, Abbildungen, Zeichenbudget |
| `docs/Arbeitsauftrag.pdf` | Originale Aufgabenstellung |
| `sessions/MARK.md` · `sessions/PHILIP.md` · `sessions/LEON.md` | Persönlicher Ablauf und Start-Prompts je Person |
| `PROMPTS.md` | Gemeinsame Prompts (Sitzungsstart, Abschnitt schreiben, STRaWBERRY-Check, Reflexion, Formatcheck) |
| `STRAWBERRY.md` | Checkliste wissenschaftliches Schreiben |
| `DATA_DOWNLOAD.md` | Manuelle Datendownloads |
| `logs/LOG_<name>.md` | KI-Protokoll je Person (Grundlage für die Reflexion) |
| `.claude/agents/` | Projekt-Subagenten (Datenprüfung, Abbildungen, Statistik-Review, STRaWBERRY-Review, Quellenprüfung) |

## Setup (jede Person, 5 Minuten)
```bash
git clone <REPO-URL> hackathon-sahel && cd hackathon-sahel
python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
# API-Zugang wie von der Hackathon-Leitung vorgegeben laden (z. B. .hrz.env lokal, NIE committen)
claude
```
Erste Nachricht in Claude Code: *„Lies CLAUDE.md und sessions/<DEIN_NAME>.md und starte mit Schritt 1.“*

## Zeitplan
| Zeit | Mark | Philip | Leon |
|---|---|---|---|
| 11:15–11:45 | Repo, Downloads | Setup, Dummy-Panel nach Schema | Setup, Literatursuche Theorie |
| 11:45–12:15 | `panel.csv` + Abdeckung → **Entscheidung GRD/EITI (12:15)** | Analyse-Skripte auf Dummy-Daten | Literatur + Suchprotokoll |
| 12:15–13:30 | Capture Ratio, Abb. 1–3, Tab. 1 | Gruppenvergleich, HDI, Robustheit, Abb. 4–5, Tab. 2–3 | Theorie + Forschungsstand im Google Doc |
| 13:30–15:00 | Methodik, Ergebnisse 5.1 | Ergebnisse 5.2–5.4, Limitationen | Einleitung, Diskussion + Fallbeispiele |
| 15:00–15:45 | Abstract, Fazit, STRaWBERRY-Review, Claude-Science-Review | Reflexion (Entwurf aus `logs/`) | Literaturverzeichnis APA 7, Anhang C |
| 15:45–16:25 | Anhang A/B/D/E, Zeichen zählen | Reflexion final, Zeichen zählen | Formatierung Google Doc (Arial 12, 1,5, 2,5 cm) |
| 16:25–16:40 | **PDF-Export + Upload beider PDFs** | Gegenlesen | Gegenlesen |

**Stopp-Regeln:** 12:15 keine brauchbare GRD-Abdeckung → Plan B (EITI). 14:30 Ergebnisse unvollständig → Theorie/Forschungsstand kürzen, nie Methodik/Limitationen. 16:25 → nichts Neues mehr.

## Git-Workflow (drei Personen gleichzeitig auf `main`)
- **Jede Person ändert nur ihre eigenen Dateien** (Zuordnung in `CLAUDE.md` §5). Keine Überschneidungen → keine Konflikte.
- Vor jedem Push: `git pull --rebase`, dann `git push`. Kleine, häufige Commits.
- Commit-Nachrichten auf Deutsch, Präfix mit Name: `mark: panel.csv und Abdeckungstabelle`.
- Der Fließtext entsteht im **gemeinsamen Google Doc**; ins Repo kommen Code, Daten, Abbildungen, Tabellen, Zahlen, Anhang und Entwürfe.
