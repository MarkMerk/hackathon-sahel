"""Abbildung 3: Streudiagramm Rohstoffrenten vs. staatliche Ressourceneinnahmen
(je % des BIP) mit 45-Grad-Referenzlinie (vollstaendige Abschoepfung).

Einheit der Darstellung: Laender-Periodenmittel (2000-2007, 2008-2014,
2015-2021), nicht einzelne Laenderjahre - sonst zaehlt ein Land mehrfach.
Nur Land-Perioden-Kombinationen mit mindestens 3 gueltigen Jahren fuer
sowohl Renten als auch Ressourceneinnahmen.

Datenquelle: data/processed/panel.csv (Schema siehe docs/Forschungsdesign.md §4).
Erzeugt figures/fig3_streudiagramm.png (dpi=300, bbox_inches="tight").
"""

import matplotlib.pyplot as plt
import pandas as pd

PANEL_PATH = "data/processed/panel.csv"
FIG_PATH = "figures/fig3_streudiagramm.png"

# Farbenblindenfreundliche Palette (Okabe-Ito)
COLOR_SAHEL = "#D55E00"  # orange
COLOR_OTHER = "#0072B2"  # blau

MIN_YEARS = 3

# Achsenobergrenze: begrenzt die Darstellung auf einen lesbaren Bereich.
# Extreme Renten-Ausreisser (GNQ, COG, jeweils 2000-2007) werden dadurch
# nicht dargestellt, aber nicht aus den Daten geloescht.
AXIS_LIMIT = 45

# Markerformen je Periode
PERIOD_MARKERS = {
    "2000–2007": "o",
    "2008–2014": "^",
    "2015–2021": "s",
}
PERIOD_ORDER = ["2000–2007", "2008–2014", "2015–2021"]


def main():
    df = pd.read_csv(PANEL_PATH)

    sub = df.dropna(subset=["rents_pct_gdp", "res_rev_pct_gdp"]).copy()

    grouped = (
        sub.groupby(["iso3", "period"])
        .agg(
            n_years=("year", "count"),
            rents_pct_gdp=("rents_pct_gdp", "mean"),
            res_rev_pct_gdp=("res_rev_pct_gdp", "mean"),
            sahel=("sahel", "first"),
        )
        .reset_index()
    )
    grouped = grouped[grouped["n_years"] >= MIN_YEARS].copy()

    n_countries = grouped["iso3"].nunique()
    n_points = len(grouped)
    n_sahel_countries = grouped.loc[grouped["sahel"], "iso3"].nunique()
    n_sahel_points = int(grouped["sahel"].sum())

    # Punkte ausserhalb des dargestellten Achsenbereichs zaehlen (nicht loeschen)
    outside = grouped[
        (grouped["rents_pct_gdp"] > AXIS_LIMIT)
        | (grouped["res_rev_pct_gdp"] > AXIS_LIMIT)
    ]
    n_outside = len(outside)
    outside_labels = sorted(
        f"{row.iso3} ({row.period})" for row in outside.itertuples()
    )

    within = grouped[~grouped.index.isin(outside.index)].copy()

    # 16 cm Breite, quadratisches Seitenverhaeltnis fuer vergleichbare Achsen
    fig_width_in = 16 / 2.54
    fig_height_in = 13.5 / 2.54
    fig, ax = plt.subplots(figsize=(fig_width_in, fig_height_in))

    # 45-Grad-Referenzlinie: vollstaendige Abschoepfung
    ax.plot(
        [0, AXIS_LIMIT],
        [0, AXIS_LIMIT],
        color="gray",
        linestyle="--",
        linewidth=1.3,
        label="vollständige Abschöpfung (y = x)",
        zorder=1,
    )

    # Uebrige Laender: neutral, klein, im Hintergrund
    other = within[~within["sahel"]]
    for period in PERIOD_ORDER:
        p = other[other["period"] == period]
        if p.empty:
            continue
        ax.scatter(
            p["rents_pct_gdp"],
            p["res_rev_pct_gdp"],
            marker=PERIOD_MARKERS[period],
            s=22,
            facecolor=COLOR_OTHER,
            edgecolor="white",
            linewidth=0.4,
            alpha=0.6,
            zorder=2,
        )

    # Sahel-Laender: hervorgehoben, groesser, mit ISO3-Beschriftung
    sahel_pts = within[within["sahel"]]
    for period in PERIOD_ORDER:
        p = sahel_pts[sahel_pts["period"] == period]
        if p.empty:
            continue
        ax.scatter(
            p["rents_pct_gdp"],
            p["res_rev_pct_gdp"],
            marker=PERIOD_MARKERS[period],
            s=55,
            facecolor=COLOR_SAHEL,
            edgecolor="black",
            linewidth=0.5,
            zorder=4,
        )

    # Burkina Faso und Niger schöpfen so wenig ab, dass ihre Punkte im unteren
    # linken Bereich fast aufeinanderliegen. Statt jeden Punkt einzeln zu
    # beschriften, wird je Land nur einmal beschriftet — am Punkt mit den
    # höchsten Renten, wo am meisten Platz ist. Die Periodenzuordnung bleibt
    # über die Markerform erkennbar.
    # Burkina Faso (10,9 | 0,4) und Niger (9,0 | 0,4) liegen praktisch
    # aufeinander, weil beide fast nichts abschöpfen. Ihre Beschriftungen
    # werden deshalb nach oben bzw. unten weggeführt und mit einer dünnen
    # Linie an den Punkt gebunden; TCD und MRT haben genug Platz.
    versatz = {"BFA": (-8, 20), "NER": (-30, -14), "TCD": (9, 6), "MRT": (9, 6)}
    for iso3, gruppe in sahel_pts.groupby("iso3"):
        anker = gruppe.loc[gruppe["rents_pct_gdp"].idxmax()]
        dx, dy = versatz.get(iso3, (7, 5))
        weit = abs(dx) > 8 or abs(dy) > 8
        ax.annotate(
            iso3,
            (anker["rents_pct_gdp"], anker["res_rev_pct_gdp"]),
            textcoords="offset points",
            xytext=(dx, dy),
            fontsize=9,
            color=COLOR_SAHEL,
            fontweight="bold",
            zorder=5,
            arrowprops=(dict(arrowstyle="-", color=COLOR_SAHEL, linewidth=0.6,
                             shrinkA=0, shrinkB=2) if weit else None),
        )

    ax.set_xlim(0, AXIS_LIMIT)
    ax.set_ylim(0, AXIS_LIMIT)
    ax.set_aspect("equal", adjustable="box")

    ax.set_xlabel("Rohstoffrenten (% des BIP)", fontsize=10)
    ax.set_ylabel("Staatliche Ressourceneinnahmen (% des BIP)", fontsize=10)
    ax.tick_params(axis="both", labelsize=9)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(linestyle="--", alpha=0.3)
    ax.set_axisbelow(True)

    # Legende: Referenzlinie, Gruppenfarben, Periodenmarker (neutral in grau)
    legend_handles = [
        plt.Line2D([0], [0], color="gray", linestyle="--", linewidth=1.3,
                   label="vollständige Abschöpfung (y = x)"),
        plt.Line2D([0], [0], marker="o", linestyle="", color=COLOR_SAHEL,
                   markeredgecolor="black", markersize=7,
                   label="Sahel-Kernländer (MLI, BFA, NER, TCD, MRT)"),
        plt.Line2D([0], [0], marker="o", linestyle="", color=COLOR_OTHER,
                   markersize=6, alpha=0.7,
                   label="Übrige Subsahara-Afrika-Länder"),
        plt.Line2D([0], [0], marker=PERIOD_MARKERS["2000–2007"], linestyle="",
                   color="black", markerfacecolor="none", markersize=7,
                   label="Periode 2000–2007"),
        plt.Line2D([0], [0], marker=PERIOD_MARKERS["2008–2014"], linestyle="",
                   color="black", markerfacecolor="none", markersize=7,
                   label="Periode 2008–2014"),
        plt.Line2D([0], [0], marker=PERIOD_MARKERS["2015–2021"], linestyle="",
                   color="black", markerfacecolor="none", markersize=7,
                   label="Periode 2015–2021"),
    ]
    ax.legend(handles=legend_handles, fontsize=8.5, frameon=True, loc="upper left")

    fig.savefig(FIG_PATH, dpi=300, bbox_inches="tight")

    print(f"Länder gesamt: {n_countries}, Länder-Perioden-Punkte: {n_points}")
    print(f"Davon Sahel: {n_sahel_countries} Länder, {n_sahel_points} Punkte")
    print(f"Außerhalb des Achsenbereichs (> {AXIS_LIMIT} % BIP): {n_outside} Punkte -> {outside_labels}")
    print(f"Gespeichert: {FIG_PATH}")


if __name__ == "__main__":
    main()
