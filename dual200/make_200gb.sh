#!/bin/sh
# make_200gb.sh - Ritek 200GB = 2x 100GB Triple-Layer, double-sided
# Side A + Side B = 2 Images, Disc muss umgedreht werden!
OUT_A=${1:-dual200/sideA_main.udf}
OUT_B=${2:-dual200/sideB_omq.udf}
D_A=$(mktemp -d); D_B=$(mktemp -d)
trap 'rm -rf "$D_A" "$D_B"' EXIT
printf '=== KDP Forum Profile ===\r\nNickname : KDPMember:KL5UQ4f48673352\r\nCode     : KL5UQ4f48673352\r\nRole     : Member\r\nPoints   : 1\r\nSIDE     : A - 100GB Triple-Layer\r\n' > "$D_A/MAIN.TXT"
printf '=== OMQ Games ===\r\nSIDE     : B - 100GB Triple-Layer\r\n' > "$D_B/OMQ.TXT"
cp -r eal320 eal321 eal322 eal323 eal324 "$D_B/" 2>/dev/null || true
genisoimage -quiet -udf -iso-level 3 -V OMQ_SIDE_A -o "$OUT_A" "$D_A"
genisoimage -quiet -udf -iso-level 3 -V OMQ_SIDE_B -o "$OUT_B" "$D_B"
ls -lh "$OUT_A" "$OUT_B"
