#!/usr/bin/env python3
"""Gruppenvergleich der Capture Ratio: Sahel vs. uebriges Subsahara-Afrika.

Forschungsdesign §5.4: Gruppenvergleich je Periode mit Median, IQR und
Mann-Whitney-U auf *Laender-Periodenmitteln*. Gepoolte Laenderjahre waeren
Pseudoreplikation (Mali 2005 und Mali 2006 sind nicht unabhaengig) und
wuerden n kuenstlich aufblaehen.

Ausgabe: tables/tab2_gruppenvergleich.md, figures/fig4_boxplot.png
Aufruf:  python src/04_gruppenvergleich.py

Autor: Philip · AI Hackathon JLU, 16.09.2026
"""

from __future__ import annotations  # Typannotationen auch unter Python 3.9

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import mannwhitneyu

PANEL = Path("data/processed/panel.csv")
PANEL_FALLBACK = Path("data/processed/panel_dummy.csv")
TAB_OUT = Path("tables/tab2_gruppenvergleich.md")
FIG_OUT = Path("figures/fig4_boxplot.png")

PERIODEN = ["2000–2007", "2008–2014", "2015–2021"]
MIN_JAHRE = 3  # Mindestzahl gueltiger Jahre je Land und Periode

FARBE_SAHEL = "#C8102E"
FARBE_VERGLEICH = "#4B6584"


# --------------------------------------------------------------------------
# Daten laden
# --------------------------------------------------------------------------
def lade_panel() -> tuple[pd.DataFrame, bool]:
    """Liest panel.csv, faellt auf panel_dummy.csv zurueck. Gibt (df, ist_dummy)."""
    if PANEL.exists():
        return pd.read_csv(PANEL), False
    if not PANEL_FALLBACK.exists():
        raise SystemExit(
            f"FEHLER: Weder {PANEL} noch {PANEL_FALLBACK} vorhanden.\n"
            "Zuerst 'python src/00_dummy_panel.py' ausfuehren."
        )
    print("!" * 70)
    print("!! WARNUNG: panel.csv fehlt -- es werden DUMMY-DATEN verwendet.")
    print("!! Alle Zahlen und Abbildungen sind ERFUNDEN und duerfen NICHT")
    print("!! in results/zahlen.md oder in den Text uebernommen werden.")
    print("!" * 70)
    return pd.read_csv(PANEL_FALLBACK), True


# --------------------------------------------------------------------------
# Aggregation auf Laender-Periodenmittel
# --------------------------------------------------------------------------
def periodenmittel(df: pd.DataFrame, wert: str = "capture_ratio",
                   min_jahre: int = MIN_JAHRE,
                   gruppenspalte: str = "sahel") -> pd.DataFrame:
    """Eine Beobachtung je Land und Periode: Mittel der gueltigen Jahre.

    Laender mit weniger als `min_jahre` gueltigen Jahren in einer Periode
    werden fuer diese Periode ausgeschlossen (instabile Mittelwerte).
    """
    gueltig = df[df[wert].notna()].copy()
    agg = (
        gueltig.groupby(["iso3", "country", gruppenspalte, "period"], as_index=False)
        .agg(mittel=(wert, "mean"), n_jahre=(wert, "size"))
    )
    agg = agg[agg["n_jahre"] >= min_jahre].copy()
    agg = agg.rename(columns={gruppenspalte: "gruppe_sahel"})
    agg["gruppe"] = np.where(agg["gruppe_sahel"], "Sahel", "übriges SSA")
    return agg


# --------------------------------------------------------------------------
# Test und Effektgroessen
# --------------------------------------------------------------------------
def cliffs_delta(u_statistik: float, n1: int, n2: int) -> float:
    """Cliff's Delta aus der U-Statistik: delta = 2U/(n1*n2) - 1.

    Wertebereich -1 bis +1. delta = P(x > y) - P(y > x), also der
    Ueberlappungsgrad zweier Verteilungen -- direkt interpretierbar als
    Anteil der Laenderpaare, in denen die erste Gruppe hoeher liegt.
    """
    return 2.0 * u_statistik / (n1 * n2) - 1.0


def delta_label(delta: float) -> str:
    """Einordnung nach Romano et al. (2006): 0,147 / 0,33 / 0,474."""
    a = abs(delta)
    if a < 0.147:
        return "vernachlässigbar"
    if a < 0.330:
        return "klein"
    if a < 0.474:
        return "mittel"
    return "groß"


def vergleiche(agg: pd.DataFrame) -> list[dict]:
    """Mann-Whitney-U je Periode, Sahel gegen uebriges SSA."""
    zeilen = []
    for periode in PERIODEN:
        teil = agg[agg["period"] == periode]
        x = teil.loc[teil["gruppe_sahel"], "mittel"].to_numpy()
        y = teil.loc[~teil["gruppe_sahel"], "mittel"].to_numpy()

        eintrag = {
            "periode": periode,
            "n_sahel": len(x),
            "n_vergleich": len(y),
            "median_sahel": np.median(x) if len(x) else np.nan,
            "median_vergleich": np.median(y) if len(y) else np.nan,
            "iqr_sahel": _iqr(x),
            "iqr_vergleich": _iqr(y),
            "u": np.nan, "p": np.nan, "delta": np.nan, "delta_txt": "—",
        }

        # Test nur bei ausreichender Besetzung beider Gruppen.
        if len(x) >= 3 and len(y) >= 3:
            u, p = mannwhitneyu(x, y, alternative="two-sided")
            d = cliffs_delta(u, len(x), len(y))
            eintrag.update({"u": u, "p": p, "delta": d, "delta_txt": delta_label(d)})
        zeilen.append(eintrag)
    return zeilen


def _iqr(werte: np.ndarray) -> tuple[float, float]:
    if len(werte) < 2:
        return (np.nan, np.nan)
    return (float(np.percentile(werte, 25)), float(np.percentile(werte, 75)))


# --------------------------------------------------------------------------
# Tabelle
# --------------------------------------------------------------------------
def schreibe_tabelle(zeilen: list[dict], agg: pd.DataFrame,
                     df: pd.DataFrame, ist_dummy: bool) -> None:
    def f(x, nd=2):
        return "—" if x is None or (isinstance(x, float) and np.isnan(x)) else f"{x:.{nd}f}".replace(".", ",")

    def p_fmt(p):
        if isinstance(p, float) and np.isnan(p):
            return "—"
        return "< 0,001" if p < 0.001 else f"{p:.3f}".replace(".", ",")

    zeilen_md = []
    for z in zeilen:
        zeilen_md.append(
            f"| {z['periode']} "
            f"| {z['n_sahel']} | {f(z['median_sahel'])} "
            f"| {f(z['iqr_sahel'][0])}–{f(z['iqr_sahel'][1])} "
            f"| {z['n_vergleich']} | {f(z['median_vergleich'])} "
            f"| {f(z['iqr_vergleich'][0])}–{f(z['iqr_vergleich'][1])} "
            f"| {f(z['u'], 1)} | {p_fmt(z['p'])} "
            f"| {f(z['delta'])} ({z['delta_txt']}) |"
        )

    geflaggt = int(df["flag_ratio_high"].sum()) if "flag_ratio_high" in df else 0

    # n-Angabe: Spannweite nur nennen, wenn sie ueber die Perioden variiert.
    n_werte = sorted({z["n_sahel"] for z in zeilen})
    n_sahel_txt = (
        f"n = {n_werte[0]}" if len(n_werte) == 1
        else f"n = {n_werte[0]}–{n_werte[-1]}"
    )

    # Welche Sahel-Laender schaffen die Mindestjahres-Schwelle nicht in
    # allen Perioden? Fuer die Limitationen und den Ergebnistext relevant.
    sahel_alle = set(df.loc[df["sahel"], "iso3"])
    vertreten = {
        p: set(agg.loc[agg["gruppe_sahel"] & (agg["period"] == p), "iso3"])
        for p in PERIODEN
    }
    luecken = []
    for iso in sorted(sahel_alle):
        fehlt = [p for p in PERIODEN if iso not in vertreten[p]]
        if fehlt:
            luecken.append(f"{iso} (fehlt in {', '.join(fehlt)})")
    fehlend_txt = "; ".join(luecken) if luecken else "keine"

    kopf = ""
    if ist_dummy:
        kopf = (
            "> **ACHTUNG: auf DUMMY-DATEN gerechnet (`panel_dummy.csv`).**\n"
            "> Alle Werte sind erfunden und dienen nur dem Test der Pipeline.\n"
            "> Nach Vorliegen von `panel.csv` neu erzeugen.\n\n"
        )

    inhalt = f"""# Tab. 2 — Capture Ratio: Sahel vs. übriges Subsahara-Afrika

{kopf}Einheit der Analyse: **Länder-Periodenmittel** der Capture Ratio
(ein Wert je Land und Periode; Länder mit weniger als {MIN_JAHRE} gültigen
Jahren in einer Periode bleiben für diese Periode unberücksichtigt).
Test: Mann-Whitney-U (zweiseitig). Effektgröße: Cliff's Delta
(negativ = Sahel niedriger), Einordnung nach Romano et al. (2006).

| Periode | n Sahel | Median Sahel | IQR Sahel | n übr. SSA | Median übr. SSA | IQR übr. SSA | U | p | Cliff's δ |
|---|---|---|---|---|---|---|---|---|---|
{chr(10).join(zeilen_md)}

**Lesehilfe:** Die Capture Ratio ist einheitenlos und gibt den Anteil der
Rohstoffrenten an, der als Ressourceneinnahme im Staatshaushalt ankommt
(0,30 = 30 %). Cliff's δ = −0,50 bedeutet: In 75 % der Länderpaare liegt das
Sahel-Land unter dem Vergleichsland.

**Hinweise zur Interpretation:**
- Der Test prüft, ob ein zufällig gezogenes Sahel-Land über einem zufällig
  gezogenen Vergleichsland liegt, nicht Kausalität. Alle Befunde sind
  **Assoziationen**.
- Mit {n_sahel_txt} Sahel-Ländern je Periode ist die Teststärke gering.
  Ein nicht signifikantes Ergebnis heißt „für eine Aussage reichen die Daten
  nicht", nicht „kein Unterschied". Deshalb steht die Effektgröße vor dem p-Wert.
- Länderjahre mit Rohstoffrenten < 1 % BIP sind bereits in `panel.csv`
  ausgeschlossen (kleiner Nenner).
- Nicht in allen Perioden vertretene Sahel-Länder: {fehlend_txt}.
- {geflaggt} Länderjahre mit Capture Ratio > 1,5 sind enthalten und geflaggt
  (`flag_ratio_high`); sie entstehen durch Timing zwischen Rentenanfall und
  Zahlungseingang sowie durch Preisschocks und wurden nicht entfernt.

Quelle: World Bank WDI, UNU-WIDER GRD 2025; eigene Berechnung.
Erzeugt von `src/04_gruppenvergleich.py`.
"""
    TAB_OUT.parent.mkdir(parents=True, exist_ok=True)
    TAB_OUT.write_text(inhalt, encoding="utf-8")
    print(f"geschrieben: {TAB_OUT}")


# --------------------------------------------------------------------------
# Abb. 4 — Boxplots
# --------------------------------------------------------------------------
def zeichne_abb4(agg: pd.DataFrame, ist_dummy: bool) -> None:
    fig, ax = plt.subplots(figsize=(9, 5.5))
    rng = np.random.default_rng(42)  # nur fuer den Jitter der Punkte

    positionen, daten, farben = [], [], []
    for i, periode in enumerate(PERIODEN):
        teil = agg[agg["period"] == periode]
        for j, (ist_sahel, farbe) in enumerate(
            [(True, FARBE_SAHEL), (False, FARBE_VERGLEICH)]
        ):
            werte = teil.loc[teil["gruppe_sahel"] == ist_sahel, "mittel"].to_numpy()
            positionen.append(i * 3 + j)
            daten.append(werte)
            farben.append(farbe)

    bp = ax.boxplot(
        daten, positions=positionen, widths=0.7, patch_artist=True,
        showfliers=False, medianprops=dict(color="black", linewidth=1.6),
        whiskerprops=dict(color="#555555"), capprops=dict(color="#555555"),
        boxprops=dict(edgecolor="#555555"),
    )
    for patch, farbe in zip(bp["boxes"], farben):
        patch.set_facecolor(farbe)
        patch.set_alpha(0.35)

    # Achse auf den interpretierbaren Bereich begrenzen. Einzelne
    # Vergleichslaender (v. a. BWA) erreichen Quoten um 7-9, weil im GRD
    # Dividenden aus Joint Ventures als Ressourceneinnahme erscheinen, die
    # WDI-Rente aber nur Preis minus Foerderkosten erfasst. Ohne Begrenzung
    # stauchen diese Faelle die gesamte relevante Variation unkenntlich.
    # Die Werte bleiben in Median, IQR und Test enthalten -- nur die
    # Darstellung wird gekappt, und die Zahl der gekappten Punkte wird
    # in der Abbildung ausgewiesen.
    Y_MAX = 1.6
    n_gekappt = 0

    # Einzelne Laenderpunkte ueberlagern -- macht das kleine n sichtbar.
    for pos, werte, farbe in zip(positionen, daten, farben):
        if len(werte) == 0:
            continue
        x = pos + rng.uniform(-0.18, 0.18, size=len(werte))
        innen = werte <= Y_MAX
        ax.scatter(x[innen], werte[innen], s=26, color=farbe,
                   edgecolor="white", linewidth=0.6, zorder=3, alpha=0.9)
        # Gekappte Punkte als Dreieck am oberen Rand andeuten.
        if (~innen).any():
            n_gekappt += int((~innen).sum())
            ax.scatter(x[~innen], np.full((~innen).sum(), Y_MAX * 0.995),
                       s=34, color=farbe, marker="^", edgecolor="white",
                       linewidth=0.6, zorder=3, alpha=0.9, clip_on=False)

    ax.set_xticks([i * 3 + 0.5 for i in range(len(PERIODEN))])
    ax.set_xticklabels(PERIODEN)
    ax.set_xlabel("Periode")
    ax.set_ylabel("Capture Ratio (Anteil der Renten im Staatshaushalt)")
    ax.set_title("Abb. 4: Staatliche Abschöpfungsquote nach Periode und Gruppe",
                 pad=28)

    # Untere Headroom fuer die n-Angaben innerhalb der Achse.
    ax.set_ylim(-0.19 * Y_MAX, Y_MAX)

    ax.axhline(1.0, color="#999999", linestyle=":", linewidth=1)
    ax.text(ax.get_xlim()[1], 1.0, " Rente vollständig\n abgeschöpft",
            va="center", ha="left", fontsize=7, color="#666666")

    if n_gekappt:
        ax.text(
            0.985, 0.975,
            f"▲ {n_gekappt} Länder-Periodenmittel über {Y_MAX:.1f}".replace(".", ",")
            + "\n(in Median, IQR und Test enthalten)",
            transform=ax.transAxes, ha="right", va="top", fontsize=7.5,
            color="#555555",
        )

    # Legende ueber der Zeichenfläche -- ueberdeckt so keine Datenpunkte.
    ax.legend(
        handles=[
            plt.Line2D([], [], marker="s", linestyle="", markersize=9,
                       markerfacecolor=FARBE_SAHEL, alpha=0.6,
                       markeredgecolor="#555555", label="Sahel (MLI, BFA, NER, TCD, MRT)"),
            plt.Line2D([], [], marker="s", linestyle="", markersize=9,
                       markerfacecolor=FARBE_VERGLEICH, alpha=0.6,
                       markeredgecolor="#555555", label="übriges Subsahara-Afrika"),
        ],
        loc="lower center", bbox_to_anchor=(0.5, 1.0), ncol=2,
        frameon=False, fontsize=9, handletextpad=0.4, columnspacing=2.0,
    )
    ax.spines[["top", "right"]].set_visible(False)
    ax.grid(axis="y", alpha=0.25, linewidth=0.6)

    # n je Box innerhalb der Achse angeben (Regel: n immer angeben).
    for pos, werte in zip(positionen, daten):
        ax.annotate(f"n = {len(werte)}", xy=(pos, 0.0), xycoords=("data", "axes fraction"),
                    xytext=(0, 7), textcoords="offset points",
                    ha="center", fontsize=7.5, color="#444444")

    if ist_dummy:
        ax.text(0.5, 0.5, "DUMMY-DATEN", transform=ax.transAxes,
                fontsize=42, color="red", alpha=0.18, ha="center",
                va="center", rotation=22, zorder=10)

    FIG_OUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(FIG_OUT, dpi=300, bbox_inches="tight")
    plt.close(fig)
    print(f"geschrieben: {FIG_OUT}")


# --------------------------------------------------------------------------
def main() -> None:
    df, ist_dummy = lade_panel()
    agg = periodenmittel(df)

    print(f"\nLaender-Periodenmittel: {len(agg)} Beobachtungen "
          f"({agg['iso3'].nunique()} Laender)")

    zeilen = vergleiche(agg)
    print("\n" + "-" * 78)
    for z in zeilen:
        print(f"{z['periode']}  Sahel n={z['n_sahel']:<3} Median={z['median_sahel']:.3f}"
              f"   |  uebr. SSA n={z['n_vergleich']:<3} Median={z['median_vergleich']:.3f}")
        if not np.isnan(z["p"]):
            print(f"{'':12}U={z['u']:.1f}  p={z['p']:.4f}  "
                  f"Cliff's delta={z['delta']:+.3f} ({z['delta_txt']})")
    print("-" * 78)
    print("Assoziation, keine Kausalitaet. Effektgroesse vor p-Wert lesen.\n")

    schreibe_tabelle(zeilen, agg, df, ist_dummy)
    zeichne_abb4(agg, ist_dummy)

    if ist_dummy:
        print("\nERINNERUNG: Ergebnisse basieren auf DUMMY-DATEN.")


if __name__ == "__main__":
    main()
