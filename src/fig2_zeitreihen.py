"""Abbildung 2: Zeitreihen der Capture Ratio (3-Jahres-Mittel) je Sahel-Kernland
gegen Median und Interquartilsband der uebrigen Subsahara-Afrika-Laender.

Datenquelle: data/processed/panel.csv (Schema siehe docs/Forschungsdesign.md §4).
Erzeugt figures/fig2_zeitreihen.png (dpi=300, bbox_inches="tight").
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

PANEL_PATH = "data/processed/panel.csv"
FIG_PATH = "figures/fig2_zeitreihen.png"

SAHEL_CORE = ["MLI", "BFA", "NER", "TCD", "MRT"]

# Farbenblindenfreundliche Palette (Okabe-Ito), je Sahel-Land eine eigene Farbe
# plus Marker zur zusaetzlichen Unterscheidung.
SAHEL_STYLE = {
    "MLI": {"color": "#D55E00", "marker": "o"},  # orange
    "BFA": {"color": "#009E73", "marker": "s"},  # gruen
    "NER": {"color": "#CC79A7", "marker": "^"},  # rosa
    "TCD": {"color": "#E69F00", "marker": "D"},  # gelb-orange
    "MRT": {"color": "#0072B2", "marker": "v"},  # blau
}
COLOR_COMP_LINE = "#000000"
COLOR_COMP_BAND = "#56B4E9"  # hellblau, farbenblindenfreundlich


def main():
    df = pd.read_csv(PANEL_PATH)

    # Vergleichsgruppe: uebriges Subsahara-Afrika ohne Sahel-Kernlaender und
    # ohne die Sensitivitaets-Laender SDN/SEN (sahel_ext == False).
    comp = df[df["sahel_ext"] == False].copy()
    comp = comp.dropna(subset=["capture_ratio_3y"])

    comp_stats = (
        comp.groupby("year")["capture_ratio_3y"]
        .agg(median="median", q1=lambda s: s.quantile(0.25), q3=lambda s: s.quantile(0.75), n="count")
        .reset_index()
        .sort_values("year")
    )
    n_comp_countries = comp["iso3"].nunique()
    n_comp_obs = len(comp)

    # 16 cm Breite
    fig_width_in = 16 / 2.54
    fig_height_in = 10 / 2.54
    fig, ax = plt.subplots(figsize=(fig_width_in, fig_height_in))

    # Hintergrund: IQR-Band und Median der Vergleichsgruppe
    ax.fill_between(
        comp_stats["year"],
        comp_stats["q1"],
        comp_stats["q3"],
        color=COLOR_COMP_BAND,
        alpha=0.35,
        label="Übrige SSA: Interquartilsband (Q1–Q3)",
        zorder=1,
    )
    ax.plot(
        comp_stats["year"],
        comp_stats["median"],
        color=COLOR_COMP_LINE,
        linewidth=1.8,
        linestyle="-",
        label="Übrige SSA: Median",
        zorder=2,
    )

    # Sahel-Kernlaender: je Land eine Linie, Luecken bleiben Luecken (kein
    # Ueberbruecken fehlender Jahre - daher explizit ueber die vorhandenen
    # Jahre plotten, ohne Reindexing auf den vollen Bereich).
    all_years = np.arange(2000, 2022)
    n_sahel_obs = 0
    for iso in SAHEL_CORE:
        sub = df[df["iso3"] == iso].sort_values("year")
        if sub.empty:
            continue
        # Auf vollen Jahresbereich reindexieren, damit matplotlib Luecken
        # (fehlende Jahre, z. B. MRT 2008-2011) NICHT ueberbrueckt, sondern
        # die Linie dort unterbricht (NaN statt interpolierter Verbindung).
        series = sub.set_index("year")["capture_ratio_3y"].reindex(all_years)
        n_sahel_obs += int(series.notna().sum())
        style = SAHEL_STYLE[iso]
        ax.plot(
            all_years,
            series.values,
            color=style["color"],
            marker=style["marker"],
            markersize=4,
            linewidth=1.8,
            label=iso,
            zorder=3,
        )

    # Hilfslinie bei 1,0 (vollstaendige Abschoepfung)
    ax.axhline(1.0, color="gray", linestyle="--", linewidth=1.0, alpha=0.6, zorder=0)

    ax.set_xlabel("Jahr", fontsize=10)
    ax.set_ylabel(
        "Abschöpfungsquote (Ressourceneinnahmen / Rohstoffrenten)", fontsize=10
    )
    ax.tick_params(axis="both", labelsize=9)

    ax.set_xlim(2000, 2021)
    # Jahre als ganze Zahlen beschriften (sonst "2000.0")
    ax.set_xticks(range(2000, 2022, 3))
    ax.set_xticklabels([str(j) for j in range(2000, 2022, 3)])
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis="y", linestyle="--", alpha=0.3)
    ax.set_axisbelow(True)

    # Legende unter die Grafik, damit sie den Ausschlag Mauretaniens 2019
    # (Quote nahe 0,9) nicht verdeckt.
    ax.legend(fontsize=9, frameon=False, ncol=3,
              loc="upper center", bbox_to_anchor=(0.5, -0.13))

    fig.savefig(FIG_PATH, dpi=300, bbox_inches="tight")

    print(f"Vergleichsgruppe: {n_comp_countries} Länder, {n_comp_obs} Länderjahre")
    print(f"Sahel-Kernländer: {len(SAHEL_CORE)} Länder, {n_sahel_obs} Länderjahre")
    print(f"Gespeichert: {FIG_PATH}")


if __name__ == "__main__":
    main()
