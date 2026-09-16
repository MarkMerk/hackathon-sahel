# 4 Daten und Methodik

## 4.1 Design und Datenquellen

Die vorliegende Arbeit ist eine deskriptiv-vergleichende Panelanalyse offener Sekundärdaten. Untersuchungseinheit ist das Länderjahr; für Gruppenvergleiche werden daraus Länder-Periodenmittel gebildet. Das Design ist nicht kausal angelegt. Das Analysefenster 2000–2021 ergibt sich aus dem aktuellen Rand beider Hauptquellen; spätere Politikwechsel behandelt allein die Diskussion.

Die Analyse stützt sich auf drei offen zugängliche Quellen (Tab. 1). Die **Rohstoffrenten** stammen aus den World Development Indicators der Weltbank (`NY.GDP.TOTL.RT.ZS`; World Bank, 2026): die Differenz zwischen dem Wert der Förderung von Öl, Gas, Kohle, Mineralien und Holz zu Weltmarktpreisen und den Förderkosten, in Prozent des Bruttoinlandsprodukts. Der Indikator misst die erwirtschaftete Rente, unabhängig davon, wem sie zufließt. Die **staatlichen Ressourceneinnahmen** entnehmen wir dem UNU-WIDER Government Revenue Dataset 2025, Variable *Total Resource Revenue* (UNU-WIDER, 2025). Es harmonisiert Angaben von OECD und IWF und weist ressourcenbezogene Einnahmen gesondert aus. Für die Sahel-Länder enthält es ausschließlich Werte der Zentralregierung. Als **Entwicklungsindikatoren** dienen der Index der menschlichen Entwicklung (UNDP, 2025) sowie Bruttoinlandsprodukt pro Kopf (`NY.GDP.PCAP.KD`) und Stromzugang (`EG.ELC.ACCS.ZS`).

Als **Sahel-Kernländer** definieren wir Mali, Burkina Faso, Niger, Tschad und Mauretanien. Die **Vergleichsgruppe** bilden alle übrigen Länder der Weltbank-Region Subsahara-Afrika, einschließlich Sudan und Senegal, die eine Sensitivitätsprüfung dem Sahel zuordnet.

## 4.2 Die Abschöpfungsquote

Zentrale Kennzahl ist die **Abschöpfungsquote** (*Capture Ratio*) als Verhältnis der staatlichen Ressourceneinnahmen zu den Rohstoffrenten, beide in Prozent des Bruttoinlandsprodukts:

    Abschöpfungsquote = Ressourceneinnahmen (% BIP) / Rohstoffrenten (% BIP)

Ein Wert von 0,30 bedeutet, dass die im GRD verbuchten Ressourceneinnahmen 30 % der geschätzten Rente entsprechen. Der Ansatz greift den Gedanken des *government take* auf (Albertin et al., 2021) und verbindet die in der Resource-Curse-Forschung übliche Messung der Rentenhöhe (Sachs & Warner, 2001; van der Ploeg, 2011) mit der Frage nach der fiskalischen Aneignung, die Crivelli und Gupta (2014) allgemein untersuchen.

Zwei Festlegungen begrenzen die Instabilität des Quotienten. Erstens berechnen wir die Quote nur für Länderjahre mit Renten von mindestens einem Prozent des Bruttoinlandsprodukts, da ein kleiner Nenner zu beliebig großen Werten führt. Zweitens werden Werte über 1,5 gekennzeichnet, aber nicht entfernt: Sie weisen auf zeitliche Verschiebungen zwischen Rentenentstehung und Einnahmeverbuchung hin oder auf Einnahmen, die nicht der Rentendefinition der Weltbank entsprechen. Auf 455 gültige Länderjahre entfallen 19 solcher Fälle (4,2 %), keiner davon im Sahel. Da Renten unmittelbar den Weltmarktpreisen folgen, Steuerzahlungen dagegen zeitversetzt eingehen, glätten wir die Quote mit einem zentrierten Dreijahresmittel, das je Land gebildet wird, Lücken nicht überbrückt und auch den Tests zugrunde liegt.

## 4.3 Auswertungsverfahren

Die Quellen werden über ISO-3-Ländercode und Jahr zusammengeführt; fehlende Werte bleiben fehlend, es wird weder interpoliert noch fortgeschrieben.

Für den Gruppenvergleich aggregieren wir die Länderjahre zu **Länder-Periodenmitteln** über die Zeiträume 2000–2007, 2008–2014 und 2015–2021, wobei je Land und Periode mindestens drei gültige Jahre vorliegen müssen. Das verhindert, dass Länder mit langer Datenreihe mehrfach in einen Test eingehen (Pseudoreplikation). Auf dieser Ebene prüfen wir Gruppenunterschiede mit dem Mann-Whitney-U-Test und berichten Cliffs Delta als Effektgröße; angesichts der kleinen Gruppen ist diese aussagekräftiger als der p-Wert, beide werden mit der Fallzahl ausgewiesen. Den Zusammenhang mit der menschlichen Entwicklung prüfen wir über Spearman-Rangkorrelationen, ebenfalls auf Länder-Periodenmitteln, da beide Größen nicht normalverteilt sind. Die Robustheit prüfen wir in zehn Varianten (Abschnitt 5.4). Der Vergleich nach Rohstoffart war nicht vorab geplant und wurde post hoc ergänzt; für alle 17 Tests berichten wir zusätzlich die Holm-Korrektur.

## 4.4 Datenabdeckung und Reproduzierbarkeit

Das Panel umfasst 48 Länder und 1.056 Länderjahre. Für 1.014 liegen Rohstoffrenten vor, für 478 staatliche Ressourceneinnahmen; eine Abschöpfungsquote lässt sich für 455 Länderjahre in 28 Ländern berechnen. Die Abdeckung ist nicht zufällig verteilt: 20 der 48 Länder enthalten keinen einzigen Wert für Ressourceneinnahmen, und Länderjahre ohne solchen Wert weisen mit durchschnittlich 8,97 Prozent des Bruttoinlandsprodukts deutlich geringere Renten auf als Länderjahre mit Wert (14,28 Prozent). Der User Guide nennt den Grund: Ressourceneinnahmen werden häufig nicht gesondert ausgewiesen, wenn sie unter etwa einem Prozent des Bruttoinlandsprodukts liegen. Die Vergleichsgruppe entspricht damit nicht dem gesamten Subsahara-Afrika, sondern dessen rohstoffreichem, im Datensatz erfasstem Teil (Abschnitt 7).

Innerhalb des Sahel erfüllen vier der fünf Kernländer das Kriterium von mindestens zehn Jahren mit Renten und Ressourceneinnahmen: Niger mit 22, Burkina Faso mit 21, Mauretanien und Tschad mit je 18 Jahren. **Mali verfügt lediglich über vier Jahre (2013–2016)** und geht daher in keinen Gruppenvergleich ein; die Diskussion behandelt es auf Grundlage der Literatur.

Alle Zahlen, Tabellen und Abbildungen stammen aus einzeln lauffähigen Python-Skripten (<https://github.com/MarkMerk/hackathon-sahel>; Anhang A, D); Bezugsquellen und Abrufdaten nennt Anhang B, den Einsatz von KI-Werkzeugen Anhang E.
