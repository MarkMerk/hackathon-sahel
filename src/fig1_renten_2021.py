"""Abbildung 1: Rohstoffrenten (% des BIP) 2021 je SSA-Land, Sahel markiert.

Datenquelle: data/processed/panel.csv (Schema siehe docs/Forschungsdesign.md §4).
Erzeugt figures/fig1_renten_2021.png (dpi=300, bbox_inches="tight").
"""

import matplotlib.pyplot as plt
import pandas as pd

PANEL_PATH = "data/processed/panel.csv"
FIG_PATH = "figures/fig1_renten_2021.png"

# Farbenblindenfreundliche Palette (Okabe-Ito)
COLOR_SAHEL = "#D55E00"  # orange
COLOR_OTHER = "#0072B2"  # blau


def main():
    df = pd.read_csv(PANEL_PATH)
    d2021 = df[df["year"] == 2021].copy()
    d2021 = d2021[d2021["rents_pct_gdp"].notna()]
    d2021 = d2021.sort_values("rents_pct_gdp", ascending=True)

    n_countries = len(d2021)
    n_sahel = int(d2021["sahel"].sum())

    colors = d2021["sahel"].map({True: COLOR_SAHEL, False: COLOR_OTHER})

    # 16 cm Breite, Höhe proportional zur Länderzahl (~40+ Länder -> ca. 20 cm)
    fig_width_in = 16 / 2.54
    fig_height_in = max(20, n_countries * 0.42) / 2.54

    fig, ax = plt.subplots(figsize=(fig_width_in, fig_height_in))

    ax.barh(d2021["country"], d2021["rents_pct_gdp"], color=colors, height=0.7)

    ax.set_xlabel("Rohstoffrenten (% des BIP)", fontsize=10)
    ax.set_ylabel("")
    ax.tick_params(axis="both", labelsize=9)
    ax.tick_params(axis="y", labelsize=9)

    # Sahel-Länder im Ranking zusätzlich mit ISO3 beschriften
    for y_pos, (_, row) in enumerate(d2021.iterrows()):
        if row["sahel"]:
            ax.text(
                row["rents_pct_gdp"] + max(d2021["rents_pct_gdp"]) * 0.01,
                y_pos,
                row["iso3"],
                va="center",
                ha="left",
                fontsize=9,
                color=COLOR_SAHEL,
                fontweight="bold",
            )

    ax.set_xlim(0, d2021["rents_pct_gdp"].max() * 1.08)

    legend_handles = [
        plt.Rectangle((0, 0), 1, 1, color=COLOR_SAHEL, label="Sahel-Kernländer (MLI, BFA, NER, TCD, MRT)"),
        plt.Rectangle((0, 0), 1, 1, color=COLOR_OTHER, label="Übrige Subsahara-Afrika-Länder"),
    ]
    ax.legend(handles=legend_handles, loc="lower right", fontsize=9, frameon=True)

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis="x", linestyle="--", alpha=0.3)
    ax.set_axisbelow(True)

    fig.savefig(FIG_PATH, dpi=300, bbox_inches="tight")

    print(f"Länder dargestellt: {n_countries} (davon Sahel: {n_sahel})")
    print(f"Gespeichert: {FIG_PATH}")


if __name__ == "__main__":
    main()
