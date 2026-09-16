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
| `logs/LOG_<name>.md` | KI-Protokoll je Person, von Claude nach jeder Teilaufgabe gepflegt (Grundlage für die Reflexion) |
| `logs/prompts_<name>.md` | Automatisches Prompt-Protokoll per Hook (Anhang E) |
| `.claude/agents/` | Projekt-Subagenten (Datenprüfung, Abbildungen, Statistik-Review, STRaWBERRY-Review, Quellenprüfung) |
| `.claude/commands/` | `/start`, `/weiter`, `/abschluss` |
| `.claude/hooks/` | Automatische Protokollierung |

## Setup (jede Person, ca. 5 Minuten)

**1. VS Code mit GitHub verbinden:** unten links Symbol *Accounts* → *Mit GitHub anmelden* → im Browser autorisieren. Einladung zum Repo vorher auf github.com/notifications annehmen.

**2. Klonen:** `Strg/Cmd+Shift+P` → *Git: Clone* → *Clone from GitHub* → `hackathon-sahel` → Ordner wählen → *Öffnen*.

**3. Im VS-Code-Terminal** (`` Strg+` ``):

macOS / Linux:
```bash
git config user.name "Vorname Nachname"      # Vorname bestimmt die Log-Datei (mark/philip/leon)
python3 -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
claude
```
Windows (PowerShell):
```powershell
git config user.name "Vorname Nachname"
py -m venv .venv
Set-ExecutionPolicy -Scope Process RemoteSigned   # nur falls Activate blockiert wird
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
claude
```
Windows-Voraussetzungen: Git for Windows (bringt Git Bash mit, das Claude Code benötigt) und Python 3.10+ von python.org mit Häkchen „Add python.exe to PATH“. Test: `python --version` muss eine echte Version zeigen (nicht den Microsoft Store öffnen).

**4. In Claude Code:** Beim ersten Start den Projekt-Hooks vertrauen (**ja** — sie schreiben nur in `logs/`). Dann eingeben:
```
/start
```
Claude erklärt dir deine Rolle, deine Dateien, Abhängigkeiten, deinen Zeitplan und den ersten Schritt.

| Befehl in Claude Code | Wofür |
|---|---|
| `/start` | Einweisung in die eigene Aufgabe (einmal zu Beginn oder nach Neustart) |
| `/weiter` | Stand prüfen, was die anderen gepusht haben, nächsten Schritt vorschlagen |
| `/abschluss <Beschreibung>` | Log-Zeile, nur eigene Dateien committen, pull --rebase, push |

### Mit der Claude-Code-Erweiterung für VS Code (grafisches Panel)
Die Erweiterung nutzt dieselbe Engine wie das Terminal: `CLAUDE.md`, `.claude/settings.json` (Deny-Regeln + Protokoll-Hooks), Subagenten und Projekt-Befehle gelten auch dort. Unterschiede und Lösungen:
- **`/start` erscheint nicht im `/`-Menü?** → Stattdessen eingeben: *„Lies .claude/commands/start.md und führe die Anweisungen aus. Ich bin <Name>.“* (analog `weiter.md`, `abschluss.md`).
- **Kein Terminal-Befehl `claude`:** Die Erweiterung bringt eine interne Kopie mit; für die Terminal-Variante Claude Code separat installieren oder in den Einstellungen *Extensions → Claude Code → Use Terminal* aktivieren.
- **Anmeldung mit dem Hackathon-API-Zugang statt eigenem Konto:** Die Erweiterung sieht Umgebungsvariablen nur, wenn VS Code sie erbt.
  - macOS/Linux: VS Code schließen, dann im Terminal im Repo-Ordner `set -a; source .hrz.env; set +a; code .`
  - Windows (oder als Alternative überall): Datei `.claude/settings.local.json` anlegen (ist in `.gitignore`, wird nie gepusht) mit `{ "env": { "<VARIABLE>": "<WERT>" } }` für jede Variable aus `.hrz.env` (z. B. `ANTHROPIC_API_KEY`, ggf. `ANTHROPIC_BASE_URL`). Danach *Developer: Reload Window*.
  - Erscheint trotzdem ein Login-Fenster und der Zugang läuft über ein Gateway (`ANTHROPIC_BASE_URL` gesetzt): in den VS-Code-Einstellungen *Claude Code → Disable Login Prompt* aktivieren.
- **Hooks prüfen:** `/` → *Customize → Hooks* muss SessionStart, UserPromptSubmit und Stop zeigen. Nach dem ersten Prompt existiert `logs/prompts_<name>.md`.

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
