#!/usr/bin/env python3
"""Stop: Wenn seit > 25 Min. kein Eintrag in logs/LOG_<person>.md erfolgte, Claude einmal zum Nachtragen auffordern."""
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(__file__))
from _person import person, project_dir  # noqa: E402

try:
    data = json.load(sys.stdin)
except Exception:
    data = {}
if data.get("stop_hook_active"):
    sys.exit(0)  # keine Endlosschleife

p = person()
log = os.path.join(project_dir(), "logs", f"LOG_{p}.md")
prompts = os.path.join(project_dir(), "logs", f"prompts_{p}.md")
if not os.path.exists(prompts):
    sys.exit(0)
try:
    last_log = os.path.getmtime(log) if os.path.exists(log) else 0
except OSError:
    sys.exit(0)
if time.time() - last_log > 25 * 60:
    print(
        f"Protokollpflicht: logs/LOG_{p}.md wurde seit über 25 Minuten nicht aktualisiert. "
        f"Trage jetzt kurz die seitdem erledigten Teilaufgaben, eingesetzten Subagenten, verworfenen Ansätze "
        f"und ggf. KI-Fehler nach (Format laut CLAUDE.md §6) und beende dann.",
        file=sys.stderr,
    )
    sys.exit(2)
sys.exit(0)
