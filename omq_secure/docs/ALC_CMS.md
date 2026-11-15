# ALC_CMS.4 + ALC_CMC.4 - Configuration Management
# OMQ Secure Core v1.0

## CM-System
- Tool: Git + GitHub
- Repo: github.com/kaiolafketelhut/omq
- Branch: main = Release-Branch, kein direkter Push ohne Commit-Message
- Tags: v38.0.0, v39.0.0, v40.0.0 - alle Releases getaggt

## CM-Liste - Was gehört zum TOE?
- omq_secure/src/omq_secure_core.py - TOE Code
- omq_gta_secure.py - TOE Anwendung
- omq_secure/docs/ST.md - Security Target
- omq_secure/docs/ADV_FSP.md, ADV_TDS.md, AGD_OPE.md, ALC_FLR.md, AVA_VAN.md
- omq_secure/tests/test_secure_core.py - Tests
- index.html - Webseite (NICHT im TOE, nur Info)

## Nachweis für Labor
- git log --oneline zeigt alle Änderungen
- git tag -l zeigt alle Versionen
- gh release list zeigt alle Auslieferungen
- Jede Änderung hat Commit-Message mit Version

## Auslieferung - ALC_DEL.1
- Auslieferung nur via GitHub Release, HTTPS
- User lädt nur von github.com/kaiolafketelhut/omq/releases
- Keine USB, keine E-Mail Anhänge
- Hash der Dateien steht in Release-Notes (zukünftig: SHA256 + GPG-Signatur)
