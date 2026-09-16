#!/usr/bin/env bash
# Delegiert EINE abgegrenzte Aufgabe an Sonnet über den Hackathon-OpenRouter-Key (nicht über das Claude-Abo).
#   tools/sonnet_api.sh "Erzeuge Abbildung 2 laut docs/Forschungsdesign.md §6 ..."
# Voraussetzung: .hrz.env enthält OPENROUTER_API_KEY=sk-or-...
# Eigener CLAUDE_CONFIG_DIR, damit Marks Abo-Login in der Hauptsitzung unberührt bleibt.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
[ -f .hrz.env ] || { echo "FEHLER: .hrz.env fehlt" >&2; exit 1; }
set -a; . ./.hrz.env; set +a
[ -n "${OPENROUTER_API_KEY:-}" ] || { echo "FEHLER: OPENROUTER_API_KEY fehlt in .hrz.env" >&2; exit 1; }
[ $# -ge 1 ] || { echo "Aufruf: tools/sonnet_api.sh \"<Auftrag>\"" >&2; exit 1; }
export ANTHROPIC_BASE_URL="https://openrouter.ai/api"
export ANTHROPIC_AUTH_TOKEN="$OPENROUTER_API_KEY"
export ANTHROPIC_API_KEY=""
export ANTHROPIC_DEFAULT_SONNET_MODEL="${SONNET_MODEL:-~anthropic/claude-sonnet-latest}"
export ANTHROPIC_DEFAULT_HAIKU_MODEL="~anthropic/claude-haiku-latest"
export CLAUDE_CODE_SUBAGENT_MODEL="$ANTHROPIC_DEFAULT_SONNET_MODEL"
export CLAUDE_CONFIG_DIR="${HOME}/.claude-openrouter"
export HACKATHON_HEADLESS=1
PROMPT="Kontext: Projekt laut CLAUDE.md, Regeln dort gelten. Erledige genau diesen Auftrag, ändere nur die dafür nötigen Dateien, gib am Ende eine Zusammenfassung in max. 10 Zeilen (geänderte Dateien, Ergebnis, Probleme). Auftrag: $*"
exec printf '%s' "$PROMPT" | claude -p \
  --model sonnet \
  --permission-mode acceptEdits \
  --allowedTools "Read,Write,Edit,Glob,Grep,Bash"
