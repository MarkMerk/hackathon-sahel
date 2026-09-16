"""Ermittelt die Person am Rechner: HACKATHON_NAME > git user.name > $USER."""
import os
import re
import subprocess

TEAM = ("mark", "philip", "leon")


def person() -> str:
    raw = os.environ.get("HACKATHON_NAME", "")
    if not raw:
        try:
            raw = subprocess.run(["git", "config", "user.name"], capture_output=True, text=True, timeout=5).stdout
        except Exception:
            raw = ""
    raw = (raw or os.environ.get("USER", "unbekannt")).strip().lower()
    for t in TEAM:
        if t in raw:
            return t
    return re.sub(r"[^a-z0-9]+", "_", raw).strip("_") or "unbekannt"


def project_dir() -> str:
    return os.environ.get("CLAUDE_PROJECT_DIR", os.getcwd())
