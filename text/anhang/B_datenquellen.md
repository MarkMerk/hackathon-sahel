# Anhang B — Datenquellen, Abfragen und Abrufdaten

Alle Rohdaten wurden am **16.09.2026** bezogen. Die Dateinamen entsprechen den Ablagen in `data/raw/`; die Verarbeitung erfolgt in `src/01_laden.py` (Anhang A).

## B.1 Übersicht

| # | Datensatz | Herausgeber | Version / Stand | Bezugsweg | Datei in `data/raw/` |
|---|---|---|---|---|---|
| 1 | Rohstoffrenten gesamt (`NY.GDP.TOTL.RT.ZS`) | Weltbank, World Development Indicators | Stand 13.07.2026 | API-Download (CSV im ZIP) | `wdi_rents_2026-09-16.csv` |
| 2 | Ländermetadaten mit Regionszuordnung | Weltbank, World Development Indicators | wie 1 | im selben ZIP enthalten | `wdi_country_meta_2026-09-16.csv` |
| 3 | Bruttoinlandsprodukt pro Kopf, konstante US-Dollar 2015 (`NY.GDP.PCAP.KD`) | Weltbank, World Development Indicators | Stand 13.07.2026 | API-Download | `wdi_gdppc_2026-09-16.csv` |
| 4 | Zugang zu Elektrizität, % der Bevölkerung (`EG.ELC.ACCS.ZS`) | Weltbank, World Development Indicators | Stand 13.07.2026 | API-Download | `wdi_elec_2026-09-16.csv` |
| 5 | Government Revenue Dataset, Blatt *Merged* | UNU-WIDER | Version 2025 | Registrierung auf der Projektseite | `grd_2025_2026-09-16.xlsx` |
| 6 | GRD User Guide | UNU-WIDER | Version 2025 | wie 5 | `grd_user_guide_2025.pdf` |
| 7 | Composite indices, vollständige Zeitreihe (HDI) | UNDP, Human Development Report | HDR 2025 | direkter CSV-Download | `hdr_composite_2026-09-16.csv` |

## B.2 Bezugsadressen

**Weltbank (Nr. 1–4).** Abgerufen über die Download-Schnittstelle der World Development Indicators nach dem Muster

```
https://api.worldbank.org/v2/country/all/indicator/<INDIKATOR>?downloadformat=csv
```

mit `<INDIKATOR>` gleich `NY.GDP.TOTL.RT.ZS`, `NY.GDP.PCAP.KD` beziehungsweise `EG.ELC.ACCS.ZS`. Jedes Archiv enthält neben der Indikatordatei eine Metadatendatei mit der Regionszuordnung; verwendet wurde die aus dem Archiv zu Nr. 1. Die Indikatordateien führen vier Kopfzeilen vor der eigentlichen Tabelle und liegen im Breitformat mit Jahren als Spalten vor.

**UNU-WIDER Government Revenue Dataset (Nr. 5–6).** Bezogen über `https://www.wider.unu.edu/database/government-revenue-dataset` nach Registrierung. Verwendet wurde die Kerndatei `UNUWIDERGRD_2025.xlsx`, in der Zentral- und Gesamtstaatsebene zusammengeführt sind; die getrennten Dateien *Central* und *General* sowie die Datei *Full* mit den ursprünglichen Formeln wurden nicht benötigt.

**UNDP (Nr. 7).** Bezogen über `https://hdr.undp.org/sites/default/files/2025_HDR/HDR25_Composite_indices_complete_time_series.csv`. Diese Fassung ist aktueller als die zum Planungszeitpunkt vorgesehene Ausgabe HDR 2023/24.

## B.3 Zitation der Datensätze

> UNU-WIDER. (2025). *UNU-WIDER Government Revenue Dataset. Version 2025*. Helsinki: UNU-WIDER. https://doi.org/10.35188/UNU-WIDER/GRD-2025

Die Herausgeberschaft hat sich gegenüber früheren Ausgaben geändert: Das International Centre for Tax and Development wird in der Zitation der Version 2025 nicht mehr geführt. In der Planungsphase dieser Arbeit war noch von der Version 2023 ausgegangen worden; die Angabe wurde nach Prüfung der Projektseite korrigiert.

Die Indikatoren der Weltbank werden als World Bank (2026), *World Development Indicators*, zitiert, der Index der menschlichen Entwicklung als UNDP (2025), *Human Development Report*.

## B.4 Hinweise zur Struktur und Aufbereitung

Drei Eigenschaften der Rohdaten waren für die Aufbereitung erheblich und sind in `src/01_laden.py` dokumentiert.

**Maßstab der GRD-Werte.** Die Einnahmevariablen des Government Revenue Dataset liegen als Anteil am Bruttoinlandsprodukt vor, nicht als Prozentwert: Saudi-Arabien erreicht dort in der Spitze 0,50, was fünfzig Prozent des Bruttoinlandsprodukts entspricht. Für das Panel werden die Werte mit 100 multipliziert, damit Zähler und Nenner der Abschöpfungsquote dieselbe Einheit tragen. Ohne diese Umrechnung fiele die Quote um den Faktor 100 zu niedrig aus.

**Aufbau der GRD-Datei.** Die Datentabelle steht im Blatt *Merged*. Über der Kopfzeile befinden sich zwei weitere Zeilen mit Unterkategorien, die beim Einlesen übersprungen werden. Die Regierungsebene ist in der Spalte `General (=1 if General)` vermerkt. Liegen zu einem Land und Jahr Werte für beide Ebenen vor, verwendet die Aufbereitung die Gesamtstaatsebene und weicht nur ersatzweise auf die Zentralstaatsebene aus. Für die Sahel-Länder enthält der Datensatz im Untersuchungszeitraum ausschließlich Werte der Zentralregierung.

**Zeichenkodierung der HDR-Datei.** Die Datei des Human Development Report ist nicht UTF-8-kodiert; Ländernamen mit diakritischen Zeichen führen beim Einlesen zu einem Fehler. Die Aufbereitung versucht daher mehrere Kodierungen nacheinander und weist die verwendete in der Konsolenausgabe aus.

## B.5 Weitergabe und Lizenz

Die Dateien der Weltbank und des UNDP sind frei verfügbar und im Repositorium (<https://github.com/MarkMerk/hackathon-sahel>) abgelegt. Das Government Revenue Dataset wird aus Rücksicht auf die Nutzungsbedingungen von UNU-WIDER **nicht** mit weitergegeben und ist in `.gitignore` ausgenommen; es ist nach kostenloser Registrierung unmittelbar beziehbar. Zur Reproduktion der Ergebnisse genügt es, die Datei unter dem in B.1 genannten Namen in `data/raw/` abzulegen und die Skripte in der Reihenfolge aus Anhang A auszuführen.

## B.6 Anmerkung zum Zugriffsweg

Die Vorplanung war davon ausgegangen, dass die Schnittstellen der Weltbank und von UNU-WIDER nicht erreichbar sind, da Zugriffe aus der zunächst genutzten Arbeitsumgebung blockiert wurden. Von den Arbeitsrechnern aus antwortete die Schnittstelle der Weltbank regulär, sodass die Positionen 1 bis 4 und 7 automatisiert bezogen werden konnten. Die Seiten von UNU-WIDER beantworten direkte Dateianfragen mit einer Zugriffsverweigerung; Position 5 und 6 wurden daher wie vorgesehen über das Registrierungsformular geladen.
