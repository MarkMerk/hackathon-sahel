# Tabelle 1: Datenquellen und Indikatoren

| Indikator | Variable im Panel | Quelle | Einheit | Abdeckung |
|---|---|---|---|---|
| Rohstoffrenten | `rents_pct_gdp` | World Bank WDI, `NY.GDP.TOTL.RT.ZS` | % des BIP | 1014 Länderjahre |
| Staatliche Ressourceneinnahmen | `res_rev_pct_gdp` | UNU-WIDER GRD 2025, *Total Resource Revenue* | % des BIP | 478 Länderjahre |
| Ressourcensteuern | `res_tax_pct_gdp` | UNU-WIDER GRD 2025, *Resource Taxes* | % des BIP | 269 Länderjahre |
| Bruttoinlandsprodukt pro Kopf | `gdppc_const` | World Bank WDI, `NY.GDP.PCAP.KD` | konstante US-Dollar (2015) | 1032 Länderjahre |
| Zugang zu Elektrizität | `elec_access_pct` | World Bank WDI, `EG.ELC.ACCS.ZS` | % der Bevölkerung | 1040 Länderjahre |
| Index der menschlichen Entwicklung | `hdi` | UNDP HDR 2025 | Index 0–1 | 985 Länderjahre |
| Abschöpfungsquote | `capture_ratio` | eigene Berechnung: `res_rev_pct_gdp / rents_pct_gdp` | einheitenlos | 455 Länderjahre |

Grundgesamtheit: 48 Länder der World-Bank-Region Subsahara-Afrika, 2000–2021 (1056 Länderjahre).
Die Abschöpfungsquote wird nur für Länderjahre mit Rohstoffrenten von mindestens 1 % des BIP berechnet, da der Quotient bei kleinerem Nenner instabil wird.

Quelle: eigene Zusammenstellung.
