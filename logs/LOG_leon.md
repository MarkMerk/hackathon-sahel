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
- 13:25–13:45 · Befunde des strawberry-reviewer eingearbeitet (6 Punkte) · Subagent strawberry-reviewer + Claude Opus 5 · RICK 4/4 bestätigt; Kausalsprache entschärft, zwei ungedeckte Quellenaussagen korrigiert, APA-Suffixe gedreht, Zeichenbudget auf Export-Zählung umgestellt
- 14:10-14:35 - Abschnitt 6 (Diskussion) geschrieben, 5.990/6.000 - Claude Opus 5 - REFLOW; Hauptbefund auf Rohstofftyp umgestellt (Philips Hinweis), Regionsbefund als nicht abgesichert ausgewiesen; alle Zahlen aus zahlen.md Abschnitt Philip; Mali nur ueber Tull (2026).
- 14:35 - Zeichenbudget gesamt geprueft - Claude Opus 5 - SUMME 38.828 bei Limit 37.500: 1.328 zu viel (Markdown-Zaehlung, Export liegt hoeher). An Team gemeldet.
- 14:20 - Write-Tool zweimal mit AbortError abgebrochen (Permission-Stream) - Claude Opus 5 - auf Bash-Heredoc ausgewichen, funktionierte.

## KI-Fehler und Korrekturen
- **Zwei Aussagen über Quelleninhalte ohne Deckung (13:30, vom Subagenten gefunden).** Im Forschungsstand stand „Debonheur (2025) bestätigt dies“ (Richtungsgleichheit mit Crivelli/Gupta) und eine Robustheitsaussage, die van der Ploeg (2011) zugeschrieben war, tatsächlich aber nur aus der Websuche-Zusammenfassung stammte. **Korrektur:** Debonheur nur noch mit dem durch Crossref belegten Untersuchungsgegenstand beschrieben; für van der Ploeg die Institutionen-Aussage aus dem über ORA Oxford aufgerufenen Abstract belegt und die Messungs-Robustheit als Literaturstand ohne Zuschreibung formuliert. **Lehre:** Auch bei korrekt verifizierter Quelle kann die inhaltliche Aussage über sie ungedeckt sein — Metadatenprüfung ersetzt keine Inhaltsprüfung.
- **Fünf Kausalformulierungen (13:35, vom Subagenten gefunden).** „antreibt“, „ersetzt“, „Wachstumseffekt maßgeblich“, „beobachtbare Konsequenz“, „hemmt“ unterstellten Kausalität, wo nur Assoziation oder eine Theorieaussage vorlag (CLAUDE.md §6.4). Alle fünf auf Assoziations- bzw. Argumentationssprache umgestellt.
- **APA-Suffixe vertauscht (13:40, vom Subagenten gefunden, unabhängig geprüft).** Ich hatte Mehlum et al. 2006a/b nach Erscheinungslogik vergeben. APA 7 vergibt alphabetisch nach Titel — per Websuche bestätigt. „Cursed …“ ist 2006a, „Institutions …“ ist 2006b; im Text getauscht und in quellen.bib als Notiz festgeschrieben.
- **Zeichenbudget falsch gemessen (13:42, vom Subagenten gefunden).** `count_chars.py` überspringt bei .md die Überschriftenzeilen, der Google-Doc-Export zählt sie mit. Beide Abschnitte lagen damit faktisch über Budget (Forschungsstand +153). Jetzt gegen die Export-Zählung geprüft: 3.498/3.500 und 3.793/3.800.

- **Drei erfundene DOI (12:33).** Aus dem Modellgedächtnis wirkten fünf DOI plausibel; die Abfrage bei Crossref ergab für `10.1017/S0022278X10000602`, `10.1080/00220388.2019.1618811` und `10.1016/j.resourpol.2019.101378` jeweils „Resource not found“ — die DOI existieren nicht. Zwei weitere (`10.1111/dech.12405`, `10.1016/j.worlddev.2016.03.001`) existieren, gehören aber zu thematisch fremden Aufsätzen (Morvaridi & Hughes bzw. Jakob et al. zu Carbon Pricing). **Korrektur:** keine dieser Angaben in die .bib übernommen; stattdessen Crossref-Titelsuche (`query.bibliographic`) genutzt und nur bestätigte Metadaten verwendet. Dokumentiert in C_suchprotokoll.md §8. **Lehre:** DOI nie aus dem Modell übernehmen, immer gegen die Registrierungsstelle prüfen.
- **Falsche Bandangabe bei Dritten (12:27).** Die Zitationsseite scirp.org führt Mehlum et al. (2006) als „The Economic Journal, 91, 1–20“; korrekt sind laut Crossref Band 116, Heft 508. Nicht die KI, sondern eine Webquelle war die Fehlerquelle — Prüfung lohnt auch dort.
- **Geratener Autorenname (12:38).** Die eigene Suchanfrage enthielt „Danquah“ als vermuteten GRD-Autor; der Name kam in keinem Treffer vor. Der Datensatz wird institutionell zitiert.


## Verworfene Ansätze
