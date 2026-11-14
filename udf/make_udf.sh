#!/bin/sh
# make_udf.sh - main.udf: the KDP profile in a UDF (+ISO 9660) image, the file system BD discs use.
# usage: sh make_udf.sh [main.udf]       needs genisoimage (Debian: apt install genisoimage)
OUT=${1:-main.udf}
D=$(mktemp -d)
trap 'rm -rf "$D"' EXIT
printf '=== KDP Forum Profile ===\r\nNickname : KDPMember:KL5UQ4f48673352\r\nCode     : KL5UQ4f48673352\r\nRole     : Member\r\nPoints   : 1\r\n' > "$D/MAIN.TXT"
command -v genisoimage >/dev/null || { echo "genisoimage not found (Debian: apt install genisoimage)"; exit 1; }
genisoimage -quiet -udf -iso-level 3 -V OMQ -o "$OUT" "$D" || exit 1
ls -l "$OUT"
command -v file >/dev/null && file "$OUT"
command -v isoinfo >/dev/null && isoinfo -l -i "$OUT" | head -12
