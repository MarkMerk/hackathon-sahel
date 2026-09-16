#!/usr/bin/env bash
# Delegiert EINE abgegrenzte Aufgabe an Sonnet über den Hackathon-API-Key (nicht über das Claude-Abo).
# Gedacht für Marks Opus-Hauptsitzung (Abo): Routinearbeit hierüber auslagern.
#
#   tools/sonnet_api.sh "Erzeuge Abbildung 2 laut docs/Forschungsdesign.md §6 ..."
#   SONNET_MODEL=claude-sonnet-4-5 tools/sonnet_api.sh "..."   # konkretes Modell erzwingen
#
# Voraussetzung: .hrz.env enthält den (neuen) Key als ANTHROPIC_API_KEY (ggf. + ANTHROPIC_BASE_URL).
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
[ -f .hrz.env ] || { echo "FEHLER: .hrz.env fehlt" >&2; exit 1; }
set -a; . ./.hrz.env; set +a
if [ -z "${ANTHROPIC_API_KEY:-}${ANTHROPIC_AUTH_TOKEN:-}" ]; then
  echo "FEHLER: weder ANTHROPIC_API_KEY noch ANTHROPIC_AUTH_TOKEN in .hrz.env" >&2; exit 1
fi
[ $# -ge 1 ] || { echo "Aufruf: tools/sonnet_api.sh \"<Auftrag>\"" >&2; exit 1; }
export HACKATHON_HEADLESS=1   # Hooks: Prompt als [API/Sonnet] markieren, keine Stop-Nachfrage
exec claude -p \
  --model "${SONNET_MODEL:-sonnet}" \
  --permission-mode acceptEdits \
  --allowedTools "Read,Write,Edit,Glob,Grep,Bash" \
  "Kontext: Projekt laut CLAUDE.md, Regeln dort gelten. Erledige genau diesen Auftrag, ändere nur die dafür nötigen Dateien, gib am Ende eine Zusammenfassung in max. 10 Zeilen (geänderte Dateien, Ergebnis, Probleme). Auftrag: $*"
