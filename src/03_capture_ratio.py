"""03_capture_ratio.py — deskriptive Kennzahlen der Capture Ratio.

Erzeugt alle Zahlen, die in Abschnitt 5.1 und im Abstract verwendet werden, und
schreibt sie nach results/zahlen.md (Abschnitt „Mark“) sowie die Quellenübersicht
nach tables/tab1_datenquellen.md.

Grundregel des Projekts: Keine Zahl darf in einen Textentwurf, die nicht hier
erzeugt und in results/zahlen.md dokumentiert ist.

Aufruf: python src/03_capture_ratio.py
"""

from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
PANEL = ROOT / "data" / "processed" / "panel.csv"
ZAHLEN = ROOT / "results" / "zahlen.md"
TAB1 = ROOT / "tables" / "tab1_datenquellen.md"

SAHEL = ["MLI", "BFA", "NER", "TCD", "MRT"]
PERIODEN = ["2000–2007", "2008–2014", "2015–2021"]
MIN_JAHRE_PERIODE = 3  # Länder-Periodenmittel erst ab drei gültigen Jahren


def fmt(wert: float | None, stellen: int = 3) -> str:
    """Zahl deutsch formatieren (Komma als Dezimaltrennzeichen)."""
    if wert is None or pd.isna(wert):
        return "n. v."
    return f"{wert:.{stellen}f}".replace(".", ",")


def schreibe_abschnitt(pfad: Path, ueberschrift: str, inhalt: list[str],
                       kopf: list[str]) -> None:
    """Nur den eigenen Abschnitt in results/zahlen.md ersetzen.

    Die Datei ist geteilt: Mark und Philip pflegen je einen Abschnitt
    (CLAUDE.md §5). Ein vollständiges Überschreiben würde den Abschnitt der
    anderen Person löschen, deshalb wird hier ausschließlich der Bereich
    zwischen der eigenen Überschrift und der nächsten `##`-Überschrift ersetzt.
    """
    neu = "\n".join([ueberschrift, ""] + inhalt).rstrip() + "\n"

    if not pfad.exists():
        pfad.parent.mkdir(parents=True, exist_ok=True)
        pfad.write_text("\n".join(kopf + ["", neu]), encoding="utf-8")
        print(f"  {pfad.name} neu angelegt")
        return

    zeilen = pfad.read_text(encoding="utf-8").splitlines()

    start = next((i for i, z in enumerate(zeilen) if z.strip() == ueberschrift), None)
    if start is None:
        # Abschnitt fehlt: hinten anhängen, fremde Abschnitte bleiben unberührt.
        pfad.write_text("\n".join(zeilen).rstrip() + "\n\n" + neu, encoding="utf-8")
        print(f"  Abschnitt '{ueberschrift}' in {pfad.name} ergänzt")
        return

    ende = next((i for i in range(start + 1, len(zeilen))
                 if zeilen[i].startswith("## ")), len(zeilen))
    fremd = [z for z in zeilen[ende:] if z.startswith("## ")]

    pfad.write_text(
        "\n".join(zeilen[:start]).rstrip() + "\n\n" + neu + "\n"
        + "\n".join(zeilen[ende:]).lstrip("\n"),
        encoding="utf-8",
    )
    print(f"  Abschnitt '{ueberschrift}' in {pfad.name} aktualisiert"
          + (f"; unverändert: {', '.join(fremd)}" if fremd else ""))


def periodenmittel(panel: pd.DataFrame) -> pd.DataFrame:
    """Länder-Periodenmittel der Capture Ratio.

    Tests und Gruppenvergleiche laufen auf dieser Ebene, nicht auf gepoolten
    Länderjahren — sonst zählt ein Land mit vielen Beobachtungen mehrfach
    (Pseudoreplikation).
    """
    gueltig = panel[panel["capture_ratio"].notna()]
    mittel = (gueltig
              .groupby(["iso3", "country", "period", "sahel", "sahel_ext", "oil_state"],
                       as_index=False)
              .agg(capture_ratio=("capture_ratio", "mean"),
                   n_jahre=("capture_ratio", "size"),
                   rents=("rents_pct_gdp", "mean"),
                   res_rev=("res_rev_pct_gdp", "mean")))
    return mittel[mittel["n_jahre"] >= MIN_JAHRE_PERIODE]


def main() -> int:
    if not PANEL.exists():
        print(f"FEHLER: {PANEL.relative_to(ROOT)} fehlt. Zuerst src/01_laden.py ausführen.")
        return 1

    panel = pd.read_csv(PANEL)
    gueltig = panel[panel["capture_ratio"].notna()]
    mittel = periodenmittel(panel)

    sahel = gueltig[gueltig["sahel"]]
    # Vergleichsgruppe: übriges Subsahara-Afrika ohne die fünf Sahel-Kernländer.
    # Sudan und Senegal bleiben enthalten — dieselbe Abgrenzung wie in
    # src/04_gruppenvergleich.py, damit alle Tabellen der Arbeit auf einer
    # einheitlichen Vergleichsgruppe beruhen.
    vergleich = gueltig[~gueltig["sahel"]]

    print("03_capture_ratio.py — deskriptive Kennzahlen")
    print(f"  {len(gueltig)} Länderjahre mit Capture Ratio, "
          f"{gueltig['iso3'].nunique()} Länder")
    print(f"  Sahel: Median {fmt(sahel['capture_ratio'].median())} (n = {len(sahel)})")
    print(f"  übriges SSA: Median {fmt(vergleich['capture_ratio'].median())} "
          f"(n = {len(vergleich)})")

    kopf = [
        "# Zahlen für den Text",
        "",
        "> Verbindliche Quelle für alle Zahlenangaben in der Abhandlung. "
        "Keine Zahl in einen Textentwurf, die nicht hier steht.",
    ]

    zeilen: list[str] = [
        f"_Erzeugt von `src/03_capture_ratio.py` aus `data/processed/panel.csv` "
        f"am {date.today().strftime('%d.%m.%Y')}._",
        "",
        "### Datengrundlage",
        "",
        f"- Analysefenster: {int(panel['year'].min())}–{int(panel['year'].max())}",
        f"- Länder der World-Bank-Region Subsahara-Afrika im Panel: "
        f"**{panel['iso3'].nunique()}**",
        f"- Länderjahre insgesamt: **{len(panel)}**",
        f"- davon mit Rohstoffrenten (WDI): **{int(panel['rents_pct_gdp'].notna().sum())}**",
        f"- davon mit Ressourceneinnahmen (GRD): "
        f"**{int(panel['res_rev_pct_gdp'].notna().sum())}**",
        f"- davon mit berechenbarer Capture Ratio (Renten ≥ 1 % BIP): **{len(gueltig)}** "
        f"in {gueltig['iso3'].nunique()} Ländern",
        f"- geflaggte Werte > 1,5: **{int(panel['flag_ratio_high'].sum())}** "
        f"({fmt(panel['flag_ratio_high'].sum() / len(gueltig) * 100, 1)} % der gültigen Werte)",
        "",
        "### Capture Ratio je Sahel-Kernland (alle Jahre)",
        "",
        "| Land | ISO3 | n Jahre | Median | Mittelwert | Minimum | Maximum |",
        "|---|---|---|---|---|---|---|",
    ]

    for iso3 in SAHEL:
        g = gueltig[gueltig["iso3"] == iso3]
        if not len(g):
            zeilen.append(f"| — | {iso3} | 0 | n. v. | n. v. | n. v. | n. v. |")
            continue
        zeilen.append(
            f"| {g['country'].iloc[0]} | {iso3} | {len(g)} | "
            f"{fmt(g['capture_ratio'].median())} | {fmt(g['capture_ratio'].mean())} | "
            f"{fmt(g['capture_ratio'].min())} | {fmt(g['capture_ratio'].max())} |"
        )

    zeilen += [
        "",
        "### Gruppenvergleich (gepoolte Länderjahre, nur deskriptiv)",
        "",
        "| Gruppe | n Länderjahre | n Länder | Median | 1. Quartil | 3. Quartil |",
        "|---|---|---|---|---|---|",
    ]
    for name, teil in [("Sahel (5 Kernländer)", sahel),
                       ("übriges Subsahara-Afrika", vergleich)]:
        zeilen.append(
            f"| {name} | {len(teil)} | {teil['iso3'].nunique()} | "
            f"{fmt(teil['capture_ratio'].median())} | "
            f"{fmt(teil['capture_ratio'].quantile(0.25))} | "
            f"{fmt(teil['capture_ratio'].quantile(0.75))} |"
        )

    zeilen += [
        "",
        f"> Hinweis: Tests laufen auf Länder-Periodenmitteln (`src/04_gruppenvergleich.py`), "
        "nicht auf diesen gepoolten Werten. Die Tabelle dient nur der Beschreibung.",
        "",
        "### Entwicklung über die Perioden (Median der Länder-Periodenmittel)",
        "",
        "| Periode | Sahel: Median | n Länder | übriges SSA: Median | n Länder |",
        "|---|---|---|---|---|",
    ]
    for p in PERIODEN:
        s = mittel[(mittel["period"] == p) & mittel["sahel"]]
        v = mittel[(mittel["period"] == p) & ~mittel["sahel"]]
        zeilen.append(
            f"| {p} | {fmt(s['capture_ratio'].median())} | {len(s)} | "
            f"{fmt(v['capture_ratio'].median())} | {len(v)} |"
        )

    # Renten- und Einnahmenniveau: zeigt, ob der Unterschied am Zähler oder am Nenner liegt
    zeilen += [
        "",
        "### Niveau von Renten und Einnahmen (Mittelwert der Länderjahre, % BIP)",
        "",
        "| Gruppe | Renten (WDI) | Ressourceneinnahmen (GRD) |",
        "|---|---|---|",
    ]
    for name, teil in [("Sahel", sahel), ("übriges SSA", vergleich)]:
        zeilen.append(
            f"| {name} | {fmt(teil['rents_pct_gdp'].mean(), 2)} | "
            f"{fmt(teil['res_rev_pct_gdp'].mean(), 2)} |"
        )

    # Geflaggte Länder transparent ausweisen — gehört in die Limitationen
    geflaggt = panel[panel["flag_ratio_high"]]
    if len(geflaggt):
        zeilen += [
            "",
            "### Geflaggte Länderjahre (Capture Ratio > 1,5)",
            "",
            "Nicht gelöscht, sondern gekennzeichnet. Ursachen sind zeitliche Verschiebungen "
            "zwischen Rentenentstehung und Einnahmeverbuchung sowie Einnahmen, die nicht "
            "als Rente im Sinne der WDI-Definition erfasst werden (etwa Dividenden aus "
            "staatlichen Beteiligungen).",
            "",
            "| Land | ISO3 | betroffene Jahre | Median der Quote |",
            "|---|---|---|---|",
        ]
        for (iso3, land), g in geflaggt.groupby(["iso3", "country"]):
            zeilen.append(f"| {land} | {iso3} | {len(g)} | "
                          f"{fmt(g['capture_ratio'].median(), 2)} |")
        im_sahel = sorted(geflaggt[geflaggt["sahel_ext"]]["iso3"].unique())
        zeilen += ["", f"Davon im Sahel: **{', '.join(im_sahel) if im_sahel else 'keines'}**."]

    # Rentenniveau 2021 je Sahel-Land, inklusive Rang in der Region (für Abb. 1)
    j2021 = panel[(panel["year"] == 2021) & panel["rents_pct_gdp"].notna()].copy()
    j2021["rang"] = j2021["rents_pct_gdp"].rank(ascending=False, method="min").astype(int)
    zeilen += [
        "",
        "### Rohstoffrenten 2021 je Sahel-Kernland (Abb. 1)",
        "",
        f"Grundlage: {len(j2021)} Länder der Region mit vorhandenem Wert für 2021.",
        "",
        "| Land | ISO3 | Renten (% BIP) | Rang in der Region |",
        "|---|---|---|---|",
    ]
    for iso3 in SAHEL:
        z = j2021[j2021["iso3"] == iso3]
        if len(z):
            r = z.iloc[0]
            zeilen.append(f"| {r['country']} | {iso3} | {fmt(r['rents_pct_gdp'], 1)} "
                          f"| {r['rang']} von {len(j2021)} |")

    zeilen += [
        "",
        "### Datenabdeckung der Sahel-Kernländer",
        "",
        "| ISO3 | Jahre mit Renten und Ressourceneinnahmen |",
        "|---|---|",
    ]
    for iso3 in SAHEL:
        g = panel[(panel["iso3"] == iso3) & panel["rents_pct_gdp"].notna()
                  & panel["res_rev_pct_gdp"].notna()]
        zeilen.append(f"| {iso3} | {len(g)} |")

    # --- Zusammensetzung der Vergleichsgruppe ---------------------------------
    # Zentral für die Einordnung: Die Vergleichsgruppe ist keine Zufallsauswahl,
    # sondern der rohstoffreiche, im GRD erfasste Teil Subsahara-Afrikas.
    ohne_grd = sorted(set(panel["iso3"]) - set(panel[panel["res_rev_pct_gdp"].notna()]["iso3"]))
    oel = vergleich[vergleich["oil_state"]]
    nicht_oel = vergleich[~vergleich["oil_state"]]
    fehlt = panel[panel["res_rev_pct_gdp"].isna() & panel["rents_pct_gdp"].notna()]
    hat = panel[panel["res_rev_pct_gdp"].notna()]

    zeilen += [
        "",
        "### Zusammensetzung der Vergleichsgruppe",
        "",
        f"- Länder der Region insgesamt: **{panel['iso3'].nunique()}**; "
        f"davon mit mindestens einem GRD-Wert: **{hat['iso3'].nunique()}**",
        f"- **{len(ohne_grd)} Länder ohne jeden GRD-Wert** und damit nicht in der "
        f"Analyse: {', '.join(ohne_grd)}",
        f"- Länderjahre ohne GRD-Wert weisen im Mittel **{fmt(fehlt['rents_pct_gdp'].mean(), 2)} % BIP** "
        f"Renten auf, solche mit GRD-Wert **{fmt(hat['rents_pct_gdp'].mean(), 2)} % BIP** — "
        "die Lücken liegen also systematisch bei den rentenärmeren Ländern, wie es der "
        "GRD User Guide beschreibt.",
        f"- Vergleichsgruppe der Analyse: **{vergleich['iso3'].nunique()} Länder**, davon "
        f"**{oel['iso3'].nunique()} Ölstaaten** (NGA, AGO, COG, GAB, GNQ, SSD), die "
        f"{oel['iso3'].nunique() / vergleich['iso3'].nunique() * 100:.0f} % der Länder und "
        f"{len(oel) / len(vergleich) * 100:.0f} % der Länderjahre stellen.",
        "",
        "### Abschöpfung nach Rohstofftyp statt nach Region",
        "",
        "Die Ölstaaten prägen den Gruppenunterschied. Ihre Abschöpfungsquote liegt "
        "deutlich über der aller übrigen Länder, und der Sahel fördert überwiegend "
        "Gold und Uran.",
        "",
        "| Gruppe | n Länder | n Länderjahre | Median | 1. Quartil | 3. Quartil |",
        "|---|---|---|---|---|---|",
        f"| Sahel (Kernländer) | {sahel['iso3'].nunique()} | {len(sahel)} | "
        f"{fmt(sahel['capture_ratio'].median())} | {fmt(sahel['capture_ratio'].quantile(.25))} | "
        f"{fmt(sahel['capture_ratio'].quantile(.75))} |",
        f"| übriges SSA: Ölstaaten | {oel['iso3'].nunique()} | {len(oel)} | "
        f"{fmt(oel['capture_ratio'].median())} | {fmt(oel['capture_ratio'].quantile(.25))} | "
        f"{fmt(oel['capture_ratio'].quantile(.75))} |",
        f"| übriges SSA: ohne Ölstaaten | {nicht_oel['iso3'].nunique()} | {len(nicht_oel)} | "
        f"{fmt(nicht_oel['capture_ratio'].median())} | "
        f"{fmt(nicht_oel['capture_ratio'].quantile(.25))} | "
        f"{fmt(nicht_oel['capture_ratio'].quantile(.75))} |",
        "",
    ]

    # Auf Länder-Periodenmitteln (Testebene), damit die Zahlen zu Tab. 2/3 passen
    m_sahel = mittel[mittel["sahel"]]
    m_vgl = mittel[~mittel["sahel"]]
    m_vgl_ohne_oel = m_vgl[~m_vgl["oil_state"]]
    zeilen += [
        "Auf Ebene der Länder-Periodenmittel (Einheit der Tests):",
        "",
        "| Vergleich | Sahel | Vergleichsgruppe |",
        "|---|---|---|",
        f"| gegen das gesamte übrige SSA | {fmt(m_sahel['capture_ratio'].median())} "
        f"(n = {m_sahel['iso3'].nunique()} Länder) | {fmt(m_vgl['capture_ratio'].median())} "
        f"(n = {m_vgl['iso3'].nunique()}) |",
        f"| gegen das übrige SSA ohne Ölstaaten | {fmt(m_sahel['capture_ratio'].median())} "
        f"(n = {m_sahel['iso3'].nunique()}) | {fmt(m_vgl_ohne_oel['capture_ratio'].median())} "
        f"(n = {m_vgl_ohne_oel['iso3'].nunique()}) |",
        "",
        "> **Einordnung:** Der Abstand zwischen Sahel und übrigem Subsahara-Afrika "
        "geht weitgehend auf die Ölstaaten zurück. Ohne sie liegen die Mediane nahe "
        "beieinander. Innerhalb des Sahel ist die Spannweite größer als der "
        "Gruppenunterschied: Tschad und Mauretanien (beide mit Erdölförderung) "
        f"erreichen {fmt(gueltig[gueltig.iso3 == 'TCD']['capture_ratio'].median(), 2)} "
        f"bzw. {fmt(gueltig[gueltig.iso3 == 'MRT']['capture_ratio'].median(), 2)}, "
        f"Burkina Faso (Gold) {fmt(gueltig[gueltig.iso3 == 'BFA']['capture_ratio'].median(), 2)} "
        f"und Niger (Uran) {fmt(gueltig[gueltig.iso3 == 'NER']['capture_ratio'].median(), 2)}. "
        "Die Signifikanztests dazu stehen in Tab. 2 und Tab. 3 (Philip).",
        "",
        "Quelle: World Bank WDI, UNU-WIDER GRD 2025, UNDP HDR; eigene Berechnung.",
    ]

    schreibe_abschnitt(ZAHLEN, "## Mark", zeilen, kopf)
    print(f"Geschrieben: {ZAHLEN.relative_to(ROOT)}")

    # --- Tabelle 1: Datenquellen ---
    tab1 = [
        "# Tabelle 1: Datenquellen und Indikatoren",
        "",
        "| Indikator | Variable im Panel | Quelle | Einheit | Abdeckung |",
        "|---|---|---|---|---|",
        "| Rohstoffrenten | `rents_pct_gdp` | World Bank WDI, `NY.GDP.TOTL.RT.ZS` | "
        f"% des BIP | {int(panel['rents_pct_gdp'].notna().sum())} Länderjahre |",
        "| Staatliche Ressourceneinnahmen | `res_rev_pct_gdp` | UNU-WIDER GRD 2025, "
        f"*Total Resource Revenue* | % des BIP | "
        f"{int(panel['res_rev_pct_gdp'].notna().sum())} Länderjahre |",
        "| Ressourcensteuern | `res_tax_pct_gdp` | UNU-WIDER GRD 2025, *Resource Taxes* | "
        f"% des BIP | {int(panel['res_tax_pct_gdp'].notna().sum())} Länderjahre |",
        "| Bruttoinlandsprodukt pro Kopf | `gdppc_const` | World Bank WDI, `NY.GDP.PCAP.KD` | "
        f"konstante US-Dollar (2015) | {int(panel['gdppc_const'].notna().sum())} Länderjahre |",
        "| Zugang zu Elektrizität | `elec_access_pct` | World Bank WDI, `EG.ELC.ACCS.ZS` | "
        f"% der Bevölkerung | {int(panel['elec_access_pct'].notna().sum())} Länderjahre |",
        "| Index der menschlichen Entwicklung | `hdi` | UNDP HDR 2025 | "
        f"Index 0–1 | {int(panel['hdi'].notna().sum())} Länderjahre |",
        "| Abschöpfungsquote | `capture_ratio` | eigene Berechnung: "
        f"`res_rev_pct_gdp / rents_pct_gdp` | einheitenlos | {len(gueltig)} Länderjahre |",
        "",
        f"Grundgesamtheit: {panel['iso3'].nunique()} Länder der World-Bank-Region "
        f"Subsahara-Afrika, {int(panel['year'].min())}–{int(panel['year'].max())} "
        f"({len(panel)} Länderjahre).",
        "Die Abschöpfungsquote wird nur für Länderjahre mit Rohstoffrenten von mindestens "
        "1 % des BIP berechnet, da der Quotient bei kleinerem Nenner instabil wird.",
        "",
        "Quelle: eigene Zusammenstellung.",
        "",
    ]
    TAB1.parent.mkdir(parents=True, exist_ok=True)
    TAB1.write_text("\n".join(tab1), encoding="utf-8")
    print(f"Geschrieben: {TAB1.relative_to(ROOT)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
