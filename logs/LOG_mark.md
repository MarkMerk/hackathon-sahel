# LOG — Mark

Format: `HH:MM · Aufgabe · Modell/Subagent · Ergebnis oder „verworfen, weil …“`

- ~09:40 · Aufgabenstellung gelesen, Tagesplan und Vorlagen erstellt · Claude Fable 5.1 (Cowork) · Plan, CLAUDE.md-Vorlage, Prompts, Zeichenzähler
- ~10:00–10:40 · Themenfindung: 6 Vorschläge (Claude) + je 5 von Leon und Philip (mit KI) verglichen · Claude Opus 5 (Cowork) · gewählt: „Wer schöpft die Rohstoffrenten ab?“; verworfen u. a. ML-Prognose (zu wenige Länder), Solar-/Abhängigkeitsindex (Gewichtung willkürlich), Konflikte (ACLED-Registrierung, Kausalität), Uran-Fallstudie (n = 1)
- ~10:45 · Datenverfügbarkeit geprüft · Claude Opus 5 (Websuche) · WDI-Renten Sahel bis 2021; GRD 2023 bis 2021/22 → Fenster 2000–2021; APIs aus Sandbox per Proxy blockiert → manuelle Downloads
- ~11:19 · Git-Repository, CLAUDE.md, Forschungsdesign, Sitzungsleitfäden, Subagenten angelegt · Claude Opus 5 (Cowork) · Repo-Grundstruktur steht
- 12:16 · Sitzung gestartet, Einweisung per /start · Claude Opus 4.6 (Claude Code) · Stand: `data/raw/` leer, `src/` leer → Schritt 2 (Downloads) aus sessions/MARK.md ist überfällig, Entscheidungspunkt 12:15 verschoben
- 12:25 · `src/01_laden.py` und `src/02_abdeckung.py` vorab geschrieben, während die Downloads noch ausstehen · Claude Opus 4.6 (Claude Code) · beide Skripte gegen synthetische Rohdaten in `/tmp` getestet (nicht im Repo): Schema §4 vollständig, Capture Ratio = res_rev/rents rechnerisch geprüft, Renten-Mindestniveau 1 % greift, zentriertes 3-Jahres-Mittel läuft nicht über Ländergrenzen, Perioden korrekt geschnitten; beide Zweige des Entscheidungspunkts (GRD / Plan B) lösen richtig aus. Spaltennamen von GRD und HDR werden über Kandidatenlisten gesucht, weil die echten Namen je Version abweichen — nach dem Download mit `daten-pruefer` gegenprüfen.

- 12:32 · WDI (3 Indikatoren + Ländermetadaten) und UNDP HDI automatisch geladen · Claude Opus 4.6 (Claude Code, curl) · Die in `docs/Forschungsdesign.md` §1 notierte API-Blockade galt nur für die Sandbox-Umgebung; von Marks Rechner antwortet die World-Bank-API normal (HTTP 200). Vier WDI-Dateien aus den ZIPs entpackt und nach Namensschema abgelegt, HDI aus HDR 2025 (aktueller als der in DATA_DOWNLOAD.md verlinkte Stand). **GRD bleibt manuell:** wider.unu.edu antwortet auf alle direkten Pfade mit HTTP 403 (Cloudflare), das Formular ist nicht umgehbar.
- 12:33 · WDI-Dateien geprüft · Subagent `daten-pruefer` · 4 Kopfzeilen bei allen drei Indikatordateien (bestätigt `skiprows=4`), Region exakt „Sub-Saharan Africa“ mit 48 Ländern, Aggregate wie SSF/SSA/WLD haben ein leeres Regionsfeld und fallen beim Merge automatisch heraus; für alle sieben Sahel-Länder 22/22 Jahre in allen drei Indikatoren, Renten 2021 stimmen mit den Werten in §1 des Forschungsdesigns überein (TCD 21,3 · BFA 20,1 · MLI 18,4 · SDN 12,8 · MRT 11,5 · NER 6,4).

## KI-Fehler und Korrekturen
- 12:31 · **Kodierungsannahme falsch** · Claude Opus 4.6 · `lies_tabelle()` las CSV-Dateien nur als UTF-8. Die UNDP-HDR-Datei ist latin-1 kodiert (Byte 0xf4 in „Côte d'Ivoire“) und brach den Import ab. Korrigiert: Kodierungen werden der Reihe nach probiert (utf-8-sig, dann latin-1) mit Hinweis in der Konsole. Aufgefallen beim ersten Lesen der echten Datei — der synthetische Test hatte nur ASCII-Ländernamen enthalten und die Lücke deshalb nicht gezeigt.

## Verworfene Ansätze
