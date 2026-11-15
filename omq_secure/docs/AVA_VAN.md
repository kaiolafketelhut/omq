# AVA_VAN.4 - Vulnerability Analysis
# OMQ Secure Core v1.0 - EAL4+

## Angreifer-Modell
- Angreifer: Spieler mit Root / Admin-Zugriff auf eigenes Gerät
- Fähigkeiten: Kann Dateien lesen, ändern, Code dekompilieren, Debugger nutzen
- Ziel: Geldstand fälschen, Passwort umgehen, Signatur fälschen
- Zeit / Mittel: Hoch - Wochen, eigene Tools, kein Geheimnis außer Passwort

## Analysierte Schwachstellen

### VAN-01: Savegame direkt editieren
- Angriff: JSON öffnen, geld auf 999.999.999 ändern
- Ergebnis: ABGEWEHRT - HMAC-SHA256 Prüfung schlägt fehl, Laden verweigert
- Getestet: test_secure_core.py PASS 4/5

### VAN-02: Falsches Passwort / Bruteforce
- Angriff: Viele Passwörter probieren
- Ergebnis: TEILWEISE - Aktuell kein Rate-Limit in v1.0!
- Massnahme für v1.1: FIA_AFL.1 - Nach 5 Fehlversuchen 60s Sperre + Counter in Datei
- Status: OFFEN - muss vor Labor gefixt werden!

### VAN-03: Key aus Code auslesen
- Angriff: Secret Key im Code suchen
- Ergebnis: ABGEWEHRT - Kein Key im Code! Key wird nur aus Passwort via PBKDF2 abgeleitet, lebt nur im RAM
- Getestet: grep -r "secret\|key =" src/ -> kein Hardcoded Key

### VAN-04: Replay - Altes Savegame wieder einspielen
- Angriff: Altes Savegame mit mehr Geld wieder einspielen
- Ergebnis: ABGEWEHRT - Monotoner Counter in omq_secure_counter.txt
- Getestet: Counter 4 in v40.0.0

### VAN-05: Timing-Angriff auf Passwort-Vergleich
- Angriff: Zeit messen, um Passwort zu raten
- Ergebnis: ABGEWEHRT - hmac.compare_digest, zeitkonstant

### VAN-06: Code-Tampering - omq_secure_core.py ändern
- Angriff: Selbsttest rauskommentieren
- Ergebnis: TEILWEISE - selftest() prüft Hash, aber Hash ist nicht extern signiert
- Massnahme für v1.1: Externe Signatur / signierte Git-Tags (git tag -s) + Hash in Release-Notes
- Status: OFFEN - muss vor Labor gefixt werden!

## Fazit für Labor
- 4 von 6 Angriffe abgewehrt
- 2 OFFENE Punkte: FIA_AFL.1 Rate-Limit + Externe Signatur
- Diese 2 fixen wir in v41.1.0, dann ist AVA_VAN.4 bereit für Labor-Prüfung
