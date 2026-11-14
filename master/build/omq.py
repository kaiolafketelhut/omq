#!/usr/bin/env python3
"""omq.py - a BDXL-sized FAT32 image with 2048-byte sectors, stored as a tiny sector map.

A 200 GB image cannot live in git (GitHub blocks files over 100 MB), but almost every sector of it is
zero. So the repo keeps omq.BDXL.map - only the sectors that hold data (about 16 KB) - and this
script expands it into a sparse image on your own disk, where the zeros cost nothing.

usage: python3 omq.py                   write omq.BDXL.map here, expand it to $TMPDIR/omq.BDXL, check it
       python3 omq.py 128               same with 128 GB (100 and 128 are the real BDXL sizes)
       python3 omq.py expand MAP IMAGE  turn a map into a sparse image
       python3 omq.py check IMAGE       read MAIN.TXT back out of an image
Layout: FAT32, 2048-byte sectors, 16 sectors (32 KiB) per cluster, label OMQBDXL, file MAIN.TXT.
Real BDXL discs use UDF; this is a FAT-style raw 2K-sector image as asked.
"""
import os
import struct
import sys
import tempfile

S = 2048                      # bytes per sector (optical "2K raw")
SPC = 16                      # sectors per cluster
RESERVED = 32
ID = "KDPMember:KL5UQ4f48673352"
TEXT = ("=== KDP Forum Profile ===\r\nNickname : %s\r\nCode     : %s\r\n"
        "Role     : Member\r\nPoints   : 1\r\n" % (ID, ID[len("KDPMember:"):])).encode("ascii")
MAGIC = b"OMQS"


def geometry(total):
    fatsz = 1
    while True:
        clusters = (total - RESERVED - 2 * fatsz) // SPC
        need = -(-((clusters + 2) * 4) // S)
        if need == fatsz:
            return fatsz, clusters
        fatsz = need


def records(total):
    fatsz, clusters = geometry(total)
    assert clusters >= 65525
    data_start = RESERVED + 2 * fatsz

    boot = bytearray(S)
    boot[0:3] = b"\xEB\x58\x90"
    boot[3:11] = b"OMQBDXL "
    struct.pack_into("<HBHBHHBHHHII", boot, 11, S, SPC, RESERVED, 2, 0, 0, 0xF8, 0, 63, 255, 0, total)
    struct.pack_into("<IHHIHH12sBBBI11s8s", boot, 36, fatsz, 0, 0, 2, 1, 6, b"", 0x80, 0, 0x29,
                     0x4F4D5142, b"OMQBDXL    ", b"FAT32   ")
    boot[510:512] = b"\x55\xAA"

    fsinfo = bytearray(S)
    struct.pack_into("<I", fsinfo, 0, 0x41615252)
    struct.pack_into("<I", fsinfo, 484, 0x61417272)
    struct.pack_into("<II", fsinfo, 488, clusters - 2, 4)
    fsinfo[508:512] = b"\x00\x00\x55\xAA"

    fat = bytearray(S)
    for i, v in enumerate((0x0FFFFFF8, 0x0FFFFFFF, 0x0FFFFFFF, 0x0FFFFFFF)):   # media, EOC, root, MAIN.TXT
        struct.pack_into("<I", fat, i * 4, v)

    root = bytearray(S)
    root[0:11] = b"OMQBDXL    "
    root[11] = 0x08
    date = ((2026 - 1980) << 9) | (11 << 5) | 5
    e = bytearray(32)
    e[0:11] = b"MAIN    TXT"
    e[11] = 0x20
    struct.pack_into("<HHHHI", e, 20, 0, 0, date, 3, len(TEXT))
    struct.pack_into("<H", e, 18, date)
    root[32:64] = e

    filedata = TEXT.ljust(S, b"\x00")
    return [(0, bytes(boot)), (1, bytes(fsinfo)), (6, bytes(boot)), (7, bytes(fsinfo)),
            (RESERVED, bytes(fat)), (RESERVED + fatsz, bytes(fat)),
            (data_start, bytes(root)), (data_start + SPC, filedata)]


def write_map(path, total):
    recs = records(total)
    with open(path, "wb") as f:
        f.write(MAGIC + struct.pack("<QII", total, S, len(recs)))
        for sector, data in recs:
            f.write(struct.pack("<Q", sector) + data)
    return os.path.getsize(path)


def expand(map_path, image):
    with open(map_path, "rb") as f:
        assert f.read(4) == MAGIC, "not an OMQS map"
        total, ss, count = struct.unpack("<QII", f.read(16))
        with open(image, "wb") as out:
            out.truncate(total * ss)                 # sparse: no space used for the zeros
            for _ in range(count):
                (sector,) = struct.unpack("<Q", f.read(8))
                out.seek(sector * ss)
                out.write(f.read(ss))
    return total * ss


def check(image):
    with open(image, "rb") as f:
        boot = f.read(S)
        bps, spc, rsv, nfat = struct.unpack_from("<HBHB", boot, 11)
        total = struct.unpack_from("<I", boot, 32)[0]
        fatsz, root_cl = struct.unpack_from("<I", boot, 36)[0], struct.unpack_from("<I", boot, 44)[0]
        label = boot[71:82].decode().strip()
        data_start = rsv + nfat * fatsz
        f.seek((data_start + (root_cl - 2) * spc) * bps)
        root = f.read(bps)
        for i in range(0, bps, 32):
            e = root[i:i + 32]
            if e[0] in (0, 0xE5) or e[11] & 0x08:
                continue
            cl = (struct.unpack_from("<H", e, 20)[0] << 16) | struct.unpack_from("<H", e, 26)[0]
            size = struct.unpack_from("<I", e, 28)[0]
            f.seek((data_start + (cl - 2) * spc) * bps)
            return label, bps, spc, total, e[0:8].decode().strip() + "." + e[8:11].decode().strip(), f.read(size)


if __name__ == "__main__":
    args = sys.argv[1:]
    if args[:1] == ["expand"]:
        print("expanded to %.1f GB logical" % (expand(args[1], args[2]) / 1e9))
    elif args[:1] == ["check"]:
        args = args[1:]
        image = args[0]
        label, bps, spc, total, name, data = check(image)
        print("%s: label %s, %d-byte sectors, %d sectors/cluster, %.1f GB" % (image, label, bps, spc, total * bps / 1e9))
        print("--- /%s ---" % name)
        print(data.decode("ascii").replace("\r\n", "\n"), end="")
    else:
        gb = float(args[0]) if args else 200.0
        total = int(gb * 1e9) // S
        size = write_map("omq.BDXL.map", total)
        image = os.path.join(tempfile.gettempdir(), "omq.BDXL")
        logical = expand("omq.BDXL.map", image)
        print("wrote omq.BDXL.map (%d bytes) - this is what goes into git" % size)
        print("expanded %s: %.1f GB logical, %d bytes on disk" % (image, logical / 1e9, os.stat(image).st_blocks * 512))
        label, bps, spc, tot, name, data = check(image)
        print("FAT32 volume %s: %d-byte sectors, %d sectors/cluster, %d clusters" % (label, bps, spc, geometry(tot)[1]))
        print("--- /%s ---" % name)
        print(data.decode("ascii").replace("\r\n", "\n"), end="")
