# LOG — Philip

Format: `HH:MM · Aufgabe · Modell/Subagent · Ergebnis oder „verworfen, weil …“`

- ~10:00–10:40 · Eigene Themenvorschläge mit KI erarbeitet (5 Varianten) · <Werkzeug eintragen> · in Teamentscheidung eingeflossen
- 12:05 · Sitzung gestartet, Einweisung per /start · Claude Opus 5 · Rolle, Dateien, Zeitplan geklärt; Repo-Stand: src/ und data/processed/ noch leer, Schritt 1 offen
- 12:18 · Schritt 1: src/00_dummy_panel.py + data/processed/panel_dummy.csv · Claude Opus 5 · 1.056 Länderjahre, 48 SSA-Länder, Schema aus Forschungsdesign §4 exakt eingehalten, Seed 20260916; GRD-Fehlwertmuster (Lücken bei Einnahmen < 1 % BIP) nachgebildet
- 12:22 · src/04_gruppenvergleich.py + tables/tab2_gruppenvergleich.md + figures/fig4_boxplot.png · Claude Opus 5 · Länder-Periodenmittel (≥ 3 Jahre), Mann-Whitney-U + Cliff's Delta mit Einordnung nach Romano et al. (2006); Abb. 4 mit Länderpunkten und n je Box
- 12:26 · src/05_zusammenhang_hdi.py + tables/tab2b_zusammenhang.md + figures/fig5_hdi.png · Claude Opus 5 · Spearman Capture Ratio ↔ HDI und ↔ Stromzugang, Two-way-FE-OLS mit Cluster-SE nach Land; durchgängig als Assoziation ausgewiesen
- 12:28 · src/06_robustheit.py + tables/tab3_robustheit.md · Claude Opus 5 · sechs Varianten (Haupt, ohne Ölstaaten, sahel_ext, 5-Jahres-Mittel, ohne geflaggte Ausreißer, ≥ 5 Jahre); Kernkriterium Vorzeichenstabilität von Cliff's Delta statt p-Wert
- 12:29 · results/zahlen.md und figures/captions.md (Abschnitt Philip) · Claude Opus 5 · Gerüst mit Skriptverweisen angelegt, bewusst ohne Dummy-Zahlen (CLAUDE.md §6.2)
- 12:48 · Quellenangabe auf GRD 2025 korrigiert (Befund von Leon, bestätigt von Mark) · Claude Opus 5 · „ICTD/UNU-WIDER GRD 2023" → „UNU-WIDER GRD 2025" an 8 Stellen: in den drei Skripten 04–06 (dort entstehen die Zeilen) und in captions.md; Tabellen neu erzeugt
- 12:55 · text/abschnitte/07_limitationen.md (Schritt 4 vorgezogen) · Claude Opus 5 · 2.298 von 2.300 Zeichen; vier Blöcke: Indikatorkonstruktion, systematische GRD-Lücken, Reichweite der Aussagen, zeitliche Grenzen. Platzhalter <n_vergleich> für Marks Nachtrag. Vorgezogen, weil panel.csv noch fehlte und die Limitationen keine Zahlen brauchen
- 12:56 · STRaWBERRY-Prüfung des Limitationsentwurfs · Subagent strawberry-reviewer · REFLOW: L erfüllt (alle 5 Checklistenpunkte), aber 7 Befunde; drei designspezifische Limitationen fehlten
- 13:10 · Befunde eingearbeitet, 07_limitationen.md überarbeitet · Claude Opus 5 · neu aufgenommen: Modellcharakter des WDI-Nenners, Selektion durch den 1-%-Filter, multiples Testen ohne Adjustierung, wenige Cluster bei den FE-Standardfehlern; „fünf Sahel-Staaten" → Platzhalter, Symmetrie-Annahme konditional, Verweis auf Tab. 3 Variante d statt Methodikwiederholung; 2.296 von 2.300 Zeichen

- 13:05 · Schritt 3: Skripte 04–06 auf dem echten `panel.csv` · Claude Opus 5 · Kernbefund: Cliff's δ in allen drei Perioden negativ (−0,36 / −0,39 / −0,24), kein p-Wert < 0,05; Sahel-Median 0,10 / 0,21 / 0,15 gegen 0,51 / 0,25 / 0,27. Robustheit: alle 18 Zellen negativ, vollständige Vorzeichenstabilität
- 13:12 · Abb. 4 und 5 nach Sichtprüfung auf y- bzw. x-Grenze 1,6 begrenzt · Claude Opus 5 · Botswana (Quote bis 9,2) hatte die gesamte relevante Variation ins unterste Achsenzehntel gestaucht; gekappte Punkte als Dreieck/Pfeil markiert und in den Bildunterschriften ausgewiesen, Tests unverändert auf allen Werten
- 13:18 · Abdeckungsprüfung der Sahel-Gruppe · Claude Opus 5 · **Mali erreicht in keiner Periode die Schwelle von 3 gültigen Jahren** (18 Länderjahre mit Renten ≥ 1 % BIP ohne GRD-Wert); alle Tests laufen faktisch auf BFA, NER, TCD, MRT. In Tab. 2 jetzt explizit ausgewiesen, in den Limitationen ergänzt
- 13:20 · results/zahlen.md Abschnitt „Philip" mit echten Zahlen gefüllt · Claude Opus 5 · Gruppenvergleich, Spearman, FE-OLS und alle sechs Robustheitsvarianten
- 13:22 · Statistik-Review der Auswertung auf echten Daten · Subagent statistik-pruefer · läuft

## KI-Fehler und Korrekturen

- 13:20 · **Marks `src/03_capture_ratio.py` überschreibt `results/zahlen.md` vollständig** und hat dabei meinen Abschnitt „Philip" gelöscht (Commit 25fdd59) · gemeinsam genutzte Datei, laut CLAUDE.md §5 schreibt aber jede Person nur ihren Abschnitt · Abschnitt wiederhergestellt und mit echten Zahlen gefüllt; **an Mark gemeldet**: Das Skript muss den Fremdabschnitt erhalten, sonst geht er bei jedem seiner Läufe wieder verloren
- 13:10 · Claude formulierte in Tab. 2 automatisch „Mit n = 4–4 Sahel-Ländern" · Artefakt einer Spannweiten-Formatierung, wenn Minimum und Maximum gleich sind · Korrektur: Spannweite wird nur noch genannt, wenn sie tatsächlich variiert

- 12:20 · Claude erzeugte den Dummy zunächst so, dass `flag_ratio_high` in keinem einzigen Länderjahr True war · Folge: der Ausreißer-Pfad der Analyseskripte wäre ungetestet geblieben · Korrektur: vereinzelte Einnahmespitzen (Faktor 4–7, p = 0,03) eingebaut, jetzt 5 geflaggte Länderjahre
- 12:24 · Abb. 4 und Abb. 5: Legende überdeckte Datenpunkte bzw. die Referenzlinie, Achsentitel „Periode" kollidierte mit den n-Angaben · nur bei der visuellen Kontrolle des PNG aufgefallen, nicht im Code sichtbar · Korrektur: Legenden auf Figur-Ebene über die Zeichenfläche gelegt, y-Grenzen mit Headroom gesetzt
- 12:26 · Claude nutzte die Typannotation `dict | None` (Python ≥ 3.10), das venv läuft aber auf Python 3.9.6 → TypeError · Korrektur: `from __future__ import annotations` in allen Skripten
- 13:05 · Im ersten Limitationsentwurf schrieb Claude „fünf Sahel-Staaten" je Periode als feste Zahl · Verstoß gegen CLAUDE.md §6.2 (keine Zahl ohne results/zahlen.md) und sachlich unsicher, weil Tab. 2 nur Länder mit ≥ 3 gültigen Jahren je Periode aufnimmt — in Variante (a) sind es bereits 4 · vom strawberry-reviewer gefunden · Korrektur: Platzhalter `<n_sahel>`
- 13:05 · Claude behauptete im Indikativ, die GRD-Lücken beträfen „beide Gruppen, weshalb der Gruppenvergleich weniger betroffen ist" · das gilt nur bei symmetrischer Ausfallstruktur, die ohne tables/abdeckung.md nicht belegt ist · vom strawberry-reviewer gefunden · Korrektur: konditional formuliert („bei ähnlicher Ausfallstruktur beider Gruppen")
- 13:05 · Claude begründete das Datenende 2021 mit „beide Quellen weisen danach keine Werte aus" · falsch: bindend ist allein der WDI-Rentenindikator, das GRD reicht laut Forschungsdesign §1 bis 2021/22 und in Version 2025 vermutlich weiter · vom strawberry-reviewer gefunden · Korrektur: Begründung auf den Nenner beschränkt
- 13:05 · Die Aussage zum GRD-Nutzerleitfaden stand ohne Klammerzitat und ist im Suchprotokoll nicht als geprüft dokumentiert · Korrektur: (UNU-WIDER, 2025) gesetzt; **offen an Leon**: den User Guide selbst in C_suchprotokoll.md nachweisen, sonst ist die zentrale Aussage des Absatzes formal unbelegt

## Verworfene Ansätze

- 12:26 · FE-OLS auf Länder-Periodenmitteln statt Länderjahren · verworfen, weil Fixed Effects Variation innerhalb der Länder brauchen und drei Perioden je Land dafür zu wenig sind; stattdessen auf Länderjahren geschätzt mit Cluster-SE nach Land, während alle Tests weiter auf Periodenmitteln laufen
