# Dokumentation und Reflexion

<!-- Budget: 12.500 Zeichen inkl. Leerzeichen (Arbeitsauftrag). Stand 14:15.
     Quellen: logs/LOG_mark.md, logs/LOG_philip.md, logs/LOG_leon.md,
     logs/prompts_*.md, CLAUDE.md, text/anhang/.
     OFFEN: je ein Absatz von Mark und Leon zur eigenen Rolle (Abschnitt 2, Ende). -->

## 1 Einordnung in den Studienstand

Wir sind drei Studierende der Data Science an der Justus-Liebig-Universität
Gießen. Die Aufgabe traf damit in ihrem methodischen Teil auf vorhandene
Kompetenzen: Aufbereitung und Zusammenführung heterogener Tabellen mit Python
und pandas, deskriptive und rangbasierte Statistik, Panelstruktur und ihre
Fallstricke, Visualisierung mit matplotlib sowie die Versionierung
gemeinsamer Arbeit mit Git. Auch die Sensibilität für Pseudoreplikation, für
den Unterschied zwischen Effektstärke und Signifikanz und für die Grenzen
kleiner Stichproben stammt aus dem Studium und nicht aus dieser Arbeit.

Außerhalb unserer Fachkompetenz lag der Gegenstand selbst. Die politische
Ökonomie rohstoffreicher Staaten, fiskalische Regime im Bergbau und die
Geschichte der Sahelstaaten sind für uns Neuland. Wir haben darauf auf zwei
Weisen reagiert. Erstens haben wir die Fragestellung so gewählt, dass sie mit
offenen Sekundärdaten deskriptiv-vergleichend beantwortbar ist, statt eine
Erklärungsfrage zu stellen, die Fachwissen über Institutionen und
Vertragsregime erfordert hätte. Zweitens haben wir jede inhaltliche Aussage an
eine belegte Quelle gebunden und den theoretischen Rahmen aus der zitierten
Literatur entwickelt, anstatt ihn zu paraphrasieren. Wo uns die Datenlage
Deutungsspielraum ließ, haben wir im Zweifel die zurückhaltendere Aussage
gewählt. Die auffälligste Konsequenz dieser Haltung ist, dass unser
Hauptbefund nicht die Antwort ist, die die Fragestellung erwarten ließ.

## 2 Arbeitsprozess

Der Tag begann mit der Themenfindung. Alle drei brachten eigene, jeweils mit
Sprachmodellen erarbeitete Vorschläge ein — insgesamt sechzehn Varianten.
Verworfen haben wir unter anderem eine ML-Prognose (zu wenige Länder für
belastbares Training), einen Solar- oder Abhängigkeitsindex (die Gewichtung
der Teilindikatoren wäre willkürlich gewesen), eine konfliktbezogene Analyse
(Registrierungspflicht der Daten, unlösbares Kausalitätsproblem) und eine
Fallstudie zum nigrischen Uran (n = 1). Gewählt haben wir die Frage nach der
Abschöpfung der Rohstoffrenten, weil sie eine klar definierte Kennzahl
erlaubt, auf zwei unabhängigen offenen Datensätzen aufsetzt und einen
Vergleich über Länder und Zeit zulässt.

Danach folgte die Datenprüfung. Die Rentenangaben der Weltbank enden für die
Sahelstaaten 2021, das Government Revenue Dataset reicht bis 2021/22 — daraus
ergab sich das Analysefenster 2000–2021, bevor die erste Zeile Code
geschrieben war. Wir hatten für den Fall unzureichender Abdeckung einen
Ersatzplan vorbereitet, der Staatseinnahmen aus der Extractive Industries
Transparency Initiative als Zähler verwendet hätte. Die Abdeckungsprüfung
entschied dagegen: Vier der fünf Sahel-Kernländer erreichen mindestens zehn
Jahre mit Renten und Ressourceneinnahmen. Mali fällt mit vier Jahren aus —
eine Einschränkung, die wir nicht umgehen, sondern in Methodik und
Limitationen benennen, weil Mali gleichzeitig eines der zentralen
Fallbeispiele der Diskussion ist.

Die Arbeit selbst organisierten wir über ein gemeinsames Git-Repository mit
strikt getrennter Dateihoheit: Mark übernahm Datenaufbereitung, Deskription
und Methodik, Philip die inferenzielle Statistik, Robustheit, Limitationen und
diesen Text, Leon Theorie, Forschungsstand, Diskussion und Literatur. Eine
Datei mit Regeln für alle Sitzungen legte Fragestellung, Datenschema,
Zuständigkeiten und Arbeitsregeln fest, sodass drei parallel laufende
Sitzungen dieselbe Operationalisierung verwendeten. Diese Trennung hat
Konflikte fast vollständig vermieden; die beiden Ausnahmen betrafen eine
bewusst geteilte Datei und werden unten beschrieben.

Vom Zeitplan sind wir zweimal abgewichen. Der Entscheidungspunkt über die
Datengrundlage verschob sich um rund vierzig Minuten, weil die GRD-Datei nur
über ein Formular zu beziehen ist. Diese Wartezeit haben wir genutzt, statt
sie abzuwarten: Die Analyseskripte entstanden gegen ein synthetisches Panel
mit identischem Schema und liefen beim Eintreffen der echten Daten ohne
Eingriff durch. Die zweite Abweichung war inhaltlich. Gegen 13:40 fiel bei
einer Prüfung der Gruppenzusammensetzung auf, dass der Unterschied zwischen
Sahel und übrigem Subsahara-Afrika weitgehend auf die sechs Ölstaaten der
Vergleichsgruppe zurückgeht. Wir haben daraufhin die Darstellung umgebaut: Der
Rohstofftyp wurde zum Hauptbefund, der Regionsvergleich zum abgeleiteten
Ergebnis. Fragestellung und Titel blieben unverändert, weil eine unerwartete
Antwort ein Ergebnis ist und kein Anlass, die Frage nachträglich anzupassen.

<!-- PLATZHALTER: Absatz Mark zur eigenen Rolle -->

<!-- PLATZHALTER: Absatz Leon zur eigenen Rolle -->

## 3 Einsatz von Sprachmodellen

Wir haben Claude in drei Formen genutzt. Für Tagesplanung und den Vergleich
der Themenvorschläge diente die Chat-Oberfläche. Die eigentliche Arbeit fand
in Claude Code statt, jeweils eine Sitzung pro Person im geteilten
Repository, gebunden an die Projektregeln und ergänzt durch spezialisierte
Unteragenten für Datenprüfung, Abbildungen, Statistik-Review und die Prüfung
der Textentwürfe gegen eine Schreibcheckliste. Für die Quellenrecherche kam
zusätzlich eine Websuche mit anschließender Verifikation über die
Crossref-Schnittstelle zum Einsatz. Alle eingegebenen Prompts wurden
automatisch mit Zeitstempel protokolliert; der Anhang enthält eine Auswahl.

Die Prompts waren überwiegend knapp und aufgabenbezogen, etwa „Schreibe ein
Skript, das Länder-Periodenmittel bildet, Mann-Whitney-U rechnet und Cliff's
Delta ausgibt", „Prüfe diesen Entwurf gegen die Checkliste, liefere nur
Befunde" oder „Rechne diesen Befund unabhängig nach". Auffällig ist im
Rückblick, wie viele Eingaben reine Verständnisfragen waren — etwa nach der
Funktionsweise des verwendeten Rangtests. Das Modell war hier so nützlich wie
ein Lehrbuch und schneller.

Entscheidend war jedoch nicht die Erzeugung, sondern die Prüfung. Wir haben
vier Kontrollen fest eingebaut, und jede hat Fehler gefunden. Die Prüfung
jeder DOI gegen Crossref ergab, dass drei von fünf aus dem Modellgedächtnis
stammende Kennungen nicht existierten und zwei weitere zu thematisch fremden
Aufsätzen gehörten; keine davon ist in unser Literaturverzeichnis gelangt. Die
Regel, dass keine Zahl in einem Textentwurf stehen darf, die nicht zuvor von
einem Skript berechnet und in einer zentralen Zahlendatei festgehalten wurde,
deckte mehrere falsche Werte auf, die aus Zusammenfassungen von Unteragenten
in Entwürfe gewandert waren — darunter ein falscher Rang und ein um ein
Zehntel abweichender Rentenwert. Der Zeichenzähler zeigte, dass erste
Textfassungen regelmäßig vierzig bis fünfzig Prozent über dem Budget lagen.
Das gegenseitige Gegenlesen fand schließlich die Fehler, die innerhalb einer
Sitzung unsichtbar blieben.

Vier Fehlertypen sind uns dabei besonders aufgefallen. Erstens die falsche
Strukturannahme: Ein Ladeskript war vorab gegen synthetische Daten
geschrieben worden und traf vier Annahmen über die echte GRD-Datei, die alle
falsch waren. Die gravierendste betraf den Maßstab — die Werte sind Anteile,
nicht Prozentzahlen; unbemerkt wäre die zentrale Kennzahl um den Faktor
hundert zu klein gewesen. Aufgefallen ist das durch eine Größenordnungsprüfung
an Ölstaaten, deren Ressourceneinnahmen bekanntlich im zweistelligen Bereich
des Bruttoinlandsprodukts liegen. Zweitens die ungedeckte Aussage über eine
Quelle: Selbst bei korrekt verifizierter Veröffentlichung kann die inhaltliche
Behauptung über sie aus einer Suchzusammenfassung stammen und nicht aus dem
Text. Metadatenprüfung ersetzt keine Inhaltsprüfung. Drittens die
Kausalsprache, die sich unauffällig einschleicht: Wörter wie „antreibt" oder
„hemmt" unterstellen eine Wirkungsrichtung, die unsere Daten nicht hergeben.
Viertens die unsichtbare Darstellungsfehler — Legenden, die Datenpunkte
verdecken, oder ein einzelner Extremwert, der die gesamte relevante Variation
in ein Achsenzehntel staucht. Beides war im Code nicht erkennbar und fiel nur
auf, weil wir jede erzeugte Abbildung selbst angesehen haben.

Zwei Verstöße gegen unsere eigene Dateiordnung gehören ebenfalls hierher.
Einmal wurde ein fremdes Skript ausgeführt, um dessen Lauffähigkeit zu
prüfen — es schrieb dabei in Zieldateien, die einer anderen Person gehörten.
Ein anderes Mal überschrieb ein Skript eine bewusst geteilte Datei
vollständig und löschte den Abschnitt einer anderen Person. Beide Fälle
wurden bemerkt, zurückgesetzt und behoben, der zweite durch eine Funktion,
die nur den eigenen Abschnitt ersetzt. Bemerkenswert ist, dass es derselbe
Fehlertyp war: Ein Werkzeug schreibt weiter, als die Absicht reichte.

Ohne Modellunterstützung haben wir die Fragestellung ausgewählt, das
Analysefenster festgelegt, die Operationalisierung der Kennzahl bestimmt, die
Entscheidung über Haupt- und Ersatzplan getroffen und den Umbau der
Ergebnisdarstellung beschlossen, nachdem der Ölstaaten-Befund vorlag.

## 4 Reflexion

Beschleunigt hat die Modellunterstützung vor allem dort, wo die Aufgabe klar
umrissen war: beim Schreiben und Testen von Auswertungsskripten, beim Erzeugen
von Abbildungen, beim Auffinden von Literatur und beim systematischen Prüfen
eigener Entwürfe gegen eine Checkliste. Ein Arbeitstag dieser Dichte wäre ohne
sie nicht möglich gewesen. Kaum Zeit gespart hat sie beim Kürzen auf ein
Zeichenbudget, weil die ersten Fassungen verlässlich zu lang waren und das
Verdichten mehrere Durchgänge brauchte, und sie hat keine Zeit gespart bei
allem, was Urteil erforderte — welche Spezifikation die Forschungsfrage
tatsächlich beantwortet, wie ein nicht signifikanter Befund zu formulieren ist
und ob ein unerwartetes Ergebnis die Darstellung ändern muss.

Zur Verlässlichkeit unserer Ergebnisse äußern wir uns zurückhaltend. Die
Rechenwege sind reproduzierbar, die Daten sind offen, jede Zahl im Text ist
auf ein Skript zurückführbar. Die inhaltliche Belastbarkeit ist davon zu
trennen: Bei vier vergleichbaren Sahelstaaten erreicht kein Regionstest die
Signifikanzschwelle, und die Vergleichsgruppe ist nicht Subsahara-Afrika,
sondern dessen rohstoffreicher, im Datensatz erfasster Teil. Belastbar ist die
Richtung des Musters über alle Spezifikationen hinweg sowie der Kontrast nach
Rohstofftyp. Wir haben uns entschieden, das so zu schreiben, statt die
Unsicherheit sprachlich zu glätten.

Anders machen würden wir zwei Dinge. Die Struktur der Rohdaten würden wir vor
dem ersten Skript prüfen, nicht danach — die vier falschen Annahmen über die
GRD-Datei hätte ein einziger Blick in die Datei erspart. Und wir würden das
Zeichenbudget vor dem Schreiben in eine Zahl von Absätzen und Sätzen
übersetzen, statt es hinterher zu messen; das Kürzen hat mehr Zeit gekostet
als das Schreiben.

Die Verantwortung für diese Arbeit liegt bei uns. Sprachmodelle haben Code
geschrieben, Texte entworfen, Quellen vorgeschlagen und unsere Entwürfe
kritisiert. Sie haben dabei Zahlen falsch übernommen, Kennungen erfunden,
Strukturen falsch angenommen und unlesbare Abbildungen als fertig gemeldet.
Gefunden wurden diese Fehler durch Prüfschritte, die wir vorher festgelegt
haben, und durch das gegenseitige Lesen. Jede Aussage in dieser Arbeit haben
wir selbst geprüft und verantworten sie auch dann, wenn ihr erster Entwurf
nicht von uns stammt.
