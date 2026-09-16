#!/usr/bin/env python3
"""SessionStart: erinnert Claude an Rolle und Protokollpflicht (stdout wird Kontext)."""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from _person import person  # noqa: E402

p = person()
name = p.capitalize()
print(
    f"PROJEKTHINWEIS (automatisch): Am Rechner sitzt vermutlich {name}. "
    f"Lies CLAUDE.md und sessions/{name.upper()}.md, falls noch nicht geschehen. "
    f"PROTOKOLLPFLICHT: Nach jeder abgeschlossenen Teilaufgabe, jedem Subagenten-Einsatz, jeder verworfenen Idee "
    f"und jedem entdeckten KI-Fehler eine Zeile an logs/LOG_{p}.md anhängen "
    f"(Format: HH:MM · Aufgabe · Modell/Subagent · Ergebnis oder 'verworfen, weil …'; KI-Fehler zusätzlich unter "
    f"'## KI-Fehler und Korrekturen'). Die Prompts werden automatisch in logs/prompts_{p}.md mitgeschrieben. "
    f"Log-Dateien gemeinsam mit der jeweiligen Arbeit committen."
)
