#!/usr/bin/env python3
"""Zählt Zeichen inkl. Leerzeichen im Fließtext.

Aufruf:
  python count_chars.py text/abschnitte               # alle .md im Ordner, Limit 37500
  python count_chars.py export_abhandlung.txt 37500   # Google-Doc-Export (Datei → Herunterladen → Nur Text)
  python count_chars.py text/reflexion.md 12500

Bei .md werden nicht gezählt: Überschriften (# …), Bild-Einbettungen, Tabellenzeilen (| … |),
HTML-Kommentare, Trennlinien; Markdown-Betonung wird entfernt. Bei .txt wird alles gezählt
außer Leerzeilen — Deckblatt, Inhaltsverzeichnis, Literaturverzeichnis und Anhang vor dem
Export aus der Datei entfernen oder mit --von/--bis eingrenzen.
Exit-Code 1, wenn das Limit überschritten ist.
"""
import argparse
import glob
import os
import re
import sys


def count_md(text: str) -> int:
    keep = []
    for line in text.splitlines():
        s = line.strip()
        if not s or s.startswith(("#", "![", "<!--", "|", "---")):
            continue
        keep.append(line)
    body = "\n".join(keep)
    body = re.sub(r"\*\*|__|\*", "", body)
    return len(body)


def count_txt(text: str, von: str | None, bis: str | None) -> int:
    if von and von in text:
        text = text[text.index(von):]
    if bis and bis in text:
        text = text[: text.index(bis)]
    return len("\n".join(l for l in text.splitlines() if l.strip()))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("pfad", nargs="?", default="text/abschnitte")
    ap.add_argument("limit", nargs="?", type=int, default=37500)
    ap.add_argument("--von", help="Zählen ab dieser Textstelle (z. B. 'Abstract')")
    ap.add_argument("--bis", help="Zählen bis zu dieser Textstelle (z. B. 'Literaturverzeichnis')")
    a = ap.parse_args()

    files = sorted(glob.glob(os.path.join(a.pfad, "*.md"))) if os.path.isdir(a.pfad) else [a.pfad]
    total = 0
    for f in files:
        with open(f, encoding="utf-8") as fh:
            t = fh.read()
        n = count_md(t) if f.endswith(".md") else count_txt(t, a.von, a.bis)
        total += n
        print(f"{n:>7}  {f}")
    print(f"{total:>7}  SUMME  (Limit {a.limit}, Reserve {a.limit - total})")
    if total > a.limit:
        print("FEHLER: Limit überschritten")
        sys.exit(1)


if __name__ == "__main__":
    main()
