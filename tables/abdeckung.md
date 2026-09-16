# Datenabdeckung je Land (2000–2021)

Erzeugt von `src/02_abdeckung.py` aus `data/processed/panel.csv`. Gezählt werden Jahre mit vorhandenem Wert; `*` markiert eine nicht lückenlose Spanne. „Jahre beides“ = Jahre mit Renten **und** Ressourceneinnahmen; „Jahre Capture Ratio“ zusätzlich eingeschränkt auf Renten ≥ 1 % BIP.

## Entscheidung GRD vs. Plan B

Kriterium (`docs/Forschungsdesign.md` §5.7): mindestens **3** der fünf Sahel-Kernländer mit mindestens **10** Jahren Renten *und* GRD-Ressourceneinnahmen.

Erfüllt: **4 von 5** (NER, BFA, MRT, TCD).

**Ergebnis: Hauptplan — Analyse auf Basis des GRD.**

## Abdeckung je Land

| Land | ISO3 | Gruppe | Jahre Renten | Jahre Ressourceneinnahmen | Jahre beides | Jahre Capture Ratio | Jahre HDI | Spanne Renten | Spanne Einnahmen |
|---|---|---|---|---|---|---|---|---|---|
| Niger | NER | Sahel | 22 | 22 | 22 | 22 | 22 | 2000–2021 | 2000–2021 |
| Burkina Faso | BFA | Sahel | 22 | 21 | 21 | 21 | 17 | 2000–2021 | 2000–2020 |
| Mauritania | MRT | Sahel | 22 | 18 | 18 | 18 | 22 | 2000–2021 | 2000–2021* |
| Chad | TCD | Sahel | 22 | 18 | 18 | 18 | 22 | 2000–2021 | 2004–2021 |
| Mali | MLI | Sahel | 22 | 4 | 4 | 4 | 22 | 2000–2021 | 2013–2016 |
| Sudan | SDN | Sahel (erw.) | 22 | 21 | 21 | 21 | 14 | 2000–2021 | 2000–2020 |
| Senegal | SEN | Sahel (erw.) | 22 | 17 | 17 | 17 | 22 | 2000–2021 | 2005–2021 |
| Angola | AGO | übriges SSA | 22 | 22 | 22 | 22 | 22 | 2000–2021 | 2000–2021 |
| Botswana | BWA | übriges SSA | 22 | 22 | 22 | 14 | 22 | 2000–2021 | 2000–2021 |
| Cameroon | CMR | übriges SSA | 22 | 22 | 22 | 22 | 22 | 2000–2021 | 2000–2021 |
| Congo, Rep. | COG | übriges SSA | 22 | 22 | 22 | 22 | 22 | 2000–2021 | 2000–2021 |
| Gabon | GAB | übriges SSA | 22 | 22 | 22 | 22 | 22 | 2000–2021 | 2000–2021 |
| Ghana | GHA | übriges SSA | 22 | 22 | 22 | 22 | 22 | 2000–2021 | 2000–2021 |
| Guinea | GIN | übriges SSA | 22 | 22 | 22 | 22 | 22 | 2000–2021 | 2000–2021 |
| Namibia | NAM | übriges SSA | 22 | 22 | 22 | 17 | 22 | 2000–2021 | 2000–2021 |
| Nigeria | NGA | übriges SSA | 22 | 22 | 22 | 22 | 22 | 2000–2021 | 2000–2021 |
| Sierra Leone | SLE | übriges SSA | 22 | 22 | 22 | 22 | 22 | 2000–2021 | 2000–2021 |
| Zambia | ZMB | übriges SSA | 22 | 22 | 22 | 22 | 22 | 2000–2021 | 2000–2021 |
| Madagascar | MDG | übriges SSA | 22 | 21 | 21 | 21 | 22 | 2000–2021 | 2000–2020 |
| Uganda | UGA | übriges SSA | 22 | 19 | 19 | 19 | 22 | 2000–2021 | 2003–2021 |
| Equatorial Guinea | GNQ | übriges SSA | 18 | 22 | 18 | 18 | 22 | 2000–2021* | 2000–2021 |
| Sao Tome and Principe | STP | übriges SSA | 21 | 12 | 12 | 12 | 17 | 2001–2021 | 2005–2021* |
| Cote d'Ivoire | CIV | übriges SSA | 22 | 11 | 11 | 11 | 22 | 2000–2021 | 2000–2010 |
| Congo, Dem. Rep. | COD | übriges SSA | 22 | 11 | 11 | 11 | 22 | 2000–2021 | 2010–2021* |
| Liberia | LBR | übriges SSA | 22 | 4 | 4 | 4 | 22 | 2000–2021 | 2012–2015 |
| South Sudan | SSD | übriges SSA | 8 | 10 | 4 | 4 | 12 | 2008–2015 | 2012–2021 |
| Zimbabwe | ZWE | übriges SSA | 22 | 3 | 3 | 3 | 22 | 2000–2021 | 2011–2013 |
| Togo | TGO | übriges SSA | 22 | 2 | 2 | 2 | 22 | 2000–2021 | 2000–2001 |
| Burundi | BDI | übriges SSA | 22 | 0 | 0 | 0 | 22 | 2000–2021 | — |
| Benin | BEN | übriges SSA | 22 | 0 | 0 | 0 | 22 | 2000–2021 | — |
| Central African Republic | CAF | übriges SSA | 22 | 0 | 0 | 0 | 21 | 2000–2021 | — |
| Comoros | COM | übriges SSA | 22 | 0 | 0 | 0 | 22 | 2000–2021 | — |
| Cabo Verde | CPV | übriges SSA | 22 | 0 | 0 | 0 | 22 | 2000–2021 | — |
| Eritrea | ERI | übriges SSA | 12 | 0 | 0 | 0 | 17 | 2000–2011 | — |
| Ethiopia | ETH | übriges SSA | 22 | 0 | 0 | 0 | 22 | 2000–2021 | — |
| Gambia, The | GMB | übriges SSA | 22 | 0 | 0 | 0 | 22 | 2000–2021 | — |
| Guinea-Bissau | GNB | übriges SSA | 22 | 0 | 0 | 0 | 17 | 2000–2021 | — |
| Kenya | KEN | übriges SSA | 22 | 0 | 0 | 0 | 22 | 2000–2021 | — |
| Lesotho | LSO | übriges SSA | 22 | 0 | 0 | 0 | 22 | 2000–2021 | — |
| Mozambique | MOZ | übriges SSA | 22 | 0 | 0 | 0 | 22 | 2000–2021 | — |
| Mauritius | MUS | übriges SSA | 22 | 0 | 0 | 0 | 22 | 2000–2021 | — |
| Malawi | MWI | übriges SSA | 22 | 0 | 0 | 0 | 22 | 2000–2021 | — |
| Rwanda | RWA | übriges SSA | 22 | 0 | 0 | 0 | 22 | 2000–2021 | — |
| Somalia, Fed. Rep. | SOM | übriges SSA | 9 | 0 | 0 | 0 | 0 | 2013–2021 | — |
| Eswatini | SWZ | übriges SSA | 22 | 0 | 0 | 0 | 22 | 2000–2021 | — |
| Seychelles | SYC | übriges SSA | 22 | 0 | 0 | 0 | 12 | 2000–2021 | — |
| Tanzania | TZA | übriges SSA | 22 | 0 | 0 | 0 | 22 | 2000–2021 | — |
| South Africa | ZAF | übriges SSA | 22 | 0 | 0 | 0 | 22 | 2000–2021 | — |

## Zusammenfassung nach Gruppen

| Gruppe | Länder | Ø Jahre Renten | Ø Jahre Einnahmen | Ø Jahre beides |
|---|---|---|---|---|
| Sahel | 5 | 22.0 | 16.6 | 16.6 |
| Sahel (erw.) | 2 | 22.0 | 19.0 | 19.0 |
| übriges SSA | 41 | 21.0 | 8.7 | 8.5 |

Quelle: World Bank WDI, ICTD/UNU-WIDER GRD 2023, UNDP HDR; eigene Berechnung.
