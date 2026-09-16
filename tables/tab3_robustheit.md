# Tab. 3 — Robustheitsprüfungen

Der Gruppenvergleich aus Tab. 2 wird unter veränderten Spezifikationen
wiederholt. Einheit bleibt das **Länder-Periodenmittel**; Test ist der
zweiseitige Mann-Whitney-U, Effektgröße Cliff's δ (negativ = Sahel niedriger).

## Kernkontrast: mit und ohne Ölstaaten in der Vergleichsgruppe

Die Vergleichsgruppe enthält je Periode bis zu sechs Ölstaaten (NGA, AGO,
COG, GAB, GNQ, SSD; Südsudan erreicht nur 2008–2014 die Mindestzahl Jahre).
Werden sie entfernt, während die Sahel-Gruppe unverändert bleibt, schrumpft
der Gruppenabstand erheblich. Das ist kein Nebenergebnis, sondern die
zentrale Einschränkung des Regionsvergleichs.

| Periode | Median Sahel | Median Vergleich (mit Öl) | δ | p | Median Vergleich (ohne Öl) | δ | p |
|---|---|---|---|---|---|---|---|
| 2000–2007 | 0,10 | 0,51 | -0,42 | 0,227 | 0,14 | -0,27 | 0,477 |
| 2008–2014 | 0,21 | 0,35 | -0,43 | 0,197 | 0,15 | -0,22 | 0,554 |
| 2015–2021 | 0,16 | 0,26 | -0,26 | 0,462 | 0,16 | -0,08 | 0,862 |

## Abschöpfung nach Rohstofftyp (alle Länder, ohne Regionsbezug)

Diese Aufschlüsselung lässt die Sahel-Zugehörigkeit außer Acht. Positives
Cliff's δ bedeutet: Länder mit Ölförderung schöpfen mehr ab.

**Diese Auswertung ist post hoc**: Sie ist im Forschungsdesign §5.6 nicht
vorgesehen und wurde nach Sichtung der Regionsergebnisse ergänzt. Die
p-Werte sind nicht für multiples Testen adjustiert (siehe unten).

Erste Abgrenzung nach der Panelspalte `oil_state` (NGA, AGO, GNQ, COG, GAB,
SSD, TCD). Diese Spalte wurde für den Robustheits-Ausschluss definiert und
ist als Öl-Kennzeichnung unvollständig:

| Periode | n Öl | Median Öl | n ohne Öl | Median ohne Öl | Cliff's δ | p |
|---|---|---|---|---|---|---|
| 2000–2007 | 6 | 0,52 | 16 | 0,12 | 0,31 | 0,294 |
| 2008–2014 | 7 | 0,74 | 19 | 0,15 | 0,74 | 0,003 |
| 2015–2021 | 6 | 0,46 | 15 | 0,14 | 0,64 | 0,023 |

Mit erweiterter Abgrenzung (zusätzlich Kamerun, Sudan und Mauretanien, die
ebenfalls Erdöl fördern):

| Periode | n Öl | Median Öl | n ohne Öl | Median ohne Öl | Cliff's δ | p |
|---|---|---|---|---|---|---|
| 2000–2007 | 9 | 0,62 | 13 | 0,11 | 0,54 | 0,038 |
| 2008–2014 | 10 | 0,66 | 16 | 0,10 | 0,76 | 0,001 |
| 2015–2021 | 9 | 0,44 | 12 | 0,10 | 0,78 | 0,003 |

Der Kontrast nach Rohstofftyp ist deskriptiv deutlicher als der nach Region
und unter beiden Abgrenzungen gleichgerichtet; mit der erweiterten
Abgrenzung fällt er stärker aus. Er hält auch der Holm-Korrektur über alle
17 in dieser Arbeit berichteten Tests stand (erweiterte Abgrenzung:
p_Holm = 0,020 für 2008–2014 und 0,038 für 2015–2021).

Einschränkungen: Die Auswertung ist post hoc, und die drei Periodentests
beruhen auf denselben wenigen Ländern — sie sind keine drei unabhängigen
Belege. Die Klassifikation nach Rohstofftyp ist eine Vereinfachung; die
Länder fördern jeweils mehrere Rohstoffe in unterschiedlichem Anteil.

## Ergebnisse je Spezifikation

| Spezifikation | Periode | n Sahel | Median Sahel | n Vergleich | Median Vergleich | p | Cliff's δ |
|---|---|---|---|---|---|---|---|
| **Haupt** — Hauptspezifikation (Sahel-Definition 5 Länder, ≥ 3 gültige Jahre) | 2000–2007 | 4 | 0,10 | 18 | 0,51 | 0,227 | -0,42 (n zu klein für Einordnung) |
|  | 2008–2014 | 4 | 0,21 | 22 | 0,35 | 0,197 | -0,43 (n zu klein für Einordnung) |
|  | 2015–2021 | 4 | 0,16 | 17 | 0,26 | 0,462 | -0,26 (n zu klein für Einordnung) |
| **a1** — Vergleichsgruppe ohne Ölstaaten (Sahel unverändert, inkl. TCD) | 2000–2007 | 4 | 0,10 | 13 | 0,14 | 0,477 | -0,27 (n zu klein für Einordnung) |
|  | 2008–2014 | 4 | 0,21 | 16 | 0,15 | 0,554 | -0,22 (n zu klein für Einordnung) |
|  | 2015–2021 | 4 | 0,16 | 12 | 0,16 | 0,862 | -0,08 (n zu klein für Einordnung) |
| **a2** — ohne Ölstaaten in beiden Gruppen (ohne TCD, Sahel n = 3) | 2000–2007 | 3 | 0,03 | 13 | 0,14 | 0,364 | -0,38 (n zu klein für Einordnung) |
|  | 2008–2014 | 3 | 0,05 | 16 | 0,15 | 0,303 | -0,42 (n zu klein für Einordnung) |
|  | 2015–2021 | 3 | 0,07 | 12 | 0,16 | 0,734 | -0,17 (n zu klein für Einordnung) |
| **b** — Sahel erweitert (+ SDN, SEN) | 2000–2007 | 6 | 0,13 | 16 | 0,51 | 0,367 | -0,27 (klein) |
|  | 2008–2014 | 6 | 0,23 | 20 | 0,35 | 0,196 | -0,37 (mittel) |
|  | 2015–2021 | 6 | 0,18 | 15 | 0,37 | 0,381 | -0,27 (klein) |
| **c** — 5- statt 3-Jahres-Glättung | 2000–2007 | 4 | 0,11 | 18 | 0,51 | 0,262 | -0,39 (n zu klein für Einordnung) |
|  | 2008–2014 | 4 | 0,21 | 22 | 0,35 | 0,197 | -0,43 (n zu klein für Einordnung) |
|  | 2015–2021 | 4 | 0,16 | 17 | 0,26 | 0,462 | -0,26 (n zu klein für Einordnung) |
| **c0** — ungeglättete Jahreswerte (ohne Glättung) | 2000–2007 | 4 | 0,10 | 18 | 0,51 | 0,300 | -0,36 (n zu klein für Einordnung) |
|  | 2008–2014 | 4 | 0,21 | 22 | 0,25 | 0,252 | -0,39 (n zu klein für Einordnung) |
|  | 2015–2021 | 4 | 0,15 | 17 | 0,27 | 0,517 | -0,24 (n zu klein für Einordnung) |
| **f** — Quotient der Periodensummen statt Mittel der Jahresquotienten | 2000–2007 | 4 | 0,09 | 18 | 0,49 | 0,166 | -0,47 (n zu klein für Einordnung) |
|  | 2008–2014 | 4 | 0,21 | 22 | 0,26 | 0,252 | -0,39 (n zu klein für Einordnung) |
|  | 2015–2021 | 4 | 0,15 | 17 | 0,21 | 0,410 | -0,29 (n zu klein für Einordnung) |
| **g0,5** — fehlende Ressourceneinnahmen mit 0.5 % BIP imputiert | 2000–2007 | 5 | 0,10 | 39 | 0,13 | 0,366 | -0,26 (klein) |
|  | 2008–2014 | 5 | 0,11 | 40 | 0,12 | 0,766 | -0,09 (vernachlässigbar) |
|  | 2015–2021 | 5 | 0,09 | 38 | 0,12 | 0,898 | -0,04 (vernachlässigbar) |
| **g0,8** — fehlende Ressourceneinnahmen mit 0.8 % BIP imputiert | 2000–2007 | 5 | 0,12 | 39 | 0,18 | 0,311 | -0,29 (klein) |
|  | 2008–2014 | 5 | 0,13 | 40 | 0,15 | 0,314 | -0,29 (klein) |
|  | 2015–2021 | 5 | 0,12 | 38 | 0,17 | 0,672 | -0,13 (vernachlässigbar) |
| **d** — ohne geflaggte Länderjahre (Capture Ratio > 1,5) | 2000–2007 | 4 | 0,10 | 16 | 0,37 | 0,335 | -0,34 (n zu klein für Einordnung) |
|  | 2008–2014 | 4 | 0,21 | 19 | 0,17 | 0,324 | -0,34 (n zu klein für Einordnung) |
|  | 2015–2021 | 4 | 0,16 | 17 | 0,26 | 0,462 | -0,26 (n zu klein für Einordnung) |
| **e** — mindestens 5 statt 3 gültige Jahre je Periode | 2000–2007 | 3 | 0,03 | 14 | 0,37 | 0,362 | -0,38 (n zu klein für Einordnung) |
|  | 2008–2014 | 3 | 0,05 | 17 | 0,47 | 0,118 | -0,61 (n zu klein für Einordnung) |
|  | 2015–2021 | 4 | 0,16 | 17 | 0,26 | 0,462 | -0,26 (n zu klein für Einordnung) |

## Vorzeichenstabilität der Effektgröße

Entscheidend ist nicht, ob p unter 0,05 bleibt — bei vier Sahel-Ländern ist
die Teststärke dafür zu gering —, sondern ob die **Richtung** des Unterschieds
erhalten bleibt. Zu beachten: Die Zellen sind **keine unabhängigen
Replikationen**, da sie auf denselben vier Sahel-Ländern beruhen. In Variante
(a1) fällt die Effektgröße 2015–2021 auf −0,08 und ist damit
vernachlässigbar klein; als Bestätigung einer Richtung trägt sie kaum.

| Variante | Beschreibung | 2000–2007 | 2008–2014 | 2015–2021 |
|---|---|---|---|---|
| a1 | Vergleichsgruppe ohne Ölstaaten (Sahel unverändert, inkl. TCD) | ja | ja | ja |
| a2 | ohne Ölstaaten in beiden Gruppen (ohne TCD, Sahel n = 3) | ja | ja | ja |
| b | Sahel erweitert (+ SDN, SEN) | ja | ja | ja |
| c | 5- statt 3-Jahres-Glättung | ja | ja | ja |
| c0 | ungeglättete Jahreswerte (ohne Glättung) | ja | ja | ja |
| f | Quotient der Periodensummen statt Mittel der Jahresquotienten | ja | ja | ja |
| g0,5 | fehlende Ressourceneinnahmen mit 0.5 % BIP imputiert | ja | ja | ja |
| g0,8 | fehlende Ressourceneinnahmen mit 0.8 % BIP imputiert | ja | ja | ja |
| d | ohne geflaggte Länderjahre (Capture Ratio > 1,5) | ja | ja | ja |
| e | mindestens 5 statt 3 gültige Jahre je Periode | ja | ja | ja |

## Einordnung

- Variante **(a1)** hält die Sahel-Gruppe konstant und entfernt die Ölstaaten
  nur aus der Vergleichsgruppe. Sie isoliert damit den Beitrag des
  Rohstofftyps zum Gruppenabstand. Das Vorzeichen bleibt negativ, die
  Effektgröße fällt jedoch deutlich — der sichtbare Abstand zwischen Sahel und
  übrigem Subsahara-Afrika erklärt sich weitgehend daraus, dass die
  Vergleichsgruppe Ölstaaten enthält.
- Variante **(a2)** entfernt die Ölstaaten aus beiden Gruppen und damit auch
  Tschad aus dem Sahel. Die Sahel-Gruppe schrumpft auf drei Länder;
  Unterschiede sind hier teils Folge der kleineren Gruppe.
- Variante **(c)** glättet stärker und reduziert Timing-Rauschen zwischen
  Rentenanfall und Zahlungseingang, verliert aber Randjahre und damit
  Beobachtungen in den Außenperioden.
- Variante **(c0)** rechnet ohne Glättung und zeigt, dass der Befund nicht
  durch die Glättung entsteht. Bis 14:20 war diese Variante versehentlich
  die Hauptspezifikation; die Umstellung auf die im Design vorgesehene
  3-Jahres-Glättung verstärkt den Befund leicht.
- Variante **(d)** prüft, ob der Befund von einzelnen Länderjahren mit
  Capture Ratio > 1,5 getragen wird. Diese Werte sind nicht unplausibel
  (Nachzahlungen, Preisverfall bei nachlaufenden Zahlungen), verzerren
  Mittelwerte aber stark. Zu beachten: Botswana verliert dadurch alle 14
  gültigen Jahre und fällt vollständig aus der Vergleichsgruppe; (d) ist
  faktisch ein Länderausschluss, keine bloße Ausreißerbereinigung.
- Variante **(f)** bildet die Capture Ratio als Quotient der Periodensummen.
  Das gewichtet Jahre mit kleinem Nenner nicht über, ist inhaltlich näher an
  der Forschungsfrage und stützt den Befund.
- Variante **(g)** ist die einzige, die den Befund faktisch entkräftet: Unter
  Imputation der fehlenden Ressourceneinnahmen mit 0,5 % BIP sinkt die
  Effektgröße auf −0,26/−0,09/−0,04, unter 0,8 % BIP schwächer. Plausibel,
  weil die Ausfallquote asymmetrisch ist (Sahel 25 %, Vergleichsgruppe 56 %
  fehlende Werte bei Renten ≥ 1 % BIP). Das ist die stärkste Einschränkung
  dieser Arbeit, nicht eine Variante unter vielen.
- **Multiples Testen:** Diese Arbeit berichtet 17 Signifikanztests. Die
  p-Werte in dieser Tabelle sind nicht adjustiert; nach Holm-Korrektur über
  alle berichteten Tests bleibt kein Regionstest signifikant — er ist es
  auch unadjustiert nicht.
- Alle Befunde sind **Assoziationen**, keine Kausalität. Die Robustheitsprüfung
  sagt etwas über die Stabilität des deskriptiven Musters, nicht über dessen
  Ursachen.

Quelle: World Bank WDI, UNU-WIDER GRD 2025; eigene Berechnung.
Erzeugt von `src/06_robustheit.py`.
