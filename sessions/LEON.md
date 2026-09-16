# Sitzungsleitfaden — Leon (Theorie, Forschungsstand, Einleitung, Diskussion, Literatur)

> Für Claude Code in Leons Terminal. Schwerpunkt Literatur und Text. Grundregel: **Keine Quelle ohne geprüfte DOI/URL.** Alles, was die KI vorschlägt, wird geöffnet und kontrolliert, bevor es in `text/quellen.bib` kommt.

## Rolle
Theoretischer Rahmen, Forschungsstand mit Forschungslücke, Einleitung, Diskussion inkl. Fallbeispiele Niger (Uran) und Mali (Gold), Literaturverzeichnis APA 7, Suchprotokoll (Anhang C), Formatierung im Google Doc.

## Ablauf

### Schritt 1 — Literatursuche (11:15–12:15)
Prompt:
```
Lies CLAUDE.md und docs/Forschungsdesign.md. Suche Literatur (Websuche) zu: (1) Rentierstaat, (2) Resource Curse, (3) Institutionen und Ressourcenreichtum, (4) government take / fiskalische Regime im Bergbau und Öl in Afrika (IMF, ICTD, UNU-WIDER), (5) illicit financial flows im Rohstoffsektor Afrikas, (6) Rohstoffpolitik im Sahel nach 2020 (Bergbaukodex Mali 2023, Verstaatlichung SOMAÏR Niger 2025).
Ziel: 12–15 Quellen, davon ≥ 4 Klassiker und ≥ 5 Arbeiten ab 2015. Für jede: vollständige APA-7-Angabe, DOI oder stabile URL, 2 Sätze Kernaussage, 1 Satz Bezug zu unserer Forschungsfrage.
Schreibe jede Suchanfrage (Datum, Werkzeug, Suchbegriffe, Treffer übernommen/verworfen + Grund) in text/anhang/C_suchprotokoll.md.
Trage in text/quellen.bib NUR Quellen ein, deren DOI/URL du tatsächlich aufgerufen hast; markiere alle anderen im Suchprotokoll als „nicht verifiziert“.
```
- Leon öffnet jede DOI selbst. Commit + Push, damit Mark die Liste parallel mit Claude Science prüfen kann.

### Schritt 2 — Theorie und Forschungsstand (12:15–13:30)
- Prompt P3 aus `PROMPTS.md`: `02_theorie.md` (3.500) und `03_forschungsstand.md` (3.800, RICK).
- Forschungsstand muss enden mit einer **klar formulierten Forschungslücke**, z. B.: Arbeiten zum Resource Curse messen meist Rentenhöhe, selten die staatliche Abschöpfung; vergleichende Evidenz zum Sahel ist dünn. (Nur so formulieren, wenn die Literatur das stützt.)

### Schritt 3 — Einleitung und Diskussion (13:30–15:00)
- `01_einleitung.md` (4.000, WHWN): Kontext Sahel, Motivation mit Quellen, Forschungslücke, Forschungsfrage + Teilfragen, Vorgehen in 2–3 Sätzen, Beitrag der Arbeit (explizit), Aufbau.
- `06_diskussion.md` (6.000, REFLOW): Ergebnisse (aus `results/zahlen.md` und Entwürfen von Mark/Philip) mit Theorie und Literatur vergleichen; Antwort auf „wem kommt es zugute“; Fallbeispiele Niger/Uran und Mali/Gold als Einordnung der Entwicklung nach 2021 (qualitativ, belegt); Implikationen, auch mit Blick auf europäische Rohstoff- und Energieinteressen; offene Fragen.
- Zahlen nur aus `results/zahlen.md`. Fehlt eine Zahl → Mark oder Philip fragen, nicht schätzen.

### Schritt 4 — Literatur und Format (15:00–16:25)
- Korrekturen aus Marks Claude-Science-Prüfung einarbeiten.
- Literaturverzeichnis APA 7 im Google Doc aus `text/quellen.bib`; jede im Text zitierte Quelle steht im Verzeichnis und umgekehrt.
- Google Doc formatieren: Arial 12, Zeilenabstand 1,5, Ränder 2,5 cm, Deckblatt (Titel, Team, Veranstaltung „AI Hackathon im AI Summercamp 2026, JLU Gießen“, Datum), automatisches Inhaltsverzeichnis, nummerierte Abbildungen/Tabellen mit Quellenzeile, Anhang A–E.
