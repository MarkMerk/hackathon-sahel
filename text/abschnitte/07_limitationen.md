# 7 Limitationen

<!-- Budget: 2.300 Zeichen inkl. Leerzeichen (Forschungsdesign §8). STRaWBERRY: REFLOW, Schwerpunkt L.
     PLATZHALTER (Mark trägt nach, sobald panel.csv und tables/abdeckung.md vorliegen):
       <n_sahel>     = Zahl der Sahel-Länder je Periode in Tab. 2 (kann 3–5 betragen, s. Variante a)
       <n_vergl_min> / <n_vergl_max> = Spannweite der Vergleichsgruppe über die drei Perioden
     Geprüft mit strawberry-reviewer (REFLOW) am 16.09., Befunde eingearbeitet. -->

**Konstruktion der Capture Ratio.** Der Indikator setzt zwei unterschiedlich
erhobene Größen ins Verhältnis: Die Weltbank schätzt Rohstoffrenten
modellbasiert aus Weltmarktpreis und Förderkosten, das Government Revenue
Dataset erfasst tatsächliche Zahlungseingänge (UNU-WIDER, 2025; World Bank,
2026). Messfehler im geschätzten Nenner schlagen durch. Renten fallen mit der
Förderung an, Abgaben folgen verzögert; das Dreijahresmittel dämpft dies nur
(vgl. Tab. 3, Variante d).

**Systematische Datenlücken.** Der Nutzerleitfaden dokumentiert, dass Werte
überwiegend fehlen, wenn die Ressourceneinnahmen unter etwa einem Prozent des
Bruttoinlandsprodukts liegen (UNU-WIDER, 2025). Sie häufen sich am
Rand der Verteilung, sodass die Quoten die tatsächlichen eher überschätzen —
bei ähnlicher Ausfallstruktur beider Gruppen vor allem im Niveau, weniger im
Gruppenvergleich. Manche Land-Jahr-Angaben liegen zudem mehrfach vor, weil
verschiedene Regierungsebenen berichten; wir behalten die belegtere Zeile.

**Reichweite der Aussagen.** Alle Ergebnisse sind Assoziationen, keine
Kausalaussagen, und sie gelten allein für rohstoffreiche Länderjahre, da nur
Werte ab einem Prozent Renten eingehen. Die Rangtests beruhen auf
Länder-Periodenmitteln, um Pseudoreplikation zu vermeiden; je Periode stehen
<n_sahel> Sahel-Staaten <n_vergl_min> bis <n_vergl_max> Vergleichsländern
gegenüber. Die Teststärke ist gering, und wir prüfen viele Spezifikationen
ohne Adjustierung: Ein einzelner p-Wert unter 0,05 wäre kein Befund, weshalb
wir Effektgrößen vorrangig lesen. Auch geclusterte Standardfehler sind bei so
wenigen Clustern unzuverlässig.

**Zeitliche Grenzen.** Das Fenster endet 2021, weil der Rentenindikator
danach keine Werte für die Sahel-Staaten ausweist; Politikwechsel
nach 2021 liegen außerhalb der Daten (Abschnitt 6). Zudem sagt eine hohe
Quote nichts über die Mittelverwendung: Über die Verteilung im Staat erlauben
unsere Daten keine Aussage.
