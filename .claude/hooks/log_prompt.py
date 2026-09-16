#!/usr/bin/env python3
"""UserPromptSubmit: schreibt jeden Prompt mit Uhrzeit nach logs/prompts_<person>.md (Anhang E / Reflexion)."""
import datetime as dt
from zoneinfo import ZoneInfo
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _person import person, project_dir  # noqa: E402

try:
    data = json.load(sys.stdin)
except Exception:
    sys.exit(0)

prompt = str(data.get("prompt", "")).strip()
if not prompt:
    sys.exit(0)

# Geheimnisse schwärzen
prompt = re.sub(r"sk-ant-[A-Za-z0-9_\-]+", "[GESCHWÄRZT]", prompt)
prompt = re.sub(r"(?i)(api[_-]?key|token|passwor[dt]|secret)\s*[:=]\s*\S+", r"\1=[GESCHWÄRZT]", prompt)

short = prompt.replace("\n", " ⏎ ")
if len(short) > 600:
    short = short[:600] + " …"

p = person()
path = os.path.join(project_dir(), "logs", f"prompts_{p}.md")
os.makedirs(os.path.dirname(path), exist_ok=True)
new = not os.path.exists(path)
now = dt.datetime.now(ZoneInfo("Europe/Berlin")).strftime("%H:%M")
sid = str(data.get("session_id", ""))[:8]
with open(path, "a", encoding="utf-8") as f:
    if new:
        f.write(f"# Prompt-Protokoll — {p.capitalize()} (automatisch per Hook)\n\n")
    f.write(f"- {now} · Sitzung {sid} · {short}\n")
sys.exit(0)
