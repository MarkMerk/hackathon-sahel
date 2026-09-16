# Bildunterschriften

## Mark (Abb. 1-3)

**Abb. 1.** Rohstoffrenten (% des BIP) im Jahr 2021 je Land der Region
Subsahara-Afrika, sortiert nach Rentenhöhe. Die Sahel-Kernländer (Mali,
Burkina Faso, Niger, Tschad, Mauretanien) sind farblich hervorgehoben und
mit ISO-3-Code beschriftet. Dargestellt sind alle Länder mit vorhandenem
Wert für 2021 (n = 46 Länder, darunter 5 Sahel-Kernländer).
Quelle: World Bank WDI, UNU-WIDER GRD 2025; eigene Berechnung und
Darstellung. Erzeugt von `src/fig1_renten_2021.py`.

**Abb. 2.** Staatliche Abschöpfungsquote (Capture Ratio, zentriertes
3-Jahres-Mittel) 2000–2021: je eine Linie für die Sahel-Kernländer (Mali,
Burkina Faso, Niger, Tschad, Mauretanien) gegenüber Median und
Interquartilsband (Q1–Q3) der übrigen Länder der World-Bank-Region
Subsahara-Afrika (ohne Sudan und Senegal). Fehlende Jahre je Sahel-Land
(z. B. Mali nur 2013–2016; Mauretanien mit Lücke 2008–2011) sind als
Datenlücke dargestellt und nicht überbrückt. Die gestrichelte Hilfslinie bei
1,0 markiert die vollständige Abschöpfung der Rohstoffrenten im
Staatshaushalt. n Vergleichsgruppe = 21 Länder / 333 Länderjahre; n
Sahel-Kernländer = 5 Länder / 83 Länderjahre.
Quelle: World Bank WDI, UNU-WIDER GRD 2025; eigene Berechnung und
Darstellung. Erzeugt von `src/fig2_zeitreihen.py`.

**Abb. 3.** Streudiagramm der Rohstoffrenten (WDI, % des BIP) gegen die
staatlichen Ressourceneinnahmen (GRD Total Resource Revenue, % des BIP) je
Land-Periodenmittel (2000–2007, 2008–2014, 2015–2021; Periode durch
Markerform unterschieden). Die gestrichelte 45-Grad-Linie markiert die
vollständige Abschöpfung der Rente im Staatshaushalt; der senkrechte Abstand
eines Punkts unter der Linie zeigt den nicht im Haushalt ankommenden Anteil
der Rente. Die Sahel-Kernländer (Mali, Burkina Faso, Niger, Tschad,
Mauretanien) sind farblich hervorgehoben und mit ISO-3-Code beschriftet und
liegen in allen 12 dargestellten Länder-Perioden unterhalb der 45-Grad-Linie.
Berücksichtigt sind Länder-Perioden mit mindestens drei gültigen Jahren für
beide Größen (n = 26 Länder, 70 Länder-Perioden-Punkte, davon 4
Sahel-Kernländer mit je drei Perioden = 12 Punkten; Mali ist wegen fehlender
GRD-Werte für ≥ 3 Jahre je Periode nicht enthalten). Die Achsen sind aus
Lesbarkeitsgründen auf 45 % des BIP begrenzt; zwei Punkte mit extrem hohen
Renten (Kongo-Brazzaville
und Äquatorialguinea, jeweils Periode 2000–2007) liegen außerhalb des
dargestellten Bereichs und werden im Diagramm nicht gezeigt, aber nicht aus
den Daten gelöscht.
Quelle: World Bank WDI, UNU-WIDER GRD 2025; eigene Berechnung und
Darstellung. Erzeugt von `src/fig3_streudiagramm.py`.

## Philip (Abb. 4–5)

**Abb. 4.** Staatliche Abschöpfungsquote (Capture Ratio) nach Periode und
Ländergruppe. Boxplots der Länder-Periodenmittel; überlagerte Punkte zeigen die
einzelnen Länder. Die Capture Ratio ist einheitenlos und gibt den Anteil der
Rohstoffrenten an, der als staatliche Ressourceneinnahme im Haushalt ankommt;
die gepunktete Linie bei 1,0 markiert die vollständige Abschöpfung.
Berücksichtigt sind Länder mit mindestens drei gültigen Jahren je Periode
(n je Gruppe in der Abbildung angegeben); Mali erreicht diese Schwelle in
keiner Periode. Die Achse endet bei 1,6; vier Länder-Periodenmittel der
Vergleichsgruppe liegen darüber und sind als Dreieck am oberen Rand
markiert — sie gehen in Median, Interquartilsabstand und Test vollständig ein.
Quelle: World Bank WDI, UNU-WIDER GRD 2025; eigene Berechnung und
Darstellung. Erzeugt von `src/04_gruppenvergleich.py`.

**Abb. 5.** Staatliche Abschöpfungsquote und menschliche Entwicklung
(Länder-Periodenmittel). Streudiagramme je Periode mit Capture Ratio auf der
Horizontalen und dem HDI auf der Vertikalen; die Sahel-Staaten sind
hervorgehoben und mit ISO-3-Code beschriftet. Angegeben sind die
Spearman-Rangkorrelation und die Fallzahl je Periode. Die Achse endet bei
1,6; vier Werte liegen darüber und sind als Pfeil am rechten Rand markiert —
sie gehen in die Korrelationen vollständig ein. Die Darstellung zeigt einen
Zusammenhang *zwischen* Ländern; innerhalb der Länder über die Zeit findet
sich keiner (vgl. Tab. 2b). Es handelt sich um eine **Assoziation**, die
keine Aussage über die Wirkungsrichtung erlaubt.
Quelle: World Bank WDI, UNU-WIDER GRD 2025, UNDP HDI; eigene Berechnung
und Darstellung. Erzeugt von `src/05_zusammenhang_hdi.py`.

