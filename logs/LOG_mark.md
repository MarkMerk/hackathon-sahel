# LOG — Mark

Format: `HH:MM · Aufgabe · Modell/Subagent · Ergebnis oder „verworfen, weil …“`

- ~09:40 · Aufgabenstellung gelesen, Tagesplan und Vorlagen erstellt · Claude Fable 5.1 (Cowork) · Plan, CLAUDE.md-Vorlage, Prompts, Zeichenzähler
- ~10:00–10:40 · Themenfindung: 6 Vorschläge (Claude) + je 5 von Leon und Philip (mit KI) verglichen · Claude Opus 5 (Cowork) · gewählt: „Wer schöpft die Rohstoffrenten ab?“; verworfen u. a. ML-Prognose (zu wenige Länder), Solar-/Abhängigkeitsindex (Gewichtung willkürlich), Konflikte (ACLED-Registrierung, Kausalität), Uran-Fallstudie (n = 1)
- ~10:45 · Datenverfügbarkeit geprüft · Claude Opus 5 (Websuche) · WDI-Renten Sahel bis 2021; GRD 2023 bis 2021/22 → Fenster 2000–2021; APIs aus Sandbox per Proxy blockiert → manuelle Downloads
- ~11:19 · Git-Repository, CLAUDE.md, Forschungsdesign, Sitzungsleitfäden, Subagenten angelegt · Claude Opus 5 (Cowork) · Repo-Grundstruktur steht
- 12:16 · Sitzung gestartet, Einweisung per /start · Claude Opus 4.6 (Claude Code) · Stand: `data/raw/` leer, `src/` leer → Schritt 2 (Downloads) aus sessions/MARK.md ist überfällig, Entscheidungspunkt 12:15 verschoben
- 12:25 · `src/01_laden.py` und `src/02_abdeckung.py` vorab geschrieben, während die Downloads noch ausstehen · Claude Opus 4.6 (Claude Code) · beide Skripte gegen synthetische Rohdaten in `/tmp` getestet (nicht im Repo): Schema §4 vollständig, Capture Ratio = res_rev/rents rechnerisch geprüft, Renten-Mindestniveau 1 % greift, zentriertes 3-Jahres-Mittel läuft nicht über Ländergrenzen, Perioden korrekt geschnitten; beide Zweige des Entscheidungspunkts (GRD / Plan B) lösen richtig aus. Spaltennamen von GRD und HDR werden über Kandidatenlisten gesucht, weil die echten Namen je Version abweichen — nach dem Download mit `daten-pruefer` gegenprüfen.

## KI-Fehler und Korrekturen

## Verworfene Ansätze
