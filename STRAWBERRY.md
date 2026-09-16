# STRaWBERRY — Checkliste für wissenschaftliches Schreiben (Kurzfassung für den Workspace)

Quelle: Theissler, Klaiber, Gerschner, Ritzer, Wang (2025), *Engaging students in scientific writing: The STRaWBERRY checklist framework with LLM-based paper draft assessment*, IEEE. https://ieeexplore.ieee.org/document/11016556 · Projektseite: https://www.ml-and-vis.org/strawberry

Grundgerüst: IMRaD (Introduction, Methods, Results, Discussion) + Related Work + Conclusion + Title + Abstract + Bibliography. Jede Komponente hat eine eigene Checkliste. Die Zuordnung zu Abschnitten muss nicht 1:1 sein.

| Komponente | Akronym | Kriterien — jedes Kriterium muss im Text nachweisbar sein |
|---|---|---|
| **Title** | SPICE | **S**pecific · **P**recise · **I**nteresting · **C**ompact · **E**asy to understand |
| **Abstract** | The-5-S | **S**hort · **S**elf-contained · **S**pecific · **S**tatement of novelty · **S**ummary of most important results (mit Zahlen!) |
| **Related Work** | RICK | **R**ecent papers cited · **I**mprovement of own work w.r.t. related work shown · **C**ontrasted to own work · **K**nowledge gap deduced |
| **Introduction** | WHWN | **W**hy? (Motivation, gestützt durch Quellen) · **H**ow? (Methodik in 2–3 Sätzen) · **W**hat's **N**ew? (Novelty + explizite Liste der Beiträge) |
| **Methods** | BURNS | **B**acked by acknowledged research methods · **U**nderstandable · **R**eproducible · **N**ovel · **S**ystematic |
| **Results** | ELVIRA | **E**xplained · **L**abelled (Abb./Tab. nummeriert, Achsen, Einheiten) · **V**isually supported · **I**nspire discussion · **R**eproducible · **A**ddress the research question / hypothesis |
| **Discussion** | REFLOW | **R**esults discussed · **E**valuation conducted · **F**indings stated · **L**imitations stated · **O**pen issues identified · **W**ork critically evaluated |
| **Conclusion** | RIB | **R**esearch summary · **I**nsights summary · **B**eginning of new research |
| **Bibliography** | YEAR | **Y**our full list of cited work · **E**mbedding own work in related work · **A**cknowledged sources · **R**elevant papers |

## Empfohlener Aufbau der Einleitung (WHWN)
1. Einführung ins Thema mit Quellen.
2. Motivation über research gap / Defizit bisheriger Arbeiten — mit konkreten Zitaten belegt.
3. Forschungsfrage(n) — als Frage oder als Aussage („Wir untersuchen, ob X …“).
4. Methodik in 2–3 Sätzen.
5. Explizit benannte Novelty.
6. Explizit aufgelistete Beiträge (Contributions).
7. Aufbau der Arbeit.

## Related Work muss zwei Dinge beweisen
- Das Problem ist relevant (andere forschen daran).
- Die eigene Arbeit leistet einen Beitrag (sie unterscheidet sich von den anderen). Aus dem Vergleich wird die **knowledge gap** abgeleitet → logische Brücke zur Forschungsfrage.

## Limitations
Pflicht. Ehrlich benannte Grenzen sind ein Zeichen von Reife, nicht von Schwäche. Typisch hier: kleine Sahel-Gruppe (n = 5), Datenende 2021, fehlende GRD-Werte, Assoziation ≠ Kausalität, Qualität der Sekundärdaten.

## Wichtige Einschränkung des Frameworks
STRaWBERRY bewertet die **Qualität des Schreibens**, nicht die Qualität der Forschung. Ein Text kann alle Kriterien erfüllen und trotzdem ein schlechtes Design haben. Beides prüfen.

## Wie die Checkliste im Hackathon benutzt wird
- Jeder Abschnitt wird nach dem Entwurf gegen seine Zeile in der Tabelle geprüft (Prompt P3 in `PROMPTS.md`).
- Vor der Abgabe ein Gesamtdurchlauf über das PDF (Subagent `strawberry-reviewer`, Prompt P4 — Nachbau des STRaWBERRY-LLM: Rolle Gutachter:in, je Komponente Kriterium → erfüllt/nicht erfüllt → Beleg-Satz aus dem Text).
- Bekannte Schwäche des LLM-Checks: Results werden oft zu Unrecht kritisiert, weil Zahlen in Abbildungen/Tabellen stehen. Deshalb: zentrale Zahlen **auch im Fließtext** nennen.
