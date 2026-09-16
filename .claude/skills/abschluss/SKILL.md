---
name: abschluss
description: Teilaufgabe sauber abschließen — Log-Zeile, nur eigene Dateien committen, pull --rebase, push
disable-model-invocation: true
---
1. Person über `git config user.name` bestimmen.
2. `git status` — zeige, welche geänderten Dateien laut CLAUDE.md §5 zur Person gehören und welche nicht. Fremde Dateien NICHT stagen; bei Unklarheit fragen.
3. Log-Zeile in `logs/LOG_<name>.md` ergänzen (HH:MM · Aufgabe · Modell/Subagent · Ergebnis/verworfen; KI-Fehler gesondert), falls noch nicht geschehen.
4. Eigene Dateien + `logs/LOG_<name>.md` + `logs/prompts_<name>.md` stagen, Commit `<name>: <kurze Beschreibung auf Deutsch>` ($ARGUMENTS als Beschreibung, falls angegeben).
5. `git pull --rebase` und `git push`. Bei Konflikt: nicht selbst auflösen, sondern Stand erklären und fragen.
