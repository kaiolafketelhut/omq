#!/bin/sh
set -e
mkdir -p master/build
cp -r eal* master/build/ 2>/dev/null || true
cp -r burner master/build/ 2>/dev/null || true
cp *.py master/build/ 2>/dev/null || true
cp *.md master/build/ 2>/dev/null || true
cat > master/build/MASTER_README.txt << 'END'
OMQ MASTER v2.8.0 - ALLE SPIELE IN 1!

EAL318 - Rate Spiel
EAL319 - Rate Spiel
EAL320 - ?
EAL321 - BDXL 64k
EAL322 - Speed
EAL323 - Rangliste - 711 Punkte
EAL324 - Hard Mode - 1 bis 1000, 1 Leben
MAIN.UDF - KDP Profil
DUAL 200GB - Side A + Side B
Burner Suite - Brennen wie ImgBurn!

Alle OMQ Spiele. Ein Image. Ein Master!
END
ls -R master/build | head -n 100
