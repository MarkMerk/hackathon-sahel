---
description: Einstieg — erklärt der Person am Rechner ihre Rolle, ihre Aufgaben, Dateien und den ersten Schritt
---
Du startest eine Arbeitssitzung im Projekt „Wer schöpft die Rohstoffrenten ab?“ (AI Hackathon, JLU, heute, Abgabe 17:00).

1. Führe `git config user.name` und `git pull --rebase` aus. Bestimme daraus die Person (Mark, Philip oder Leon). Wenn unklar oder `$ARGUMENTS` einen Namen enthält, nimm den Namen aus `$ARGUMENTS`; sonst frage nach.
2. Lies `CLAUDE.md`, `docs/Forschungsdesign.md`, `sessions/<NAME>.md` und `logs/LOG_<name>.md`. Lies `docs/Arbeitsauftrag.pdf` nur, wenn etwas unklar ist.
3. Prüfe mit `git log --oneline -15` und einem Blick in `data/processed/`, `figures/`, `text/abschnitte/`, was im Team schon erledigt ist.
4. Erkläre der Person auf Deutsch, knapp und konkret (max. ~35 Zeilen):
   - **Worum es geht:** Forschungsfrage in 2 Sätzen, was die Capture Ratio misst und warum.
   - **Deine Rolle:** wofür du verantwortlich bist und wie dein Teil in die Abhandlung einfließt (welche Abschnitte, Abbildungen, Tabellen, Zeichenbudget).
   - **Deine Dateien:** welche Dateien du schreiben darfst (laut CLAUDE.md §5) und welche du nur liest.
   - **Abhängigkeiten:** worauf du von den anderen wartest und wer auf dich wartet (z. B. panel.csv von Mark um ca. 12:15).
   - **Zeitplan:** deine Blöcke laut README mit Uhrzeiten; markiere, wo wir laut aktueller Uhrzeit stehen.
   - **Regeln, die du nicht brechen darfst:** keine erfundenen Quellen, Zahlen nur aus results/zahlen.md, nur eigene Dateien, Log-Pflicht.
   - **Jetzt als Erstes:** der konkrete nächste Schritt aus `sessions/<NAME>.md`, passend zum aktuellen Repo-Stand.
5. Frage am Ende: „Soll ich mit diesem Schritt beginnen?“ und warte. Trage eine Log-Zeile „Sitzung gestartet, Einweisung per /start“ in `logs/LOG_<name>.md` ein.
