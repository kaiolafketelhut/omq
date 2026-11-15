# ALC_FLR.1 - Flaw Remediation - Bugfix-Prozess
# OMQ Secure Core v1.0 - EAL4+

## Prozess bei Bug / Schwachstelle
1. Bug wird in GitHub Issue gemeldet (mit Version, Schritte, Log)
2. Entwickler bestätigt in 48h, Schweregrad: Kritisch / Hoch / Mittel / Niedrig
3. Fix auf eigenem Branch, kein direkter Push auf main
4. Tests laufen: python3 omq_secure/tests/test_secure_core.py - muss 5/5 bestehen
5. Neues Release mit Patch-Version, z.B. v40.0.1
6. User werden in Release-Notes informiert

## Bekannte Fälle
- Phase 2: Tamper-Test mit 999.999.999$ -> korrekt abgelehnt
- Phase 3: Altes manipuliertes Savegame -> korrekt mit 0$ neu gestartet, danach sauber 52.000.000$ gesichert
