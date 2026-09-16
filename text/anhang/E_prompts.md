# Anhang E — Prompt-Protokoll und KI-Einsatz

## E.1 Werkzeuge und Modelle

Alle drei Teammitglieder arbeiteten mit **Claude Code** (Terminal-Agent), gesteuert über die projektspezifische `CLAUDE.md` und die Sitzungsleitfäden in `sessions/`. Eingesetzte Modelle laut Sitzungsprotokoll: **Claude Opus 5** (alle drei Sitzungen) sowie **Claude Fable 5.1** in der Vorbereitungsphase (Themenfindung, Cowork, vor Sitzungsbeginn). Für einzelne, klar abgegrenzte Aufträge nutzte Mark zusätzlich eine **Sonnet-Delegation über einen separaten API-Zugang** (`tools/sonnet_api.sh`), um die reguläre Nutzungsgrenze der Sitzung zu schonen; Aufträge wurden dabei mit demselben Kontextrahmen („Kontext: Projekt laut CLAUDE.md …“) an ein zweites, unabhängiges Claude-Code-Fenster übergeben.

Innerhalb von Claude Code kamen fünf projektspezifische **Subagenten** (`.claude/agents/`) für abgegrenzte, wiederholbare Teilaufgaben zum Einsatz:

| Subagent | Zweck |
|---|---|
| `daten-pruefer` | Prüft Rohdaten in `data/raw/` bzw. `data/processed/` (Spalten, Ländercodes, Jahresbereich, fehlende Werte, Abdeckung der Sahel-Länder) rein lesend, ohne etwas zu verändern. |
| `abbildungen` | Erzeugt genau eine wissenschaftliche Abbildung (matplotlib, 300 dpi, deutsche Beschriftung) samt Skript und Bildunterschrift aus `data/processed/panel.csv`. |
| `statistik-pruefer` | Prüft statistische Auswertungen (Skripte, Tabellen, `results/zahlen.md`) adversarial auf methodische Fehler und Überinterpretation, vor der Übernahme in den Text. |
| `strawberry-reviewer` | Bewertet einen Textentwurf gegen die STRaWBERRY-Checkliste (z. B. RICK, REFLOW) und das Zeichenbudget; liefert nur Befunde, schreibt nicht um. |
| `quellen-pruefer` | Prüft `text/quellen.bib` und das Suchprotokoll auf Vollständigkeit, APA-7-Tauglichkeit, DOI-Format und Konsistenz mit den Zitaten im Fließtext. |

Jeder Prompt wurde **automatisch per Hook** mit Uhrzeit in `logs/prompts_<name>.md` protokolliert (`.claude/settings.json`); manuelle Log-Zeilen zu Teilaufgaben, Subagenten-Einsätzen, verworfenen Ideen und KI-Fehlern stehen in `logs/LOG_<name>.md`. Beide Protokolltypen sind die Grundlage dieses Anhangs.

## E.2 Zentrale Prompts je Person

Auswahl der inhaltlich wichtigsten Prompts; rein bestätigende oder organisatorische Prompts („ok“, „weiter“, Git-Routine) sind ausgelassen. Wortlaut aus `logs/prompts_<name>.md`, bei Länge gekürzt (**[…]**). Mark formulierte seine Prompts auf Russisch; wiedergegeben ist eine deutsche Übersetzung, der Originalwortlaut steht im Protokoll.

### Mark

| Uhrzeit | Person | Modell/Agent | Prompt | Ergebnis/Verwendung |
|---|---|---|---|---|
| 12:29 | Mark | Claude Opus 5 | „Committe, wann du es für nötig hältst, mach alles Nötige, sag mir, wenn ich etwas von Hand tun muss, und starte ruhig Subagenten, wenn eine Aufgabe es erfordert.“ | Autonomie-Freigabe für Commits und Subagenten-Einsatz während der Sitzung. |
| 12:41 | Mark | Claude Opus 5 | „Mach weiter, aber sag mir zuerst, was ich Philip auf Deutsch antworten soll, damit er es in seinen Claude einfügt […], und sag mir, was ich auf diesen Bildern herunterladen soll.“ | Formulierung einer deutschen Nachricht an Philip sowie Interpretation der GRD-Download-Screenshots. |
| 12:45 | Mark | Claude Opus 5 | „Ich habe alles heruntergeladen und abgelegt, mach weiter […]“ (mit Bericht zu `text/quellen.bib`, 13 Einträgen, DOI-Prüfung über Crossref) | Fortsetzung der Arbeit nach GRD-Download; Quellenarbeit bestätigt. |
| 13:29 | Mark | Claude Opus 5 | „Ja, nehmen wir C. Sag Philip und Leon, was sie ändern müssen, und wie lautet am Ende die Aufgabe? […]“ | Entscheidung für Variante C (Rohstofftyp als Hauptbefund) und Kommunikation der Konsequenzen an Philip und Leon. |
| 13:35 | Mark | Claude Opus 5 | Weiterleitung von Philips Fehlermeldung: „Philip schreibt: 1. Mark sagen, dass sein Skript meinen Abschnitt löscht. src/03_capture_ratio.py schreibt results/zahlen.md komplett neu […]“ | Auslöser für die Korrektur der geteilten Datei `results/zahlen.md` (s. E.3). |
| 13:44 | Mark | Claude Opus 5 | „Ja, mach komplett selbstständig weiter und beobachte regelmäßig, was die anderen committen; ich bin etwa 30 Minuten weg.“ | Weitreichende Autonomie-Freigabe für ca. 30 Minuten eigenständiger Arbeit. |
| 15:10 | Mark | Claude Opus 5 | „Nutze nach Möglichkeit auch mein Sonnet über die API, um mein Abonnement zu schonen.“ | Einführung der Sonnet-API-Delegation für abgegrenzte Anhang-Aufträge. |
| 15:11 | Mark | Sonnet (API, delegiert) | „Erstelle text/anhang/D_tabellen.md (Anhang D — Tabellen). Schreibe NUR diese eine Datei. Übernimm die Tabellen unverändert […]“ | Anhang D per delegierter Sonnet-Instanz erstellt, ohne die Hauptsitzung zu belasten. |

### Philip

| Uhrzeit | Person | Modell/Agent | Prompt | Ergebnis/Verwendung |
|---|---|---|---|---|
| 12:43 | Philip | Claude Opus 5 | „Antwort von Mark (Stand 12:45): 1. GRD-VERSION — Leon hat recht, und es betrifft mehr als die Jahreszahl. […]“ | Übernahme der korrigierten GRD-Strukturannahmen (Version 2025, Skalierung, Blattstruktur) in die eigenen Skripte. |
| 13:33 | Philip | Claude Opus 5 | „DRINGEND — BEHOBEN, bitte einmal pullen. Du hattest recht: 03_capture_ratio.py hat results/zahlen.md komplett neu geschrieben und dabei deinen Abschnitt gelöscht. Mein Fehler […]“ | Bestätigung, dass die geteilte Datei repariert wurde; Grundlage für Wiederherstellung des eigenen Abschnitts. |
| 13:39 | Philip | Claude Opus 5 | „Was ist als nächstes zu tun? Ich glaube, die panel.csv Datei, nach der du gefragt hast ist jetzt vorhanden.“ | Auslöser für Schritt 3: Auswertungsskripte 04–06 auf dem echten Panel laufen lassen. |
| 13:45 | Philip | Claude Opus 5 | „Nachgerechnet und bestätigt — dein Befund trägt. […]“ | Unabhängige Bestätigung von Marks Ölstaaten-Befund; Grundlage für Variante (a1/a2) in Tab. 3. |
| 13:59 | Philip | Claude Opus 5 | „Ja, fange bitte mit der Reflexion an“ | Beginn des Entwurfs von `text/reflexion.md`. |
| 14:10 | Philip | Subagent `statistik-pruefer` (Hand-back) | Adversariale Methodik-Prüfung von `src/04`–`06`, Tab. 2/2b/3 und den zugehörigen Abschnitten | Vier kritische und zehn wichtige Befunde, die zu den in E.3 gelisteten Korrekturen führten. |
| 14:31 | Philip | Claude Opus 5 | „Die Diskussion ist fertig (5.990/6.000) […] Hier der Reflexionsbeitrag für Philip: Leon (Literatur, Theorie, Diskussion). Die KI beschleunigte die Literatursuche […]“ | Übernahme von Leons Reflexionsbeitrag und des Budgetstands in `text/reflexion.md`. |

### Leon

| Uhrzeit | Person | Modell/Agent | Prompt | Ergebnis/Verwendung |
|---|---|---|---|---|
| 12:55 | Leon | Subagent `strawberry-reviewer` (Hand-back) | RICK-Prüfung von `text/abschnitte/02_theorie.md` und `03_forschungsstand.md` | RICK 4/4 bestätigt, sechs Befunde (Kausalsprache, ungedeckte Quellenaussagen, APA-Suffixe) zur Überarbeitung. |
| 13:34 | Leon | Claude Opus 5 | „Ja, fang mit Theorie und Forschungsstand an. Beides braucht keine Zahlen. Vorher aber ein Befund, der deine Argumentation betrifft — eher zu deinem Vorteil. […]“ | Freigabe zum Schreiben von Theorie/Forschungsstand unter Berücksichtigung eines neuen Teambefunds. |
| 14:01 | Leon | Claude Opus 5 | „Ja schreibe die Diskussion jetzt, aber beachte folgende Anmerkungen von Mark und Philip: […] der Rohstofftyp-Befund den Regionsbefund überlagert. Öl vs. Gold/Uran: δ = +0,74 und +0,64 […]“ | Grundlage für die Umstellung von `06_diskussion.md` auf den Rohstofftyp als Hauptbefund. |
| 14:05 | Leon | Claude Opus 5 | „warum ist der write fehlgeschlagen?“ | Diagnose eines Werkzeugfehlers (AbortError beim Schreiben der Diskussion). |
| 14:10 | Leon | Claude Opus 5 | „Jetzt hat der write schon zum zweiten mal fehlgeschlagen, überlege dir, was schiefläuft da. Falls du das Problem gelöst bekommst, dann beachte folgendes von Philip: […] der Hauptbefund hat sich verschoben […]“ | Umstellung auf Bash-Heredoc als Workaround; inhaltliche Aktualisierung der Diskussion übernommen. |
| 14:30 | Leon | Subagent (Hand-back, „Review discussion section“) | Prüfung von `06_diskussion.md` nach der Umstellung auf den Rohstofftyp-Befund | Bestätigung der überarbeiteten Fassung vor Abgabe. |

## E.3 Entdeckte KI-Fehler und Korrekturen

Zusammengeführt aus den Abschnitten „KI-Fehler und Korrekturen“ in `logs/LOG_mark.md`, `logs/LOG_philip.md` und `logs/LOG_leon.md`.

| Uhrzeit | Person | Fehler | Korrektur |
|---|---|---|---|
| 12:26 | Leon | Fünf DOI aus dem Modellgedächtnis übernommen; drei existierten laut Crossref nicht, zwei gehörten zu thematisch fremden Aufsätzen. | Keine dieser Angaben in `quellen.bib` übernommen; stattdessen Crossref-Titelsuche genutzt, nur bestätigte Metadaten verwendet, im Suchprotokoll dokumentiert. |
| 12:27 | Leon | Falsche Bandangabe zu Mehlum et al. (2006) von einer Drittquelle übernommen (Band/Heft falsch). | Über Crossref korrigiert (Band 116, Heft 508). |
| 12:31 | Mark | Kodierungsannahme falsch: CSV-Leser ging von UTF-8 aus; UNDP-HDR-Datei ist latin-1 kodiert und brach den Import ab. | Kodierungen werden nacheinander probiert (utf-8-sig, dann latin-1) mit Konsolenhinweis. |
| 12:38 | Leon | Vermuteter Autorenname „Danquah“ als GRD-Autor in der Suchanfrage, kam in keinem Treffer vor. | Datensatz institutionell zitiert statt mit erratenem Autor. |
| 12:40 | Mark | Falsche Modellangabe im eigenen Log: Claude bezeichnete sich in vier Zeilen als „Opus 4.6“ statt des tatsächlich genutzten Opus 5. | Von Mark bemerkt und korrigiert; derselbe Fehler trat um 15:17 erneut auf und wurde ebenfalls korrigiert. |
| 12:20 | Philip | Dummy-Panel erzeugt, ohne dass `flag_ratio_high` in irgendeinem Länderjahr True war; Ausreißer-Pfad der Analyseskripte wäre ungetestet geblieben. | Vereinzelte Einnahmespitzen (Faktor 4–7) eingebaut, jetzt 5 geflaggte Länderjahre. |
| 12:24 | Philip | In Abb. 4/5 überdeckte die Legende Datenpunkte bzw. die Referenzlinie; Achsentitel kollidierte mit den n-Angaben. Nur bei visueller Kontrolle sichtbar, nicht im Code. | Legenden auf Figur-Ebene über die Zeichenfläche gelegt, y-Grenzen mit Headroom gesetzt. |
| 12:26 | Philip | Typannotation `dict \| None` (Python ≥ 3.10) verwendet, venv läuft aber auf Python 3.9.6 → TypeError. | `from __future__ import annotations` in allen betroffenen Skripten ergänzt. |
| 12:50 | Mark | Vier falsche Annahmen über die GRD-Struktur (Werte als Prozent statt Anteile, Datentabelle im falschen Blatt, keine Zwischenzeilen über der Kopfzeile, Duplikate nach Datenfülle statt Regierungsebene unterschieden). | `01_laden.py` an die reale Struktur angepasst: Multiplikation ×100, Blatt „Merged“, `skiprows=[1,2]`, General-Government vor Central-Government bevorzugt. |
| 13:05 (×4) | Philip | Im ersten Limitationsentwurf: feste Zahl „fünf Sahel-Staaten“ ohne Beleg; unbelegte Aussage zu symmetrischen GRD-Lücken; Datenende 2021 mit falscher Begründung („beide Quellen“ statt allein WDI); Aussage zum GRD-Nutzerleitfaden ohne Klammerzitat. | Platzhalter `<n_sahel>` eingesetzt; Aussage konditional formuliert; Begründung auf den Nenner beschränkt; Zitat (UNU-WIDER, 2025) ergänzt. |
| 13:05 | Philip | In Tab. 2 automatisch „Mit n = 4–4 Sahel-Ländern“ formuliert (Formatierungsartefakt bei identischem Minimum/Maximum). | Spannweite wird nur noch genannt, wenn sie tatsächlich variiert. |
| 13:05/13:20 | Mark / Philip | `src/03_capture_ratio.py` schrieb die geteilte Datei `results/zahlen.md` vollständig neu und löschte dabei Philips Abschnitt (CLAUDE.md §5 sieht getrennte Abschnittshoheit vor). | Philip stellte den Abschnitt wieder her und meldete den Fehler; Mark ergänzte eine Funktion `schreibe_abschnitt()`, die nur den eigenen Bereich zwischen Überschriften ersetzt. |
| 13:05 | Mark | Beim Testen von Philips Analysekette wurden versehentlich Dateien in Philips Hoheit überschrieben (`tab2_gruppenvergleich.md`, `fig4_boxplot.png`). | Per `git checkout --` zurückgesetzt, nichts davon committet. |
| 13:30 | Leon | Zwei Aussagen über Quelleninhalte ohne Deckung: eine unterstellte Bestätigung durch Debonheur (2025), eine Robustheitsaussage fälschlich van der Ploeg (2011) zugeschrieben. | Debonheur nur mit dem durch Crossref belegten Gegenstand beschrieben; van der Ploeg-Aussage auf das über ORA Oxford geprüfte Abstract gestützt, Messungs-Robustheit ohne Zuschreibung formuliert. |
| 13:35 | Leon | Fünf Kausalformulierungen („antreibt“, „ersetzt“, „Wachstumseffekt maßgeblich“, „beobachtbare Konsequenz“, „hemmt“) unterstellten Kausalität statt Assoziation. | Alle fünf auf Assoziations- bzw. Argumentationssprache umgestellt. |
| 13:40 | Leon | APA-Suffixe von Mehlum et al. 2006a/b nach Erscheinungslogik statt alphabetisch nach Titel vergeben. | Per Websuche korrigiert: „Cursed …“ = 2006a, „Institutions …“ = 2006b. |
| 13:42 | Leon | Zeichenbudget falsch gemessen: `count_chars.py` überspringt bei .md Überschriftenzeilen, der Export zählt sie mit; beide Abschnitte lagen faktisch über Budget. | Gegen die Export-Zählung nachgeprüft und angepasst (3.498/3.500 und 3.793/3.800). |
| 14:00 | Philip | Erster Entwurf von 5.2–5.4 lag mit 6.631 Zeichen 47 % über dem Budget von 4.500, weil das Budget erst nach dem Schreiben geprüft wurde. | In sieben Runden gekürzt, u. a. durch Streichung des methodischen Vorspanns. |
| 14:18 | Mark | Zahlen aus einer Agenten-Rückmeldung ungeprüft übernommen: Rang Tschads und Mauretaniens Rentenwert im Entwurf 5.1 falsch, in `results/zahlen.md` nicht belegt. | `03_capture_ratio.py` um eine Rangtabelle der Renten 2021 ergänzt, Entwurf an die berechneten Werte angeglichen. |
| 14:45 | Philip | Die Hauptspezifikation nutzte die vorgeschriebene 3-Jahres-Glättung nie (`capture_ratio` statt `capture_ratio_3y`); die Robustheitsvariante „5- statt 3-Jahres-Mittel“ verglich damit gegen eine nicht existierende Referenz. | Glättung als Hauptspezifikation gesetzt, ungeglättete Werte als eigene Variante (c0) geführt. |
| 14:47 | Philip | Öl-Klassifikation sachlich falsch: für den Rohstofftyp-Test wurde die für den Robustheits-Ausschluss definierte Spalte `oil_state` verwendet; Kamerun, Sudan und Mauretanien fälschlich als „ohne Öl“ eingeordnet. | Erweiterte Abgrenzung ergänzt; Befund wird dadurch stärker (δ + 0,54/+0,76/+0,78, alle p < 0,05). |
| 14:48 | Philip | „Innerhalb der Länder kein Zusammenhang“ aus einem FE-Nullbefund abgeleitet, obwohl der Koeffizient je Spezifikation das Vorzeichen wechselt und die scheinbare Präzision von Botswana stammt. | Als „nicht belastbar, Frage nicht beantwortbar“ formuliert. |
| 14:49 | Philip | Pseudoreplikation in Tab. 2b: Zeile „alle Perioden“ (ρ = 0,515, n = 68) zählte jedes Land bis zu dreimal. | Durch echten Querschnitt ersetzt (ρ = 0,517, n = 26, p = 0,007). |
| 14:49 | Philip | Robustheitsvariante (d) war nach einer eigenen Umstellung wirkungslos geworden, weil sie die falsche Spalte maskierte. | Beide Spalten maskiert und neu geglättet. |
| 14:50 | Philip | Multiples Testen bei 17 berichteten Tests nirgends erwähnt. | Holm-Korrektur berechnet und in `zahlen.md`, Tab. 3 und den Limitationen ausgewiesen; sechs Tests überleben. |
| 14:50 | Philip | Zensierung durch fehlende GRD-Werte gegen den eigenen Befund nicht quantifiziert (Ausfallquote Sahel 25 %, Vergleichsgruppe 56 %). | Als Variante (g) mit Imputation der fehlenden Zähler ergänzt und als stärkste Einschränkung in die Limitationen aufgenommen. |
| 14:52 | Mark | Überinterpretation in Abstract, Fazit und 5.1: Regionsunterschied als „Folge der Rohstoffstruktur, nicht der geografischen Lage“ dargestellt, Rohstofftyp zum alleinigen Hauptbefund erklärt. | Nach Gegenprobe (Ölstaaten aus beiden Gruppen entfernt, Sahel-Abstand bleibt bestehen) auf „zwei Muster bestehen nebeneinander und sind bei dieser Fallzahl nicht zu trennen“ umgeschrieben. |

## E.4 Vollständige Protokolle

Die vollständigen, ungekürzten Protokolle liegen im Repository unter `logs/`: die automatisch per Hook geführten Prompt-Protokolle (`logs/prompts_mark.md`, `logs/prompts_philip.md`, `logs/prompts_leon.md`) sowie die manuell gepflegten Arbeitslogs mit den vollständigen Abschnitten „KI-Fehler und Korrekturen“ und „Verworfene Ansätze“ (`logs/LOG_mark.md`, `logs/LOG_philip.md`, `logs/LOG_leon.md`).
