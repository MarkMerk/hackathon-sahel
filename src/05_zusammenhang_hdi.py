#!/usr/bin/env python3
"""Zusammenhang zwischen Capture Ratio und menschlicher Entwicklung.

Forschungsdesign §5.5: Spearman-Rangkorrelation der Capture Ratio mit HDI
und Stromzugang auf *Laender-Periodenmitteln*, zusaetzlich eine Two-way-
Fixed-Effects-OLS mit laenderweise geclusterten Standardfehlern.

WICHTIG: Alle Befunde sind **Assoziationen**, keine Kausalitaet. Ein
Zusammenhang zwischen Abschoepfungsquote und HDI kann auf gemeinsame
Ursachen (Staatskapazitaet, Institutionen) zurueckgehen; die Wirkungs-
richtung ist mit diesen Daten nicht bestimmbar. Auch die Fixed-Effects-
Schaetzung identifiziert keinen kausalen Effekt, sie kontrolliert nur
zeitkonstante Laendermerkmale und gemeinsame Jahresschocks.

Ausgabe: tables/tab2b_zusammenhang.md, figures/fig5_hdi.png
Aufruf:  python src/05_zusammenhang_hdi.py

Autor: Philip · AI Hackathon JLU, 16.09.2026
"""

from __future__ import annotations  # Typannotationen auch unter Python 3.9

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import spearmanr

# Aggregationslogik aus Skript 04 wiederverwenden (identische Definition).
import importlib.util

_spec = importlib.util.spec_from_file_location(
    "gv", Path(__file__).with_name("04_gruppenvergleich.py")
)
_gv = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_gv)

PANEL = _gv.PANEL
TAB_OUT = Path("tables/tab2b_zusammenhang.md")
FIG_OUT = Path("figures/fig5_hdi.png")
PERIODEN = _gv.PERIODEN
MIN_JAHRE = _gv.MIN_JAHRE
FARBE_SAHEL = _gv.FARBE_SAHEL
FARBE_VERGLEICH = _gv.FARBE_VERGLEICH


def periodenmittel_mehrspaltig(df: pd.DataFrame) -> pd.DataFrame:
    """Laender-Periodenmittel fuer capture_ratio, hdi, Stromzugang und BIP/Kopf.

    Die Mindestjahres-Regel gilt fuer die capture_ratio (unsere Kernvariable);
    die Kovariaten werden ueber dieselben Laenderjahre gemittelt.
    """
    basis = df[df["capture_ratio"].notna()].copy()
    agg = basis.groupby(["iso3", "country", "sahel", "period"], as_index=False).agg(
        capture_ratio=("capture_ratio", "mean"),
        n_jahre=("capture_ratio", "size"),
        hdi=("hdi", "mean"),
        elec_access_pct=("elec_access_pct", "mean"),
        gdppc_const=("gdppc_const", "mean"),
    )
    agg = agg[agg["n_jahre"] >= MIN_JAHRE].copy()
    agg["gruppe"] = np.where(agg["sahel"], "Sahel", "übriges SSA")
    return agg


def spearman_block(agg: pd.DataFrame, ziel: str) -> list[dict]:
    """Spearman capture_ratio <-> ziel, gesamt und je Periode."""
    ergebnisse = []
    for label, teil in [("alle Perioden", agg)] + [
        (p, agg[agg["period"] == p]) for p in PERIODEN
    ]:
        paar = teil[["capture_ratio", ziel]].dropna()
        if len(paar) < 4:
            ergebnisse.append({"ebene": label, "n": len(paar),
                               "rho": np.nan, "p": np.nan})
            continue
        rho, p = spearmanr(paar["capture_ratio"], paar[ziel])
        ergebnisse.append({"ebene": label, "n": len(paar), "rho": rho, "p": p})
    return ergebnisse


def fe_ols(df: pd.DataFrame) -> dict | None:
    """Two-way-FE-OLS: hdi ~ capture_ratio + log(gdppc) + Land-FE + Jahr-FE.

    Geclusterte Standardfehler nach Land. Auf Laenderjahren geschaetzt, weil
    Fixed Effects Variation innerhalb der Laender brauchen -- die Clusterung
    korrigiert die Abhaengigkeit der Beobachtungen eines Landes.
    Rein deskriptive Assoziation, KEINE Kausalschaetzung.
    """
    try:
        import statsmodels.formula.api as smf
    except ImportError:
        print("statsmodels nicht verfuegbar -- FE-OLS uebersprungen.")
        return None

    d = df[["iso3", "year", "hdi", "capture_ratio", "gdppc_const"]].dropna().copy()
    d = d[d["gdppc_const"] > 0]
    if d["iso3"].nunique() < 10 or len(d) < 50:
        print("Zu wenig Beobachtungen fuer FE-OLS -- uebersprungen.")
        return None

    d["log_gdppc"] = np.log(d["gdppc_const"])
    modell = smf.ols("hdi ~ capture_ratio + log_gdppc + C(iso3) + C(year)", data=d).fit(
        cov_type="cluster", cov_kwds={"groups": d["iso3"]}
    )
    ki = modell.conf_int().loc["capture_ratio"]
    return {
        "koeffizient": float(modell.params["capture_ratio"]),
        "se": float(modell.bse["capture_ratio"]),
        "p": float(modell.pvalues["capture_ratio"]),
        "ki_unten": float(ki[0]),
        "ki_oben": float(ki[1]),
        "n": int(modell.nobs),
        "n_laender": int(d["iso3"].nunique()),
        "r2": float(modell.rsquared),
    }


# --------------------------------------------------------------------------
def schreibe_tabelle(hdi_res, strom_res, fe, agg, ist_dummy) -> None:
    def zahl(x, nd=3):
        return "—" if x is None or (isinstance(x, float) and np.isnan(x)) else f"{x:.{nd}f}".replace(".", ",")

    def p_fmt(p):
        if p is None or (isinstance(p, float) and np.isnan(p)):
            return "—"
        return "< 0,001" if p < 0.001 else f"{p:.3f}".replace(".", ",")

    def block(res):
        return "\n".join(
            f"| {r['ebene']} | {r['n']} | {zahl(r['rho'])} | {p_fmt(r['p'])} |"
            for r in res
        )

    fe_text = "Nicht geschätzt (zu wenige Beobachtungen oder statsmodels fehlt)."
    if fe:
        fe_text = (
            f"Koeffizient der Capture Ratio: **{zahl(fe['koeffizient'], 4)}** "
            f"(SE {zahl(fe['se'], 4)}, p {p_fmt(fe['p'])}, "
            f"95-%-KI [{zahl(fe['ki_unten'], 4)}; {zahl(fe['ki_oben'], 4)}]), "
            f"n = {fe['n']} Länderjahre aus {fe['n_laender']} Ländern, "
            f"R² = {zahl(fe['r2'])} (inkl. Fixed Effects).\n\n"
            f"Lesart: Eine um 0,1 höhere Capture Ratio geht mit einem um "
            f"{zahl(fe['koeffizient'] * 0.1, 4)} HDI-Punkten abweichenden Wert einher — "
            f"**innerhalb** eines Landes und nach Kontrolle des Jahres und des "
            f"BIP pro Kopf. Das ist eine Assoziation; die Wirkungsrichtung ist "
            f"nicht identifiziert."
        )

    kopf = ""
    if ist_dummy:
        kopf = (
            "> **ACHTUNG: auf DUMMY-DATEN gerechnet (`panel_dummy.csv`).**\n"
            "> Alle Werte sind erfunden. Nach Vorliegen von `panel.csv` neu erzeugen.\n\n"
        )

    inhalt = f"""# Tab. 2b — Capture Ratio und menschliche Entwicklung

{kopf}Spearman-Rangkorrelation auf **Länder-Periodenmitteln** (ein Wert je Land
und Periode, mindestens {MIN_JAHRE} gültige Jahre). Rangbasiert, weil beide
Größen schief verteilt sind und der Zusammenhang nicht linear sein muss.

## Capture Ratio ↔ HDI

| Ebene | n | Spearman ρ | p |
|---|---|---|---|
{block(hdi_res)}

## Capture Ratio ↔ Stromzugang (% der Bevölkerung)

| Ebene | n | Spearman ρ | p |
|---|---|---|---|
{block(strom_res)}

## Two-way-Fixed-Effects-OLS (Ergänzung)

Modell: `hdi ~ capture_ratio + log(BIP pro Kopf) + Land-FE + Jahr-FE`,
Standardfehler geclustert nach Land.

{fe_text}

## Einordnung

- **Assoziation, keine Kausalität.** Eine höhere Abschöpfungsquote und ein
  höherer HDI können beide Folge einer dritten Größe sein — etwa staatlicher
  Verwaltungskapazität oder der Qualität fiskalischer Institutionen. Auch die
  umgekehrte Richtung ist denkbar: entwickeltere Staaten können Renten besser
  besteuern.
- Die Capture Ratio sagt nichts darüber, **wofür** die Einnahmen verwendet
  werden. Ein hoher Wert bedeutet nicht, dass die Mittel entwicklungswirksam
  eingesetzt werden; die Verteilung innerhalb des Staates bleibt außerhalb
  der Reichweite dieser Daten.
- Der HDI bewegt sich über 22 Jahre träge und monoton nach oben. In der
  FE-Schätzung konkurriert die Capture Ratio daher mit einem starken
  Zeittrend, der über die Jahres-Fixed-Effects absorbiert wird.

Quelle: World Bank WDI, UNU-WIDER GRD 2025, UNDP HDI; eigene Berechnung.
Erzeugt von `src/05_zusammenhang_hdi.py`.
"""
    TAB_OUT.parent.mkdir(parents=True, exist_ok=True)
    TAB_OUT.write_text(inhalt, encoding="utf-8")
    print(f"geschrieben: {TAB_OUT}")


# --------------------------------------------------------------------------
def zeichne_abb5(agg: pd.DataFrame, hdi_res: list[dict], ist_dummy: bool) -> None:
    fig, axes = plt.subplots(1, 3, figsize=(13, 4.8), sharex=True, sharey=True)

    for ax, periode in zip(axes, PERIODEN):
        teil = agg[agg["period"] == periode].dropna(subset=["capture_ratio", "hdi"])
        verg = teil[~teil["sahel"]]
        sahel = teil[teil["sahel"]]

        ax.scatter(verg["capture_ratio"], verg["hdi"], s=34,
                   color=FARBE_VERGLEICH, alpha=0.55, edgecolor="white",
                   linewidth=0.6, label="übriges Subsahara-Afrika")
        ax.scatter(sahel["capture_ratio"], sahel["hdi"], s=90,
                   color=FARBE_SAHEL, edgecolor="white", linewidth=0.9,
                   zorder=4, label="Sahel")

        # Sahel-Laender beschriften -- macht die fuenf Faelle nachvollziehbar.
        for _, r in sahel.iterrows():
            ax.annotate(r["iso3"], (r["capture_ratio"], r["hdi"]),
                        xytext=(6, 4), textcoords="offset points",
                        fontsize=7.5, color=FARBE_SAHEL, fontweight="bold")

        rho = next((r["rho"] for r in hdi_res if r["ebene"] == periode), np.nan)
        n = next((r["n"] for r in hdi_res if r["ebene"] == periode), 0)
        beschriftung = (
            f"ρ = {rho:.2f}".replace(".", ",") if not np.isnan(rho) else "ρ = —"
        )
        ax.set_title(f"{periode}\n{beschriftung}, n = {n}", fontsize=10)
        ax.set_xlabel("Capture Ratio")
        ax.spines[["top", "right"]].set_visible(False)
        ax.grid(alpha=0.22, linewidth=0.6)

        if ist_dummy:
            ax.text(0.5, 0.5, "DUMMY", transform=ax.transAxes, fontsize=30,
                    color="red", alpha=0.16, ha="center", va="center", rotation=22)

    axes[0].set_ylabel("HDI (Index, 0–1)")
    fig.suptitle(
        "Abb. 5: Staatliche Abschöpfungsquote und menschliche Entwicklung "
        "(Länder-Periodenmittel)", fontsize=12, y=1.10,
    )
    # Legende auf Figur-Ebene, damit sie keine Datenpunkte verdeckt.
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="upper center", bbox_to_anchor=(0.5, 1.02),
               ncol=2, frameon=False, fontsize=9)

    FIG_OUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIG_OUT, dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"geschrieben: {FIG_OUT}")


# --------------------------------------------------------------------------
def main() -> None:
    df, ist_dummy = _gv.lade_panel()
    agg = periodenmittel_mehrspaltig(df)
    print(f"\nLaender-Periodenmittel: {len(agg)} Beobachtungen "
          f"({agg['iso3'].nunique()} Laender)")

    hdi_res = spearman_block(agg, "hdi")
    strom_res = spearman_block(agg, "elec_access_pct")

    print("\nSpearman capture_ratio <-> HDI")
    for r in hdi_res:
        print(f"  {r['ebene']:<14} n={r['n']:<4} rho={r['rho']:+.3f}  p={r['p']:.4f}"
              if not np.isnan(r["rho"]) else f"  {r['ebene']:<14} n={r['n']:<4} —")
    print("\nSpearman capture_ratio <-> Stromzugang")
    for r in strom_res:
        print(f"  {r['ebene']:<14} n={r['n']:<4} rho={r['rho']:+.3f}  p={r['p']:.4f}"
              if not np.isnan(r["rho"]) else f"  {r['ebene']:<14} n={r['n']:<4} —")

    fe = fe_ols(df)
    if fe:
        print(f"\nFE-OLS capture_ratio: b={fe['koeffizient']:+.4f} "
              f"(SE {fe['se']:.4f}, p={fe['p']:.4f}), n={fe['n']}")

    print("\nAssoziation, keine Kausalitaet.\n")
    schreibe_tabelle(hdi_res, strom_res, fe, agg, ist_dummy)
    zeichne_abb5(agg, hdi_res, ist_dummy)

    if ist_dummy:
        print("\nERINNERUNG: Ergebnisse basieren auf DUMMY-DATEN.")


if __name__ == "__main__":
    main()
