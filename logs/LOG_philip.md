# LOG — Philip

Format: `HH:MM · Aufgabe · Modell/Subagent · Ergebnis oder „verworfen, weil …“`

- ~10:00–10:40 · Eigene Themenvorschläge mit KI erarbeitet (5 Varianten) · <Werkzeug eintragen> · in Teamentscheidung eingeflossen
- 12:05 · Sitzung gestartet, Einweisung per /start · Claude Opus 5 · Rolle, Dateien, Zeitplan geklärt; Repo-Stand: src/ und data/processed/ noch leer, Schritt 1 offen
- 12:18 · Schritt 1: src/00_dummy_panel.py + data/processed/panel_dummy.csv · Claude Opus 5 · 1.056 Länderjahre, 48 SSA-Länder, Schema aus Forschungsdesign §4 exakt eingehalten, Seed 20260916; GRD-Fehlwertmuster (Lücken bei Einnahmen < 1 % BIP) nachgebildet
- 12:22 · src/04_gruppenvergleich.py + tables/tab2_gruppenvergleich.md + figures/fig4_boxplot.png · Claude Opus 5 · Länder-Periodenmittel (≥ 3 Jahre), Mann-Whitney-U + Cliff's Delta mit Einordnung nach Romano et al. (2006); Abb. 4 mit Länderpunkten und n je Box
- 12:26 · src/05_zusammenhang_hdi.py + tables/tab2b_zusammenhang.md + figures/fig5_hdi.png · Claude Opus 5 · Spearman Capture Ratio ↔ HDI und ↔ Stromzugang, Two-way-FE-OLS mit Cluster-SE nach Land; durchgängig als Assoziation ausgewiesen
- 12:28 · src/06_robustheit.py + tables/tab3_robustheit.md · Claude Opus 5 · sechs Varianten (Haupt, ohne Ölstaaten, sahel_ext, 5-Jahres-Mittel, ohne geflaggte Ausreißer, ≥ 5 Jahre); Kernkriterium Vorzeichenstabilität von Cliff's Delta statt p-Wert
- 12:29 · results/zahlen.md und figures/captions.md (Abschnitt Philip) · Claude Opus 5 · Gerüst mit Skriptverweisen angelegt, bewusst ohne Dummy-Zahlen (CLAUDE.md §6.2)

## KI-Fehler und Korrekturen

- 12:20 · Claude erzeugte den Dummy zunächst so, dass `flag_ratio_high` in keinem einzigen Länderjahr True war · Folge: der Ausreißer-Pfad der Analyseskripte wäre ungetestet geblieben · Korrektur: vereinzelte Einnahmespitzen (Faktor 4–7, p = 0,03) eingebaut, jetzt 5 geflaggte Länderjahre
- 12:24 · Abb. 4 und Abb. 5: Legende überdeckte Datenpunkte bzw. die Referenzlinie, Achsentitel „Periode" kollidierte mit den n-Angaben · nur bei der visuellen Kontrolle des PNG aufgefallen, nicht im Code sichtbar · Korrektur: Legenden auf Figur-Ebene über die Zeichenfläche gelegt, y-Grenzen mit Headroom gesetzt
- 12:26 · Claude nutzte die Typannotation `dict | None` (Python ≥ 3.10), das venv läuft aber auf Python 3.9.6 → TypeError · Korrektur: `from __future__ import annotations` in allen Skripten

## Verworfene Ansätze

- 12:26 · FE-OLS auf Länder-Periodenmitteln statt Länderjahren · verworfen, weil Fixed Effects Variation innerhalb der Länder brauchen und drei Perioden je Land dafür zu wenig sind; stattdessen auf Länderjahren geschätzt mit Cluster-SE nach Land, während alle Tests weiter auf Periodenmitteln laufen
