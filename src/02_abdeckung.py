"""02_abdeckung.py — Datenabdeckung je Land prüfen und dokumentieren.

Zählt je Land die Jahre mit Werten für Renten (WDI), Ressourceneinnahmen (GRD)
und HDI und beantwortet die Entscheidungsfrage aus docs/Forschungsdesign.md §5.7:

    Haben mindestens drei der fünf Sahel-Kernländer jeweils mindestens zehn Jahre
    mit GRD-Ressourceneinnahmen UND Renten?

  ja   → Analyse auf Basis des GRD (Hauptplan)
  nein → Plan B: EITI-Staatseinnahmen als Zähler

Ausgabe: tables/abdeckung.md (Sahel-Länder zuerst).
Aufruf: python src/02_abdeckung.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
PANEL = ROOT / "data" / "processed" / "panel.csv"
OUT = ROOT / "tables" / "abdeckung.md"

SAHEL = ["MLI", "BFA", "NER", "TCD", "MRT"]
SAHEL_EXT_ZUSATZ = ["SDN", "SEN"]

MINDESTJAHRE = 10
MINDESTLAENDER = 3


def jahresspanne(jahre: pd.Series) -> str:
    """Jahre als kompakte Spanne darstellen, Lücken mit '*' kennzeichnen."""
    werte = sorted(jahre.dropna().astype(int).unique())
    if not werte:
        return "—"
    spanne = f"{werte[0]}–{werte[-1]}"
    if len(werte) < werte[-1] - werte[0] + 1:
        spanne += "*"  # nicht lückenlos
    return spanne


def main() -> int:
    if not PANEL.exists():
        print(f"FEHLER: {PANEL.relative_to(ROOT)} fehlt. Zuerst src/01_laden.py ausführen.")
        return 1

    panel = pd.read_csv(PANEL)
    print(f"02_abdeckung.py — {len(panel)} Länderjahre, {panel['iso3'].nunique()} Länder")

    zeilen = []
    for iso3, gruppe in panel.groupby("iso3"):
        mit_renten = gruppe[gruppe["rents_pct_gdp"].notna()]
        mit_einnahmen = gruppe[gruppe["res_rev_pct_gdp"].notna()]
        # Entscheidend ist die Überschneidung: nur wo BEIDES vorliegt,
        # lässt sich eine Capture Ratio bilden.
        beides = gruppe[gruppe["rents_pct_gdp"].notna() & gruppe["res_rev_pct_gdp"].notna()]

        zeilen.append({
            "iso3": iso3,
            "country": gruppe["country"].dropna().iloc[0] if gruppe["country"].notna().any() else iso3,
            "gruppe": ("Sahel" if iso3 in SAHEL
                       else "Sahel (erw.)" if iso3 in SAHEL_EXT_ZUSATZ
                       else "übriges SSA"),
            "n_rents": len(mit_renten),
            "n_res_rev": len(mit_einnahmen),
            "n_beides": len(beides),
            "n_ratio": int(gruppe["capture_ratio"].notna().sum()),
            "n_hdi": int(gruppe["hdi"].notna().sum()),
            "spanne_rents": jahresspanne(mit_renten["year"]),
            "spanne_res_rev": jahresspanne(mit_einnahmen["year"]),
        })

    abdeckung = pd.DataFrame(zeilen)

    # Sortierung: Sahel-Kernländer zuerst, dann erweiterter Sahel, dann der Rest
    rang = {"Sahel": 0, "Sahel (erw.)": 1, "übriges SSA": 2}
    abdeckung["_rang"] = abdeckung["gruppe"].map(rang)
    abdeckung = abdeckung.sort_values(
        ["_rang", "n_beides", "iso3"], ascending=[True, False, True]
    ).drop(columns="_rang")

    # --- Entscheidungsfrage ---
    kern = abdeckung[abdeckung["iso3"].isin(SAHEL)]
    erfuellt = kern[kern["n_beides"] >= MINDESTJAHRE]
    plan_a = len(erfuellt) >= MINDESTLAENDER

    # --- Markdown schreiben ---
    kopf = ["Land", "ISO3", "Gruppe", "Jahre Renten", "Jahre Ressourceneinnahmen",
            "Jahre beides", "Jahre Capture Ratio", "Jahre HDI",
            "Spanne Renten", "Spanne Einnahmen"]

    md = [
        "# Datenabdeckung je Land (2000–2021)",
        "",
        "Erzeugt von `src/02_abdeckung.py` aus `data/processed/panel.csv`. "
        "Gezählt werden Jahre mit vorhandenem Wert; `*` markiert eine nicht lückenlose Spanne. "
        "„Jahre beides“ = Jahre mit Renten **und** Ressourceneinnahmen; "
        "„Jahre Capture Ratio“ zusätzlich eingeschränkt auf Renten ≥ 1 % BIP.",
        "",
        "## Entscheidung GRD vs. Plan B",
        "",
        f"Kriterium (`docs/Forschungsdesign.md` §5.7): mindestens **{MINDESTLAENDER}** der fünf "
        f"Sahel-Kernländer mit mindestens **{MINDESTJAHRE}** Jahren Renten *und* "
        "GRD-Ressourceneinnahmen.",
        "",
        f"Erfüllt: **{len(erfuellt)} von 5** "
        f"({', '.join(erfuellt['iso3']) if len(erfuellt) else 'keines'}).",
        "",
        (f"**Ergebnis: Hauptplan — Analyse auf Basis des GRD.**" if plan_a
         else f"**Ergebnis: Plan B — EITI-Staatseinnahmen als Zähler.** "
              "Begründung zusätzlich in `text/anhang/B_datenquellen.md` festhalten."),
        "",
        "## Abdeckung je Land",
        "",
        "| " + " | ".join(kopf) + " |",
        "|" + "|".join(["---"] * len(kopf)) + "|",
    ]

    for _, z in abdeckung.iterrows():
        md.append(
            f"| {z['country']} | {z['iso3']} | {z['gruppe']} | {z['n_rents']} | "
            f"{z['n_res_rev']} | {z['n_beides']} | {z['n_ratio']} | {z['n_hdi']} | "
            f"{z['spanne_rents']} | {z['spanne_res_rev']} |"
        )

    md += [
        "",
        "## Zusammenfassung nach Gruppen",
        "",
        "| Gruppe | Länder | Ø Jahre Renten | Ø Jahre Einnahmen | Ø Jahre beides |",
        "|---|---|---|---|---|",
    ]
    for gruppe in ["Sahel", "Sahel (erw.)", "übriges SSA"]:
        teil = abdeckung[abdeckung["gruppe"] == gruppe]
        if len(teil):
            md.append(
                f"| {gruppe} | {len(teil)} | {teil['n_rents'].mean():.1f} | "
                f"{teil['n_res_rev'].mean():.1f} | {teil['n_beides'].mean():.1f} |"
            )

    md += [
        "",
        "Quelle: World Bank WDI, ICTD/UNU-WIDER GRD 2023, UNDP HDR; eigene Berechnung.",
        "",
    ]

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(md), encoding="utf-8")

    # --- Konsolenausgabe für die Entscheidung ---
    print(f"\nGeschrieben: {OUT.relative_to(ROOT)}")
    print("\nSahel-Kernländer (Jahre mit Renten UND Ressourceneinnahmen):")
    for _, z in kern.iterrows():
        marke = "ok " if z["n_beides"] >= MINDESTJAHRE else "zu wenig"
        print(f"  {z['iso3']}  {z['n_beides']:>2} Jahre  ({marke})")

    print(f"\nKriterium erfüllt von {len(erfuellt)} der 5 Länder "
          f"(nötig: {MINDESTLAENDER}).")
    print("ENTSCHEIDUNG: " + ("Hauptplan — GRD verwenden."
                              if plan_a else "PLAN B — EITI als Zähler laden."))
    return 0


if __name__ == "__main__":
    sys.exit(main())
