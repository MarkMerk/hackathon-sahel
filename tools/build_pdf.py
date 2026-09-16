#!/usr/bin/env python3
"""Baut die beiden Abgabe-PDFs aus den Markdown-Entwürfen (pandoc -> XeLaTeX, biblatex-apa).

Aufruf:  python tools/build_pdf.py
Ergebnis: abgabe/Abhandlung.pdf, abgabe/Reflexion.pdf (+ Zeichenzählung aus dem fertigen PDF)

Format laut docs/Arbeitsauftrag.pdf: Arial 12 pt einheitlich, Zeilenabstand 1,5, Ränder 2,5 cm,
Deckblatt, Inhaltsverzeichnis, Literaturverzeichnis (APA 7), Anhang. Sprache Deutsch.
Nebenbei wird text/anhang/D_tabellen.md aus tables/ und figures/captions.md neu erzeugt.
"""
from __future__ import annotations

import re
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / "build"
OUT = ROOT / "abgabe"

# Deckblatt — bei Bedarf Nachnamen/Matrikelnummern ergänzen
TEAM = r"Mark Merkouchev \\ Leon \\ Philip"
DATUM = "16. September 2026"
TITEL = "Wer schöpft die Rohstoffrenten ab?"
UNTERTITEL = ("Der Anteil staatlicher Ressourceneinnahmen an den Rohstoffrenten "
              "in den Sahel-Staaten im Vergleich zu Subsahara-Afrika (2000--2021)")
KONTEXT = ("Fachlicher Kontext: Data Science -- deskriptiv-vergleichende "
           "Panelanalyse offener Sekundärdaten")

ABSCHNITTE = ["00_abstract", "01_einleitung", "02_theorie", "03_forschungsstand",
              "04_methodik", "05_1_deskriptiv", "05_2_gruppenvergleich", "05_3_hdi",
              "05_4_robustheit", "06_diskussion", "07_limitationen", "08_fazit"]
ANHANG = ["A_code", "B_datenquellen", "C_suchprotokoll", "D_tabellen", "E_prompts"]

QUELLE = "Quelle: World Bank WDI, UNU-WIDER GRD 2025{hdi}; eigene Darstellung; Details in Anhang D.6."
# (Datei, Titel, Anmerkung, HDI-Quelle?) — Kurzfassung im Text, ausführlich in Anhang D.6
ABB = {
    1: ("fig1_renten_2021.png",
        "Rohstoffrenten 2021 je Land in Prozent des BIP",
        "Sahel-Kernländer hervorgehoben; n = 46.", False),
    2: ("fig2_zeitreihen.png",
        "Abschöpfungsquote im Sahel und im übrigen Subsahara-Afrika, 2000--2021",
        "Dreijahresmittel; Lücken nicht überbrückt.", False),
    3: ("fig3_streudiagramm.png",
        "Rohstoffrenten und Ressourceneinnahmen in Prozent des BIP",
        "Länder-Periodenmittel; gestrichelt: vollständige Abschöpfung; n = 70.", False),
    4: ("fig4_boxplot.png",
        "Abschöpfungsquote nach Periode und Ländergruppe",
        "Länder-Periodenmittel.", False),
    5: ("fig5_hdi.png",
        "Abschöpfungsquote und Index der menschlichen Entwicklung",
        "Länder-Periodenmittel; Assoziation.", True),
}
# Abbildung(en) nach dem ersten Absatz einfügen, der das Muster enthält
EINFUEGEN = {
    "05_1_deskriptiv": [(r"\(Abb\. 1\)", [1]), (r"Abbildung 2 zeigt", [2, 3])],
    "05_2_gruppenvergleich": [(r"Abb\. 4", [4])],
    "05_3_hdi": [(r"Abb\. 5", [5])],
}

VORSPANN = r"""
\documentclass[12pt,a4paper]{article}
\usepackage[a4paper,margin=2.5cm]{geometry}
\usepackage{fontspec}
\defaultfontfeatures{Ligatures=TeX}
\setmainfont{Arial}[Path=/System/Library/Fonts/Supplemental/,Extension=.ttf,UprightFont=*,BoldFont=* Bold,ItalicFont=* Italic,BoldItalicFont=* Bold Italic]
\setsansfont{Arial}[Path=/System/Library/Fonts/Supplemental/,Extension=.ttf,UprightFont=*,BoldFont=* Bold,ItalicFont=* Italic,BoldItalicFont=* Bold Italic]
\setmonofont{Arial}[Path=/System/Library/Fonts/Supplemental/,Extension=.ttf,UprightFont=*,BoldFont=* Bold,ItalicFont=* Italic,BoldItalicFont=* Bold Italic]
\usepackage[ngerman]{babel}
\usepackage[autostyle,german=quotes]{csquotes}
\usepackage[style=apa,backend=biber]{biblatex}
\addbibresource{quellen.bib}
\usepackage{setspace}
\onehalfspacing
\usepackage{graphicx,float,longtable,booktabs,array,calc,xurl}
\usepackage{fvextra}
\fvset{breaklines=true,breakanywhere=true,fontsize=\normalsize}
\usepackage[hidelinks]{hyperref}
\usepackage{titlesec}
\titleformat{\section}{\normalfont\normalsize\bfseries}{}{0pt}{}
\titleformat{\subsection}{\normalfont\normalsize\bfseries}{}{0pt}{}
\titleformat{\subsubsection}{\normalfont\normalsize\bfseries\itshape}{}{0pt}{}
\titlespacing*{\section}{0pt}{18pt}{6pt}
\titlespacing*{\subsection}{0pt}{12pt}{4pt}
\titlespacing*{\subsubsection}{0pt}{8pt}{2pt}
\setcounter{secnumdepth}{0}
\setcounter{tocdepth}{2}
\setlength{\parindent}{0pt}
\setlength{\parskip}{6pt}
\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
\setlength{\LTleft}{0pt}\setlength{\LTright}{0pt}
\renewcommand{\arraystretch}{1.0}
\urlstyle{same}
\raggedbottom
\sloppy
"""


def md_lesen(p: Path) -> str:
    t = p.read_text(encoding="utf-8")
    return re.sub(r"<!--.*?-->", "", t, flags=re.S)


def abbildung(n: int) -> str:
    datei, titel, anm, hdi = ABB[n]
    q = QUELLE.format(hdi=", UNDP HDI" if hdi else "")
    return (
        "\n```{=latex}\n\\begin{figure}[H]\n\\raggedright\n"
        f"\\textbf{{Abbildung {n}}}\\par\n\\textit{{{titel}}}\\par\\smallskip\n"
        f"\\includegraphics[width=\\linewidth,height=0.5\\textheight,keepaspectratio]{{{ROOT / 'figures' / datei}}}\\par\n"
        f"\\textit{{Anmerkung.}} {anm} {q}\\par\n"
        "\\end{figure}\n```\n"
    )


def abschnitt(name: str) -> str:
    t = md_lesen(ROOT / "text" / "abschnitte" / f"{name}.md")
    # „# 5.2 …“ ist inhaltlich ein Unterabschnitt
    t = re.sub(r"^# (\d+\.\d+ )", r"## \1", t, flags=re.M)
    for muster, nummern in EINFUEGEN.get(name, []):
        absaetze = t.split("\n\n")
        for i, a in enumerate(absaetze):
            if re.search(muster, a) and not a.lstrip().startswith("#"):
                absaetze[i] = a + "\n" + "".join(abbildung(n) for n in nummern)
                break
        else:
            raise SystemExit(f"Einfügestelle für Abb. {nummern} in {name} nicht gefunden")
        t = "\n\n".join(absaetze)
    return t


def tabelle_demote(t: str) -> str:
    return re.sub(r"^(#+) ", lambda m: "#" * (len(m.group(1)) + 1) + " ", t, flags=re.M)


def anhang_d_erzeugen() -> None:
    teile = ["# Anhang D — Tabellen und Erläuterungen zu den Abbildungen\n",
             "Alle Tabellen sind skriptgeneriert und unverändert aus `tables/` übernommen; "
             "die Skripte beschreibt Anhang A. Die Tabellennummern entsprechen den Verweisen im Text.\n"]
    quellen = [("D.1", "tab1_datenquellen", "`src/03_capture_ratio.py`"),
               ("D.2", "tab2_gruppenvergleich", "`src/04_gruppenvergleich.py`"),
               ("D.3", "tab2b_zusammenhang", "`src/05_zusammenhang_hdi.py`"),
               ("D.4", "tab3_robustheit", "`src/06_robustheit.py`"),
               ("D.5", "abdeckung", "`src/02_abdeckung.py`")]
    for nr, datei, skript in quellen:
        t = (ROOT / "tables" / f"{datei}.md").read_text(encoding="utf-8")
        t = re.sub(r"<!--.*?-->", "", t, flags=re.S).strip()
        erste, rest = t.split("\n", 1)
        titel = re.sub(r"^#\s*", "", erste).strip()
        if datei == "abdeckung":
            titel = "Tabelle 4 — " + titel
        titel = re.sub(r"^Tab\. ", "Tabelle ", titel)
        teile.append(f"## {nr} {titel}\n\nErzeugt von: {skript}\n\n{tabelle_demote(rest).strip()}\n")
    cap = (ROOT / "figures" / "captions.md").read_text(encoding="utf-8")
    cap = "\n".join(l for l in cap.splitlines() if not l.startswith("#")).strip()
    cap = re.sub(r"\*\*Abb\. (\d)\.\*\*", r"**Abbildung \1.**", cap)
    teile.append("## D.6 Erläuterungen zu den Abbildungen\n\n" + cap + "\n")
    (ROOT / "text" / "anhang" / "D_tabellen.md").write_text("\n".join(teile), encoding="utf-8")


def pandoc(md: str, ziel: Path) -> None:
    src = ziel.with_suffix(".md")
    src.write_text(md, encoding="utf-8")
    subprocess.run(["pandoc", str(src), "-f", "markdown-auto_identifiers+raw_attribute",
                    "-t", "latex", "--no-highlight", "--columns=20", "-o", str(ziel)], check=True)
    t = ziel.read_text(encoding="utf-8")
    t = t.replace("\\begin{verbatim}", "\\begin{Verbatim}").replace("\\end{verbatim}", "\\end{Verbatim}")
    ziel.write_text(t, encoding="utf-8")


def deckblatt(art: str) -> str:
    return rf"""
\begin{{titlepage}}
\centering
Justus-Liebig-Universität Gießen\par
AI Hackathon im AI Summercamp 2026\par
\vspace*{{3cm}}
{art}\par\vspace{{1cm}}
\textbf{{{TITEL}}}\par\vspace{{0.5cm}}
{UNTERTITEL}\par\vspace{{1cm}}
{KONTEXT}\par
\vfill
{TEAM}\par\vspace{{0.5cm}}
{DATUM}\par
\end{{titlepage}}
"""


def latex(pfad: Path) -> None:
    for _ in range(2):
        subprocess.run(["latexmk", "-xelatex", "-interaction=nonstopmode", "-halt-on-error",
                        pfad.name], cwd=BUILD, check=True, stdout=subprocess.DEVNULL)


def bib_vorbereiten() -> None:
    t = (ROOT / "text" / "quellen.bib").read_text(encoding="utf-8")
    # interne Arbeitsnotizen (note = {...}) nicht ins Literaturverzeichnis
    t = re.sub(r"^\s*note\s*=\s*\{(?:[^{}]|\{[^{}]*\})*\},?\s*$\n", "", t, flags=re.M)
    (BUILD / "quellen.bib").write_text(t, encoding="utf-8")


def zaehlen(pdf: Path, von: str, bis: str | None) -> int:
    txt = subprocess.run(["pdftotext", "-layout", str(pdf), "-"], capture_output=True,
                         text=True, check=True).stdout
    # Inhaltsverzeichnis überspringen: ab dem zweiten Vorkommen des Startworts
    start = txt.find(von, txt.find(von) + 1) if txt.count(von) > 1 else txt.find(von)
    txt = txt[start:]
    if bis:
        txt = txt[: txt.find(bis)]
    zeilen = [re.sub(r"\s+", " ", l).strip() for l in txt.splitlines()]
    zeilen = [l for l in zeilen if l and not re.fullmatch(r"\d+", l)]
    return len("\n".join(zeilen))


def main() -> None:
    BUILD.mkdir(exist_ok=True)
    OUT.mkdir(exist_ok=True)
    bib_vorbereiten()
    anhang_d_erzeugen()

    pandoc("\n\n".join(abschnitt(a) for a in ABSCHNITTE), BUILD / "haupttext.tex")
    pandoc("\n\n".join(md_lesen(ROOT / "text" / "anhang" / f"{a}.md") + "\n\n```{=latex}\n\\clearpage\n```\n"
                       for a in ANHANG), BUILD / "anhang.tex")
    (BUILD / "Abhandlung.tex").write_text(VORSPANN + r"""
\begin{document}
""" + deckblatt("Wissenschaftliche Abhandlung") + r"""
\pagenumbering{roman}
\tableofcontents
\clearpage
\pagenumbering{arabic}
\input{haupttext}
\clearpage
\nocite{*}
\printbibliography[title=Literaturverzeichnis]
\clearpage
\input{anhang}
\end{document}
""", encoding="utf-8")

    refl = md_lesen(ROOT / "text" / "reflexion.md")
    refl = re.sub(r"^# .*\n", "", refl, count=1)
    refl = re.sub(r"^## ", "# ", refl, flags=re.M)
    pandoc(refl, BUILD / "reflexion_text.tex")
    (BUILD / "Reflexion.tex").write_text(VORSPANN + r"""
\begin{document}
""" + deckblatt("Dokumentation und Reflexion des Arbeits- und KI-Nutzungsprozesses") + r"""
\input{reflexion_text}
\end{document}
""", encoding="utf-8")

    for name in ["Abhandlung", "Reflexion"]:
        latex(BUILD / f"{name}.tex")
        shutil.copy(BUILD / f"{name}.pdf", OUT / f"{name}.pdf")

    n_abh = zaehlen(OUT / "Abhandlung.pdf", "Abstract", "Literaturverzeichnis")
    n_ref = zaehlen(OUT / "Reflexion.pdf", "Einordnung in den Studienstand", None)
    print(f"Abhandlung: {n_abh} Zeichen aus dem PDF (Abstract bis Literaturverzeichnis, inkl. "
          f"Überschriften, Abbildungstitel und Anmerkungen) — Limit 37.500")
    print(f"Reflexion:  {n_ref} Zeichen aus dem PDF (ohne Deckblatt) — Limit 12.500")


if __name__ == "__main__":
    main()
