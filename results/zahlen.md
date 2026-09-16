# Zahlen für den Text

Jede Zahl mit Skriptverweis. Nur eigener Abschnitt bearbeiten.

## Mark

## Philip

> **Stand 12:05 — noch keine Zahlen eingetragen.** Die Skripte `src/04`–`src/06`
> laufen, aber bislang nur auf `panel_dummy.csv`. Dummy-Werte werden hier
> bewusst **nicht** aufgeführt (CLAUDE.md §6.2). Sobald `data/processed/panel.csv`
> von Mark vorliegt, werden die Skripte erneut ausgeführt und die Zahlen hier
> eingetragen.

### Gruppenvergleich (`src/04_gruppenvergleich.py` → `tables/tab2_gruppenvergleich.md`, `figures/fig4_boxplot.png`)
Einzutragen je Periode (2000–2007, 2008–2014, 2015–2021):
- n Sahel / n übriges SSA (Länder-Periodenmittel, ≥ 3 gültige Jahre)
- Median und IQR der Capture Ratio je Gruppe
- Mann-Whitney-U, p, Cliff's δ mit Einordnung

### Zusammenhang mit Entwicklung (`src/05_zusammenhang_hdi.py` → `tables/tab2b_zusammenhang.md`, `figures/fig5_hdi.png`)
- Spearman ρ, p, n für Capture Ratio ↔ HDI (gesamt und je Periode)
- Spearman ρ, p, n für Capture Ratio ↔ Stromzugang (gesamt und je Periode)
- FE-OLS: Koeffizient der Capture Ratio, Cluster-SE, p, 95-%-KI, n, Anzahl Länder
- *Durchgängig als Assoziation formulieren, nicht als Effekt.*

### Robustheit (`src/06_robustheit.py` → `tables/tab3_robustheit.md`)
- Cliff's δ und p je Periode für die Varianten (a) ohne Ölstaaten, (b) Sahel
  erweitert um SDN/SEN, (c) 5-Jahres-Mittel, (d) ohne geflaggte Länderjahre
  (Ratio > 1,5), (e) mindestens 5 gültige Jahre
- Vorzeichenstabilität gegenüber der Hauptspezifikation je Variante
- Anzahl geflaggter Länderjahre (`flag_ratio_high`) im Datensatz
