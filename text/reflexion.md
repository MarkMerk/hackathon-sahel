# Dokumentation und Reflexion

<!-- Budget: 12.500 Zeichen inkl. Leerzeichen (Arbeitsauftrag). Stand 14:15.
     Quellen: logs/LOG_mark.md, logs/LOG_philip.md, logs/LOG_leon.md,
     logs/prompts_*.md, CLAUDE.md, text/anhang/.
     OFFEN: je ein Absatz von Mark und Leon zur eigenen Rolle (Abschnitt 2, Ende). -->

## 1 Einordnung in den Studienstand

Wir sind drei Studierende der Data Science an der Justus-Liebig-Universität
Gießen. Die Aufgabe traf damit in ihrem methodischen Teil auf vorhandene
Kompetenzen: Aufbereitung heterogener Tabellen mit Python und pandas,
deskriptive und rangbasierte Statistik, Panelstruktur und ihre Fallstricke,
Visualisierung sowie die Versionierung gemeinsamer Arbeit mit Git. Auch die
Sensibilität für Pseudoreplikation, für den Unterschied zwischen Effektstärke
und Signifikanz und für die Grenzen kleiner Stichproben stammt aus dem
Studium.

Außerhalb unserer Fachkompetenz lag der Gegenstand selbst. Die politische
Ökonomie rohstoffreicher Staaten, fiskalische Regime im Bergbau und die
Geschichte der Sahelstaaten sind für uns Neuland. Darauf haben wir zweifach
reagiert: Wir haben die Fragestellung so gewählt, dass sie mit offenen
Sekundärdaten deskriptiv-vergleichend beantwortbar ist, statt eine
Erklärungsfrage zu stellen, die Fachwissen über Institutionen und
Vertragsregime erfordert hätte. Und wir haben jede inhaltliche Aussage an eine
belegte Quelle gebunden, statt sie zu paraphrasieren. Wo die Datenlage
Deutungsspielraum ließ, haben wir die zurückhaltendere Aussage gewählt. Die
auffälligste Konsequenz dieser Haltung: Unser Hauptbefund ist nicht die
Antwort, die die Fragestellung erwarten ließ.

## 2 Arbeitsprozess

Der Tag begann mit der Themenfindung. Alle drei brachten eigene, mit
Sprachmodellen erarbeitete Vorschläge ein — insgesamt sechzehn Varianten.
Verworfen haben wir unter anderem eine ML-Prognose (zu wenige Länder für
belastbares Training), einen Abhängigkeitsindex (willkürliche Gewichtung der
Teilindikatoren), eine konfliktbezogene Analyse (Registrierungspflicht,
unlösbares Kausalitätsproblem) und eine Fallstudie zum nigrischen Uran
(n = 1). Gewählt haben wir die Frage nach der Abschöpfung der Rohstoffrenten,
weil sie eine klar definierte Kennzahl erlaubt, auf zwei unabhängigen offenen
Datensätzen aufsetzt und einen Vergleich über Länder und Zeit zulässt.

Danach folgte die Datenprüfung. Die Rentenangaben der Weltbank enden für die
Sahelstaaten 2021, das Government Revenue Dataset reicht bis 2021/22 — daraus
ergab sich das Analysefenster, bevor die erste Zeile Code geschrieben war. Für
den Fall unzureichender Abdeckung hatten wir einen Ersatzplan vorbereitet, der
Staatseinnahmen aus der Extractive Industries Transparency Initiative als
Zähler verwendet hätte. Die Abdeckungsprüfung entschied dagegen: Vier der fünf
Sahel-Kernländer erreichen mindestens zehn Jahre mit Renten und
Ressourceneinnahmen. Mali fällt mit vier Jahren aus — eine Einschränkung, die
wir nicht umgehen, sondern benennen, weil Mali gleichzeitig eines der
zentralen Fallbeispiele der Diskussion ist.

Die Arbeit organisierten wir über ein gemeinsames Git-Repository mit strikt
getrennter Dateihoheit: Mark übernahm Datenaufbereitung, Deskription und
Methodik, Philip die inferenzielle Statistik, Robustheit, Limitationen und
diesen Text, Leon Theorie, Forschungsstand, Diskussion und Literatur. Eine
Datei mit Regeln für alle Sitzungen legte Fragestellung, Datenschema und
Zuständigkeiten fest, sodass drei parallel laufende Sitzungen dieselbe
Operationalisierung verwendeten. Das hat Konflikte fast vollständig vermieden;
die beiden Ausnahmen betrafen eine geteilte Datei und werden unten beschrieben.

Vom Zeitplan sind wir zweimal abgewichen. Der Entscheidungspunkt über die
Datengrundlage verschob sich um rund vierzig Minuten, weil die GRD-Datei nur
über ein Formular zu beziehen ist. Diese Wartezeit haben wir genutzt: Die
Analyseskripte entstanden gegen ein synthetisches Panel mit identischem Schema
und liefen beim Eintreffen der echten Daten ohne Eingriff durch. Die zweite
Abweichung war inhaltlich. Gegen 13:40 fiel auf, dass der Unterschied zwischen
Sahel und übrigem Subsahara-Afrika weitgehend auf die Ölstaaten der
Vergleichsgruppe zurückgeht. Wir haben die Darstellung daraufhin umgebaut: Der
Rohstofftyp wurde zum Hauptbefund, der Regionsvergleich zum abgeleiteten
Ergebnis. Fragestellung und Titel blieben unverändert, weil eine unerwartete
Antwort ein Ergebnis ist und kein Anlass, die Frage nachträglich anzupassen.

Mark verantwortete Datenaufbereitung und Deskription. Sein lehrreichster
Fehler: Ein gegen synthetische Daten geschriebener Lader traf vier falsche
Annahmen über die echte Datei, darunter den Maßstab der Werte. Seither
prüft er jede Strukturannahme an der Quelle.

Leon verantwortete Literatur, Theorie und Diskussion. Die
Modellunterstützung beschleunigte die Literatursuche, war beim Belegen aber
unzuverlässig: Von fünf aus dem Modellgedächtnis vorgeschlagenen
DOI existierten drei nicht, zwei führten zu fremden Arbeiten. Keine ging in
die Quellenliste ein, jede Angabe wurde über die Crossref-Schnittstelle
bestätigt. Der lehrreichere Fehler war subtiler: Eine per DOI geprüfte Quelle
war zweimal für Aussagen herangezogen worden, die in ihr nie gelesen wurden.
Ein Prüfagent fand beides, ebenso vertauschte APA-Suffixe und eine falsch
gemessene Zeichenzahl; seither trennt das Suchprotokoll die bibliografische
von der inhaltlichen Prüfung. Der Arbeitsschritt verschob sich damit vom
Schreiben zum Verifizieren.

## 3 Einsatz von Sprachmodellen

Wir haben Claude in drei Formen genutzt. Für Tagesplanung und den Vergleich
der Themenvorschläge diente die Chat-Oberfläche. Die eigentliche Arbeit fand
in Claude Code statt, jeweils eine Sitzung pro Person im geteilten
Repository, gebunden an die Projektregeln und ergänzt durch spezialisierte
Unteragenten für Datenprüfung, Abbildungen, Statistik-Review und die Prüfung
der Textentwürfe gegen eine Schreibcheckliste. Für die Quellenrecherche kam
eine Websuche mit Verifikation über die Crossref-Schnittstelle hinzu. Alle
Prompts wurden automatisch mit Zeitstempel protokolliert; der Anhang enthält
eine Auswahl.

Die Prompts waren überwiegend knapp und aufgabenbezogen, etwa „Schreibe ein
Skript, das Länder-Periodenmittel bildet, Mann-Whitney-U rechnet und Cliff's
Delta ausgibt", „Prüfe diesen Entwurf gegen die Checkliste, liefere nur
Befunde" oder „Rechne diesen Befund unabhängig nach". Auffällig ist, wie viele
Eingaben reine Verständnisfragen waren — etwa nach der Funktionsweise des
verwendeten Rangtests. Das Modell war hier so nützlich wie ein Lehrbuch und
schneller.

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

Fünf Fehlertypen sind uns aufgefallen. Erstens die falsche Strukturannahme:
Ein Ladeskript war vorab gegen synthetische Daten geschrieben worden und traf
vier Annahmen über die echte GRD-Datei, die alle falsch waren. Die
gravierendste betraf den Maßstab — die Werte sind Anteile, nicht Prozentzahlen;
unbemerkt wäre die zentrale Kennzahl um den Faktor hundert zu klein gewesen.
Aufgefallen ist das durch eine Größenordnungsprüfung an Ölstaaten, deren
Ressourceneinnahmen im zweistelligen Bereich des Bruttoinlandsprodukts liegen.
Zweitens die ungedeckte Aussage über eine Quelle: Selbst bei korrekt
verifizierter Veröffentlichung kann die inhaltliche Behauptung über sie aus
einer Suchzusammenfassung stammen. Metadatenprüfung ersetzt keine
Inhaltsprüfung. Drittens die Kausalsprache: Wörter wie „antreibt" oder „hemmt"
unterstellen eine Wirkungsrichtung, die unsere Daten nicht hergeben. Viertens
Darstellungsfehler — Legenden, die Datenpunkte verdecken, oder ein einzelner
Extremwert, der die relevante Variation in ein Achsenzehntel staucht. Beides
war im Code nicht erkennbar und fiel nur auf, weil wir jede Abbildung selbst
angesehen haben.

Fünftens, und am folgenreichsten: die stillschweigend falsche Spezifikation.
Ein adversarial angesetzter Prüfagent fand, dass unsere Hauptspezifikation die
vorgeschriebene Dreijahresglättung überhaupt nicht verwendete; die
Robustheitsvariante „Fünf- statt Dreijahresmittel" verglich folglich gegen eine
Referenz, die es nicht gab. Derselbe Durchlauf zeigte, dass unsere
Öl-Klassifikation drei Ölförderer als Nicht-Ölförderer führte und dass eine als
„kein Zusammenhang über Zeit" formulierte Aussage nur besagte, dass die
Schätzung von wenigen Extremwerten getragen wird. Alle drei Punkte hätten in
der Abgabe gestanden — sie erzeugten plausible Zahlen und waren deshalb weder
in der Konsolenausgabe noch in den Tabellen sichtbar.

Zwei Verstöße gegen unsere Dateiordnung gehören hierher. Einmal wurde ein
fremdes Skript ausgeführt, um dessen Lauffähigkeit zu prüfen — es schrieb dabei
in Zieldateien einer anderen Person. Ein anderes Mal überschrieb ein Skript
eine geteilte Datei vollständig und löschte den Abschnitt einer anderen Person.
Beide Fälle wurden bemerkt und behoben. Bemerkenswert ist, dass es derselbe
Fehlertyp war: Ein Werkzeug schreibt weiter, als die Absicht reichte.

Ohne Modellunterstützung haben wir die Fragestellung ausgewählt, das
Analysefenster festgelegt, die Operationalisierung der Kennzahl bestimmt, die
Entscheidung über Haupt- und Ersatzplan getroffen und den Umbau der
Ergebnisdarstellung beschlossen, nachdem der Ölstaaten-Befund vorlag.

## 4 Reflexion

Beschleunigt hat die Modellunterstützung vor allem dort, wo die Aufgabe klar
umrissen war: beim Schreiben und Testen von Auswertungsskripten, beim Erzeugen
von Abbildungen, beim Auffinden von Literatur und beim Prüfen eigener
Entwürfe gegen eine Checkliste. Ein Arbeitstag wäre ohne sie
nicht möglich gewesen. Kaum Zeit gespart hat sie beim Kürzen auf ein
Zeichenbudget, weil die ersten Fassungen zu lang waren, und keine
Zeit bei allem, was Urteil erforderte — welche Spezifikation die
Forschungsfrage tatsächlich beantwortet, wie ein nicht signifikanter Befund zu
formulieren ist und ob ein unerwartetes Ergebnis die Darstellung ändern muss.

Zur Verlässlichkeit unserer Ergebnisse äußern wir uns zurückhaltend. Die
Rechenwege sind reproduzierbar, die Daten offen, jede Zahl im Text auf ein
Skript zurückführbar. Die inhaltliche Belastbarkeit ist davon zu trennen: Bei
vier vergleichbaren Sahelstaaten erreicht kein Regionstest die
Signifikanzschwelle, und die Vergleichsgruppe ist nicht Subsahara-Afrika,
sondern dessen rohstoffreicher, erfasster Teil. Belastbar ist die Richtung des
Musters sowie der Kontrast nach Rohstofftyp. Wir schreiben das so, statt die
Unsicherheit sprachlich zu glätten.

Anders machen würden wir drei Dinge. Die Struktur der Rohdaten würden wir vor
dem ersten Skript prüfen — die vier falschen Annahmen über die GRD-Datei hätte
ein Blick in die Datei erspart. Wir würden das Zeichenbudget vor dem Schreiben
in eine Zahl von Absätzen übersetzen, statt es hinterher zu messen; das Kürzen
hat mehr Zeit gekostet als das Schreiben. Und wir würden die adversariale
Prüfung früher ansetzen: Sie kam erst, als Tabellen und Textentwürfe fertig
waren, weshalb ein einzelner Befund die Neuberechnung aller Ergebnisse nach
sich zog. Bezeichnend ist, dass die schwerwiegendsten Fehler plausible Zahlen
erzeugten — falsche Ergebnisse fallen auf, falsche Spezifikationen nicht.

Die Verantwortung für diese Arbeit liegt bei uns. Sprachmodelle haben Code
geschrieben, Texte entworfen, Quellen vorgeschlagen und unsere Entwürfe
kritisiert. Sie haben dabei Zahlen falsch übernommen, Kennungen erfunden,
Strukturen falsch angenommen und unlesbare Abbildungen als fertig gemeldet.
Gefunden wurden diese Fehler durch Prüfschritte, die wir vorher festgelegt
haben, und durch das gegenseitige Lesen. Jede Aussage in dieser Arbeit haben
wir selbst geprüft und verantworten sie auch dann, wenn ihr erster Entwurf
nicht von uns stammt.
