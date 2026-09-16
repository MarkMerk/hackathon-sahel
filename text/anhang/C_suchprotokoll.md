# Anhang C — Suchprotokoll Literaturrecherche

Alle Recherchen am 16.09.2026 durch Leon, unterstützt von Claude Code (Modell Opus 5). Werkzeuge: Websuche
(Suchmaschine über Claude Code), gezielter Abruf von Verlagsseiten sowie die **Crossref-REST-API**
(`api.crossref.org`) als maßgebliche DOI-Registrierungsstelle. Grundregel des Projekts: In
`text/quellen.bib` steht ausschließlich, was über DOI oder stabile URL tatsächlich aufgerufen und in den
Metadaten bestätigt wurde. Alles andere ist unten als **nicht verifiziert** oder **verworfen** vermerkt.

**Hinweis zur Prüfmethode:** Verlagsseiten (Oxford Academic, AEA, Elsevier/ScienceDirect) liefern über die
verfügbaren Werkzeuge keine Metadaten aus (Paywall, HTTP 403, JavaScript-Weiterleitung). Die
bibliografischen Angaben wurden daher über die Crossref-API des jeweiligen DOI abgerufen; Crossref ist die
Registrierungsstelle, bei der die Verlage ihre Metadaten selbst hinterlegen. Jede unten mit „Crossref
bestätigt" markierte Angabe (Autor, Titel, Journal, Jahr, Band, Heft, Seiten) stammt aus dieser Abfrage,
nicht aus dem Vorschlag eines Sprachmodells.

## 1. Rentierstaat

| Feld | Inhalt |
|---|---|
| Datum/Zeit | 16.09.2026, 12:25 |
| Werkzeug | Websuche; Verlagsseite Routledge; Crossref-API |
| Suchbegriffe | `Beblawi Luciani rentier state theory Arab oil states`; `Beblawi Luciani The Rentier State` (Crossref) |
| Treffer | 10 Webtreffer, 3 Crossref-Treffer |

- **Übernommen:** Beblawi & Luciani (Hrsg.), *The Rentier State*, Routledge. Crossref bestätigt die
  Neuausgabe 2015 mit DOI `10.4324/9781315684864`; die Verlagsseite bestätigt Erstveröffentlichung **1987**,
  Reihe *Routledge Library Editions: Politics of the Middle East*. Wir zitieren die Erstausgabe 1987 und
  führen die DOI der Neuausgabe als Nachweis.
- **Nebenbefund, protokolliert:** Die Websuche nennt Hossein **Mahdavy (1970)** als eigentlichen Urheber des
  Begriffs „rentier state". Sachlich plausibel und für die Theorie einschlägig, aber **nicht verifiziert** —
  kein DOI gefunden (Kapitel in einem Sammelband von 1970). Nur zitieren, wenn Leon die Printquelle einsehen
  kann; sonst über Beblawi/Luciani referieren.
- **Verworfen:** Wikipedia-Artikel „Rentier state", ResearchGate- und Academia-Volltexte, SWP-/LSE-Papiere zu
  den Golfstaaten — keine zitierfähige Primärliteratur bzw. nicht auf unsere Fragestellung bezogen.

## 2. Resource Curse (Klassiker)

| Feld | Inhalt |
|---|---|
| Datum/Zeit | 16.09.2026, 12:26 |
| Werkzeug | Websuche; Crossref-API |
| Suchbegriffe | `Sachs Warner natural resource abundance economic growth curse`; `van der Ploeg Natural Resources Curse or Blessing Journal of Economic Literature 2011` |
| Treffer | 20 Webtreffer, davon 2 in die .bib |

- **Übernommen:** Sachs & Warner (2001), *The curse of natural resources*, European Economic Review 45(4–6),
  827–838. Crossref bestätigt Autoren, Titel, Band, Heft, Seiten; DOI `10.1016/S0014-2921(01)00125-8`.
- **Übernommen:** van der Ploeg (2011), *Natural Resources: Curse or Blessing?*, Journal of Economic
  Literature 49(2), 366–420. Crossref bestätigt alle Angaben; DOI `10.1257/jel.49.2.366`.
- **Protokolliert (wichtig für den Forschungsstand):** Die Websuche weist ausdrücklich darauf hin, dass das
  Sachs-Warner-Ergebnis **nicht robust** ist, wenn Ressourcenreichtum über Reserven oder Produktion statt
  über Exportanteile gemessen wird. Diese Einschränkung stützt unsere Operationalisierung über Renten statt
  Exporte und gehört in Abschnitt 3.
- **Verworfen:** NBER Working Paper 5398 und SSRN-Fassung (Sachs/Warner 1995) — Vorstufe des publizierten
  Aufsatzes, wird höchstens erwähnt, nicht zitiert. Kritische Sekundärtexte auf Academia.edu — nicht
  begutachtet.

## 3. Institutionen und Ressourcenreichtum

| Feld | Inhalt |
|---|---|
| Datum/Zeit | 16.09.2026, 12:27 |
| Werkzeug | Websuche; Crossref-API |
| Suchbegriffe | `Mehlum Moene Torvik institutions and the resource curse Economic Journal 2006` |
| Treffer | 9 Webtreffer; 2 Aufsätze verifiziert |

- **Übernommen:** Mehlum, Moene & Torvik (2006), *Institutions and the Resource Curse*, The Economic Journal
  116(508), 1–20. Crossref bestätigt alle Angaben; DOI `10.1111/j.1468-0297.2006.01045.x`.
- **Übernommen:** Mehlum, Moene & Torvik (2006), *Cursed by Resources or Institutions?*, The World Economy
  29(8), 1117–1131. Crossref bestätigt; DOI `10.1111/j.1467-9701.2006.00808.x`.
- **Fremdfehler, korrigiert:** Eine Trefferseite (scirp.org) gibt die Quelle als „The Economic Journal, **91**,
  1–20" an. Crossref bestätigt Band **116**, Heft 508. Wir verwenden die Crossref-Angabe. Der Fall zeigt,
  dass auch Zitationssammlungen Dritter fehlerhaft sind, nicht nur Sprachmodelle.
- **Kernaussage für die Theorie:** Mehr Rohstoffe senken das Aggregateinkommen bei „grabber friendly"
  Institutionen und erhöhen es bei „producer friendly" Institutionen — der institutionelle Rahmen
  entscheidet. Das ist die theoretische Begründung dafür, die **Abschöpfungsquote** und nicht die
  Rentenhöhe zu messen.

## 4. Government take, fiskalische Regime und Abschöpfung

| Feld | Inhalt |
|---|---|
| Datum/Zeit | 16.09.2026, 12:28–12:34 |
| Werkzeug | Websuche; Crossref-Suche (`query.bibliographic`) |
| Suchbegriffe | `government take fiscal regime mining Africa IMF working paper`; `taxation of mining rents developing countries government revenue share`; `Crivelli Gupta resource blessing revenue curse`; `mining sector tax avoidance Sub-Saharan Africa profit shifting` |
| Treffer | 8 Webtreffer + 16 Crossref-Treffer, 3 übernommen |

- **Übernommen (zentral):** Crivelli & Gupta (2014), *Resource blessing, revenue curse? Domestic revenue
  effort in resource-rich countries*, European Journal of Political Economy 35, 88–101. Crossref bestätigt;
  DOI `10.1016/j.ejpoleco.2014.04.001`. **Direkt anschlussfähig:** untersucht die staatliche
  Einnahmeanstrengung in ressourcenreichen Ländern — dieselbe Frage, anderer Zugang als unsere Capture Ratio.
- **Übernommen:** Albertin et al. (2021), *Tax Avoidance in Sub-Saharan Africa's Mining Sector*, IMF
  Departmental Paper 2021/022. Crossref bestätigt acht Autor:innen und Abstract; DOI
  `10.5089/9781513594361.087`. Liefert den Mechanismus für eine niedrige Capture Ratio (Gewinnverlagerung)
  und die Beschreibung der Regime (Royalties, Körperschaftsteuer, staatliche Beteiligungen).
- **Übernommen:** Debonheur (2025), *Natural resource rents and non-resource tax revenue mobilization in
  selected developing countries*, Resources Policy 105, 105622. Crossref bestätigt; DOI
  `10.1016/j.resourpol.2025.105622`.
- **Nicht verifiziert:** Smith (2012), *Issues in Extractive Resource Taxation*, IMF Working Paper 2012/287 —
  von der Websuche genannt, DOI nicht geprüft. Nur nach eigener Prüfung verwenden.
- **Verworfen:** IMF Country Report Südafrika 15/244, IMF-Konferenzseite Westafrika 2018, Zambia windfall tax
  (UNU-WIDER wp-2018-51), Guj (2018) Buchkapitel — Einzelland bzw. zu eng, kein Bezug zum Sahel-Vergleich.

## 5. Illicit financial flows im Rohstoffsektor

| Feld | Inhalt |
|---|---|
| Datum/Zeit | 16.09.2026, 12:29–12:34 |
| Werkzeug | Websuche; Crossref-API |
| Suchbegriffe | `illicit financial flows mining sector Africa trade mispricing revenue loss study`; `extractive sector illicit financial flows Africa mechanisms transparency governance` |
| Treffer | 9 + 4 Crossref-Treffer, 2 übernommen |

- **Übernommen:** Nkemgha (2026), *The extractive sector and illicit financial flows in Africa: mechanisms and
  policy implications for transparency and governance*, Economics of Governance 27(1). Crossref bestätigt
  Autor, Journal, Band und Abstract; DOI `10.1007/s10101-026-00367-1`. Panel aus 27 afrikanischen Ländern
  2004–2018, System-GMM: der Rohstoffsektor treibt illegale Finanzflüsse signifikant.
- **Übernommen:** Corrigan (2017), *The effects of increased revenue transparency in the extractives sector:
  The case of the Extractive Industries Transparency Initiative*, The Extractive Industries and Society 4(4),
  779–787. Crossref bestätigt; DOI `10.1016/j.exis.2017.03.004`. Relevant für Plan B (EITI als Zähler) und
  für die Diskussion der Transparenzinstrumente.
- **Nicht verifiziert, aber inhaltlich einschlägig:** AU/ECA High Level Panel on Illicit Financial Flows
  (Mbeki-Report) mit den oft zitierten Größenordnungen (> 50 Mrd. USD pro Jahr; 409 Mrd. USD aus dem
  Rohstoffsektor 2001–2010). Graue Literatur ohne DOI, PDF über unodc.org erreichbar. **Falls im Text
  verwendet: als Bericht mit URL und Abrufdatum zitieren und die Zahl ausdrücklich als Schätzung
  kennzeichnen** — nicht als peer-reviewte Evidenz führen.
- **Verworfen:** Oxfam-Bericht, AFRODAD, Tax Justice Network Africa, Universal Journal of Finance and
  Economics — Advocacy-Literatur bzw. Zeitschrift ohne belastbare Begutachtung.

## 6. Rohstoffpolitik im Sahel nach 2020

| Feld | Inhalt |
|---|---|
| Datum/Zeit | 16.09.2026, 12:30 |
| Werkzeug | Websuche; Abruf der SWP-Publikationsseite |
| Suchbegriffe | `Mali mining code 2023 Niger SOMAIR nationalisation 2025 resource sovereignty Sahel` |
| Treffer | 9 Webtreffer, 1 übernommen |

- **Übernommen:** Tull, D. M. (2026), *Affirming Economic Sovereignty: Resource Nationalism in the Sahel*,
  Megatrends Spotlight 69, Stiftung Wissenschaft und Politik. Seite selbst aufgerufen; alle Zahlen direkt von
  dort: Malis Bergbaugesetz 2023 erhöht staatliche und lokale Beteiligung auf **bis zu 35 %** (bis 30 % Staat,
  5 % Privatsektor) und Royalties von maximal 6,5 % auf **10 %**; Burkina Fasos Kodex 2024 hebt die
  Staatsbeteiligung von 10 % auf **15 %**; Mali erzielte 2023–2025 rund **1,2 Mrd. USD** Nachzahlungen; Niger
  verstaatlichte **SOMAÏR** (Mehrheitseigner Orano). Stabile URL, kein DOI — als Institutionenbericht
  zitieren.
- **Wichtig für die Diskussion:** Tull argumentiert, die Maßnahmen hätten kurzfristig Milliarden eingebracht,
  beruhten aber auf Zwang und könnten Investitionen abschrecken, ohne der Bevölkerung zugutezukommen. Diese
  Ambivalenz gehört in Abschnitt 6, nicht nur die Einnahmeseite.
- **Verworfen:** The Arab Weekly, Modern Diplomacy, Miningmx, Africa Defense Forum, Shia Waves,
  US-Lokalzeitungen — journalistische Quellen ohne wissenschaftlichen Apparat. Einzelne Fakten (Zeitpunkte,
  Beträge) nur, wenn sie durch SWP oder eine andere Institution gedeckt sind.
- **Nicht verifiziert:** Gründung der Allianz der Sahelstaaten (AES) im September 2023 und ECOWAS-Austritt im
  Januar 2025 — mehrfach in der Websuche genannt, aber noch nicht gegen eine zitierfähige Quelle geprüft.
  Vor Verwendung in der Diskussion belegen.

## 7. Datenquellen (Nachweise für Methodik und Anhang B)

| Feld | Inhalt |
|---|---|
| Datum/Zeit | 16.09.2026, 12:31–12:38 |
| Werkzeug | Websuche; UNU-WIDER-Projektseite; Crossref-API; World-Bank-Indikator-API |
| Suchbegriffe | `Government Revenue Dataset ICTD UNU-WIDER 2023 McNabb Danquah resource revenue` |
| Treffer | 10 Webtreffer; beide Datenquellen direkt geprüft |

- **Übernommen:** UNU-WIDER Government Revenue Dataset. **Befund mit Konsequenz für das Projekt:** Die
  UNU-WIDER-Projektseite weist als aktuelle Fassung **Version 2025 (Stand November 2025)** mit DOI
  `10.35188/UNU-WIDER/GRD-2025` aus; Crossref bestätigt diesen DOI als Datensatz mit dem Titel
  „UNU-WIDER Government Revenue Dataset — Version 2025". `CLAUDE.md` und `docs/Forschungsdesign.md` nennen
  dagegen **Version 2023**. → **Für Mark vermerkt** (Commit-Nachricht und dieses Protokoll), damit Zitat und
  Abdeckungsangaben zur tatsächlich heruntergeladenen Datei passen; `src/01_laden.py` liest die Datei über
  ein Namensmuster ein und ist von der Version nicht betroffen, das Zitat in Methodik und Anhang B schon.
  Leon gibt den Befund mündlich an Mark weiter. Die Seite bestätigt außerdem, dass Einnahmen inklusive und exklusive
  Ressourceneinnahmen ausgewiesen werden — die Grundlage unseres Zählers.
- **Übernommen:** World Bank, World Development Indicators, Indikator `NY.GDP.TOTL.RT.ZS`. Über die
  World-Bank-API geprüft: offizieller Name **„Total natural resources rents (% of GDP)"**, Quelle *World
  Development Indicators*, Methodik laut *The Changing Wealth of Nations* (World Bank staff estimates). Damit
  ist der Nenner der Capture Ratio belegt.
- **Nicht verifiziert:** Die Websuche nennt „McNabb & Oppel (Oktober 2023)" als Autor:innen des
  GRD-Updates; die Crossref-Metadaten des Datensatzes führen keine Personen. Datensatz daher nach der
  Zitierempfehlung von UNU-WIDER institutionell zitieren, nicht über Personennamen. Der in der Suchanfrage
  von uns vermutete Name „Danquah" tauchte in keinem Treffer auf — **geraten, nicht bestätigt, verworfen.**

## 8. Nicht auflösbare DOI (Prüfschritt dokumentiert)

Um die Prüfkette zu testen, wurden fünf aus dem Gedächtnis des Sprachmodells plausibel erscheinende DOI
gegen Crossref abgefragt, bevor irgendetwas in die `.bib` übernommen wurde:

| Abgefragte DOI | Ergebnis |
|---|---|
| `10.1017/S0022278X10000602` | **Resource not found** — existiert nicht |
| `10.1080/00220388.2019.1618811` | **Resource not found** — existiert nicht |
| `10.1016/j.resourpol.2019.101378` | **Resource not found** — existiert nicht |
| `10.1111/dech.12405` | existiert, ist aber ein **thematisch fremder** Aufsatz (Morvaridi & Hughes) |
| `10.1016/j.worlddev.2016.03.001` | existiert, ist aber **Jakob et al., Carbon Pricing Revenues** — nicht das vermutete Werk |

**Konsequenz:** Drei von fünf geratenen DOI waren frei erfunden, zwei führten zu anderen Arbeiten als
vermutet. Keine dieser Angaben ist in `text/quellen.bib` eingegangen. Alle tatsächlich übernommenen Quellen
wurden stattdessen über eine Crossref-Titelsuche gefunden und anschließend anhand ihrer Metadaten
bestätigt. Dieser Vorgang ist zusätzlich in `logs/LOG_leon.md` unter „KI-Fehler und Korrekturen" vermerkt
und ist Material für die Reflexion.

## Zusammenfassung

| Kategorie | Anzahl |
|---|---|
| In `text/quellen.bib` übernommen (DOI/URL geprüft) | **13** (11 Literatur + 2 Datenquellen) |
| davon Klassiker (bis 2011) | 5 (Beblawi/Luciani 1987; Sachs/Warner 2001; Mehlum et al. 2006 ×2; van der Ploeg 2011) |
| davon ab 2015 | 5 (Corrigan 2017; Albertin et al. 2021; Debonheur 2025; Nkemgha 2026; Tull 2026) |
| dazwischen | 1 (Crivelli & Gupta 2014) |
| davon Datenquellen | 2 (GRD Version 2025; WDI `NY.GDP.TOTL.RT.ZS`) |
| Als „nicht verifiziert" vermerkt | 5 (Mahdavy 1970; Smith 2012; AU/ECA-Bericht; AES/ECOWAS-Daten; McNabb/Oppel) |
| Verworfen | ca. 25 Treffer (Presse, Advocacy, Preprints, Wikipedia, thematisch fremd) |

**Offen für Schritt 4:** Mahdavy (1970) und der AU/ECA-Bericht sind inhaltlich wertvoll. Entweder mit
belastbarem Nachweis nachtragen oder im Text durch bereits verifizierte Literatur ersetzen.
