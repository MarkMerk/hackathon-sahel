# Gemeinsame Prompts (Copy-Paste)

Persönliche Schritt-Prompts stehen in `sessions/<NAME>.md`. Platzhalter `<…>` ausfüllen.

## P0 — Sitzungsstart
```
Ich bin <Mark|Philip|Leon>. Lies CLAUDE.md, docs/Forschungsdesign.md, sessions/<NAME>.md und die letzten Zeilen von logs/LOG_<name>.md. Führe `git pull --rebase` aus. Fasse in 5 Zeilen zusammen: Forschungsfrage, Stand im Repo, mein nächster Schritt laut Leitfaden. Dann warte auf meine Bestätigung. Nach jeder abgeschlossenen Teilaufgabe: Log-Zeile, Commit nur mit meinen Dateien, pull --rebase, push.
```

## P3 — Abschnitt schreiben und prüfen
```
Schreibe den Entwurf text/abschnitte/<DATEI>.md. Budget: <N> Zeichen inkl. Leerzeichen (hart, laut docs/Forschungsdesign.md §8). Fakten nur aus results/zahlen.md, tables/, figures/captions.md und text/quellen.bib (Zitate als (Autor, Jahr) nach APA 7). Wissenschaftliches Deutsch, nüchtern, „wir“ bzw. „die vorliegende Arbeit“, keine Kausalbehauptungen.
Prüfe den Entwurf danach gegen die Zeile <AKRONYM> in STRAWBERRY.md: je Kriterium erfüllt/nicht erfüllt + Beleg-Satz. Überarbeite, bis alle Kriterien erfüllt sind und das Budget eingehalten ist. Gib am Ende `python count_chars.py text/abschnitte/<DATEI>.md` aus.
```
Zuordnung: 00_abstract → The-5-S · 01_einleitung → WHWN · 03_forschungsstand → RICK · 04_methodik → BURNS · 05_* → ELVIRA · 06_diskussion + 07_limitationen → REFLOW · 08_fazit → RIB · Titel → SPICE.

## P4 — STRaWBERRY-Gesamtprüfung
```
Nutze den Subagenten strawberry-reviewer auf <Datei, z. B. export_abhandlung.txt>. Gib mir seine Tabelle und die drei wichtigsten Änderungen zurück. Ändere selbst nichts.
```

## P5 — Dokumentation & Reflexion (≤ 12.500 Zeichen)
```
Schreibe text/reflexion.md aus logs/LOG_mark.md, logs/LOG_philip.md, logs/LOG_leon.md, den automatischen Prompt-Protokollen logs/prompts_*.md, CLAUDE.md und text/anhang/E_prompts.md. Fließtext, Deutsch, ≤ 12.500 Zeichen inkl. Leerzeichen, wir-Form, ehrlich, keine Werbesprache, keine Aufzählungslisten. Inhalt:
1. Einordnung im Studienstand: Team aus dem Data-Science-Studium der JLU Gießen; angewandte Kompetenzen (Datenaufbereitung mit Python/pandas, Statistik, Visualisierung, wissenschaftliches Schreiben nach STRaWBERRY); was außerhalb unserer Fachkompetenz lag (Politische Ökonomie der Sahelzone) und wie wir damit umgegangen sind.
2. Arbeitsprozess chronologisch: Themenfindung (Vorschläge aller drei, mit KI erarbeitet; welche Alternativen verworfen wurden und warum), Datenprüfung und Festlegung auf 2000–2021, Rollen- und Dateiaufteilung im Git-Repository, Abweichungen vom Zeitplan.
3. KI-Nutzung konkret: Claude (Cowork) für Planung und Themenvergleich, Claude Code je Person mit Projekt-Regeln (CLAUDE.md) und Subagenten für Datenprüfung, Abbildungen, Statistik- und STRaWBERRY-Review, Claude Science für Quellenprüfung und Review; 3–4 verkürzte Beispiel-Prompts; konkrete KI-Fehler aus den Logs und wie sie entdeckt wurden (DOI-Prüfung, Zahlen nur aus Skripten, Zeichenzähler, Gegenlesen); was bewusst ohne KI entschieden wurde.
4. Reflexion: Wo KI beschleunigt hat und wo nicht; Verlässlichkeit der Ergebnisse; was wir anders machen würden; Verantwortung für Inhalte liegt beim Team.
Gib am Ende die Zeichenzahl aus.
```

## P7 — Finaler Formatcheck
```
Prüfe die exportierten PDFs <Pfad Abhandlung> und <Pfad Reflexion>: Arial 12 durchgängig (PDF-Schriften auslesen, z. B. mit pdffonts falls vorhanden), Zeilenabstand 1,5, Ränder 2,5 cm, Deckblatt, Inhaltsverzeichnis, Abbildungen/Tabellen nummeriert und im Text referenziert, Literaturverzeichnis APA 7 vollständig, Anhang A–E vorhanden und referenziert, Zeichenzahl Fließtext ≤ 37.500 bzw. ≤ 12.500. Liste nur Abweichungen.
