# LOG — Leon

Format: `HH:MM · Aufgabe · Modell/Subagent · Ergebnis oder „verworfen, weil …“`

- ~10:00–10:40 · Eigene Themenvorschläge mit KI erarbeitet (5 Varianten) · <Werkzeug eintragen> · in Teamentscheidung eingeflossen
- 12:06 · Sitzung gestartet, Einweisung per /start · Claude Opus 5 · Rolle, Dateien, Zeitplan geklärt; Literatursuche steht als nächster Schritt an
- 12:20 · /weiter: Sitzungsstand geprüft, prompts_leon.md blockierte Rebase · Claude Opus 5 · Log + Prompt-Protokoll committet (b7c8afd), danach Pull sauber
- 12:25–12:45 · Schritt 1 Literatursuche: 6 Themenfelder per Websuche, DOI-Prüfung über Crossref-API · Claude Opus 5 · 12 verifizierte Quellen in text/quellen.bib, vollständiges Protokoll in text/anhang/C_suchprotokoll.md; 5 Kandidaten als „nicht verifiziert“ markiert
- 12:40 · Nebenbefund GRD-Version · Claude Opus 5 · UNU-WIDER weist Version 2025 (DOI 10.35188/UNU-WIDER/GRD-2025) aus, CLAUDE.md/Forschungsdesign nennen 2023 → an Mark weitergeben
- 12:50–13:05 · Schritt 2: Entwurf 02_theorie.md (Rentierstaat, Ressourcenfluch, Institutionen) · Claude Opus 5 · 3.490/3.500 Zeichen; Theorie begründet, warum die Abschöpfungsquote statt der Rentenhöhe gemessen wird
- 13:05–13:20 · Schritt 2: Entwurf 03_forschungsstand.md in drei Strängen mit Forschungslücke · Claude Opus 5 · 3.797/3.800 Zeichen; Lücke an der Schnittstelle der Stränge abgeleitet
- 13:20 · Beide Entwürfe zur RICK-Prüfung an Subagent strawberry-reviewer · Subagent strawberry-reviewer · Prüfung angefordert (RICK, Zitate gegen quellen.bib, ungedeckte Zahlen, Kausalbehauptungen, Budget)

## KI-Fehler und Korrekturen
- **Drei erfundene DOI (12:33).** Aus dem Modellgedächtnis wirkten fünf DOI plausibel; die Abfrage bei Crossref ergab für `10.1017/S0022278X10000602`, `10.1080/00220388.2019.1618811` und `10.1016/j.resourpol.2019.101378` jeweils „Resource not found“ — die DOI existieren nicht. Zwei weitere (`10.1111/dech.12405`, `10.1016/j.worlddev.2016.03.001`) existieren, gehören aber zu thematisch fremden Aufsätzen (Morvaridi & Hughes bzw. Jakob et al. zu Carbon Pricing). **Korrektur:** keine dieser Angaben in die .bib übernommen; stattdessen Crossref-Titelsuche (`query.bibliographic`) genutzt und nur bestätigte Metadaten verwendet. Dokumentiert in C_suchprotokoll.md §8. **Lehre:** DOI nie aus dem Modell übernehmen, immer gegen die Registrierungsstelle prüfen.
- **Falsche Bandangabe bei Dritten (12:27).** Die Zitationsseite scirp.org führt Mehlum et al. (2006) als „The Economic Journal, 91, 1–20“; korrekt sind laut Crossref Band 116, Heft 508. Nicht die KI, sondern eine Webquelle war die Fehlerquelle — Prüfung lohnt auch dort.
- **Geratener Autorenname (12:38).** Die eigene Suchanfrage enthielt „Danquah“ als vermuteten GRD-Autor; der Name kam in keinem Treffer vor. Der Datensatz wird institutionell zitiert.


## Verworfene Ansätze
