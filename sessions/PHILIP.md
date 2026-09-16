# Sitzungsleitfaden — Philip (Statistik, Gruppenvergleich, Robustheit, Limitationen, Reflexion)

> Für Claude Code in Philips Terminal. Arbeite Schritt für Schritt; nach jedem Schritt Log-Zeile, Commit, `git pull --rebase`, `git push`.

## Rolle
Statistische Auswertung auf Basis von `data/processed/panel.csv`: Gruppenvergleich je Periode, Zusammenhang mit HDI/Stromzugang, Robustheit, Abb. 4–5, Tab. 2–3, Ergebnisse 5.2–5.4, Limitationen, Entwurf der Dokumentation & Reflexion.

## Ablauf

### Schritt 1 — Setup und Dummy-Daten (11:15–11:45)
Prompt:
```
Lies CLAUDE.md und docs/Forschungsdesign.md. Schreibe src/00_dummy_panel.py, das data/processed/panel_dummy.csv mit exakt dem Schema aus §4 erzeugt: ca. 45 SSA-Länder (echte ISO3-Codes, Sahel-Flags korrekt), Jahre 2000–2021, plausible Zufallswerte (rents 0–40, res_rev 0–15, hdi 0.3–0.7, einzelne NaN), capture_ratio und period nach Definition. Seed fest. Kennzeichne im Dateikopf deutlich: DUMMY, nicht für Ergebnisse.
```

### Schritt 2 — Analyse-Skripte auf Dummy (11:45–12:15)
Alle Skripte lesen den Pfad über eine Variable `PANEL = "data/processed/panel.csv"` mit Fallback auf `panel_dummy.csv`, wenn die echte Datei fehlt — und geben dann eine deutliche Warnung aus.
```
Schreibe src/04_gruppenvergleich.py: Länder-Periodenmittel der capture_ratio (nur Länder mit ≥ 3 gültigen Jahren je Periode); je Periode Median, IQR, n für Sahel vs. übrige SSA; Mann-Whitney-U mit Effektgröße (r = Z/√N oder Cliff's Delta). Ausgabe tables/tab2_gruppenvergleich.md und Abb. 4 (Boxplots nach Periode und Gruppe, einzelne Länderpunkte überlagert) als figures/fig4_boxplot.png, dpi 300, deutsche Achsen.
Schreibe src/05_zusammenhang_hdi.py: Spearman capture_ratio ↔ hdi und ↔ elec_access_pct auf Länder-Periodenmitteln (n, rho, p); optional Two-way-FE-OLS hdi ~ capture_ratio + log(gdppc_const) mit Länder- und Jahres-FE, Cluster-SE nach Land (statsmodels). Abb. 5 Scatter capture_ratio vs. hdi, Sahel hervorgehoben: figures/fig5_hdi.png.
Schreibe src/06_robustheit.py: Wiederhole den Gruppenvergleich (a) ohne oil_state, (b) mit sahel_ext statt sahel, (c) mit 5-Jahres-Mittel. Ausgabe tables/tab3_robustheit.md.
Alle Zahlen zusätzlich in results/zahlen.md unter „Philip“ (mit Skriptname). Im Kommentar jeweils: Assoziation, keine Kausalität.
```

### Schritt 3 — Echte Daten (ab Marks Push, ca. 12:15–13:30)
- `git pull --rebase`, Skripte auf `panel.csv` laufen lassen, Ergebnisse plausibilisieren: Stimmen n mit `tables/abdeckung.md` überein? Ausreißer (`flag_ratio_high`) gesondert erwähnen.
- Commit + Push. Mark lässt den `statistik-pruefer` darüberlaufen — Befunde einarbeiten.

### Schritt 4 — Texte (13:30–15:00)
- Prompt P3 aus `PROMPTS.md` für `text/abschnitte/05_2_gruppenvergleich.md`, `05_3_hdi.md`, `05_4_robustheit.md` (zusammen ca. 4.500 Zeichen, ELVIRA) und `07_limitationen.md` (2.300, REFLOW-L).
- Limitationen mindestens: kleine Sahel-Gruppe (n = 5), Datenende 2021, fehlende GRD-Werte bei geringen Ressourceneinnahmen, Messfehler/Timing zwischen Renten und Einnahmen, Weltmarktpreise, Assoziation statt Kausalität, keine Aussage über Verteilung *innerhalb* des Staates.

### Schritt 5 — Dokumentation & Reflexion (15:00–16:25)
- Alle drei `logs/LOG_*.md` pullen, Prompt P5 aus `PROMPTS.md` → `text/reflexion.md` (≤ 12.500).
- Mark und Leon ergänzen je einen Absatz zur eigenen Rolle; dann `python count_chars.py text/reflexion.md 12500`, ins Google Doc übernehmen, formatieren.
