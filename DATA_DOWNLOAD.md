# Manuelle Downloads (im Browser, dann nach data/raw/)

Dateinamen mit Datum, z. B. `wdi_rents_2026-09-16.csv`. Abrufdatum und URL zusätzlich in `text/anhang/B_datenquellen.md` eintragen.

| # | Datensatz | Wo | Was genau | Ablegen als |
|---|---|---|---|---|
| 1 | WDI Rohstoffrenten | https://api.worldbank.org/v2/country/all/indicator/NY.GDP.TOTL.RT.ZS?downloadformat=csv | ZIP entpacken, `API_NY.GDP.TOTL.RT.ZS_*.csv` + `Metadata_Country_*.csv` (enthält Region → SSA-Filter) | `wdi_rents_<datum>.csv`, `wdi_country_meta_<datum>.csv` |
| 2 | WDI BIP p. c. | https://api.worldbank.org/v2/country/all/indicator/NY.GDP.PCAP.KD?downloadformat=csv | ZIP entpacken | `wdi_gdppc_<datum>.csv` |
| 3 | WDI Stromzugang | https://api.worldbank.org/v2/country/all/indicator/EG.ELC.ACCS.ZS?downloadformat=csv | ZIP entpacken | `wdi_elec_<datum>.csv` |
| 4 | ICTD/UNU-WIDER GRD | https://www2.wider.unu.edu/content/grd-data-download | Formular ausfüllen, neueste Version (Excel oder Stata), „Merged“-Datei | `grd_<version>_<datum>.xlsx` / `.dta` |
| 5 | UNDP HDI | https://hdr.undp.org/data-center/documentation-and-downloads | „All composite indices and components time series“ (CSV) | `hdr_composite_<datum>.csv` |
| 6 | (Plan B) EITI Summary Data | https://eiti.org/open-data | Länder MLI, BFA, TCD, MRT, SEN (NER falls vorhanden) | `eiti_<land>_<datum>.xlsx` |

Nach dem Download in Claude Code: Mark: Schritt 2–3 aus `sessions/MARK.md` (Subagent `daten-pruefer`, dann `src/01_laden.py` und `src/02_abdeckung.py`).
**Entscheidungspunkt:** Haben ≥ 3 Sahel-Länder ≥ 10 Jahre mit GRD Resource Revenue *und* Renten? Wenn nein → EITI als Zähler (Plan B).

**Hinweis GRD:** Die GRD-Datei wird vorsorglich nicht ins Repository gepusht (`.gitignore`). Philip und Leon brauchen sie nicht direkt — sie arbeiten mit `data/processed/panel.csv`.
