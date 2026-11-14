import subprocess, os, sys
print("=== OMQ BURNER SUITE v2.7.0 ===")
print("Ritek BD-R XL 200GB - Dual 2x100GB")
print("Side A = KDP Profil | Side B = OMQ Spiele")
print("")

def run(cmd):
    print(f"\n> {cmd}")
    os.system(cmd)

while True:
    print("\n--- MENU ---")
    print("1. Side A brennen (MAIN.UDF - KDP Profil)")
    print("2. Side B brennen (OMQ.UDF - Spiele) - NACH UMDREHEN!")
    print("3. Disc pruefen (Welche Seite ist drin?)")
    print("4. Dry-Run Test (ohne Brennen - Sicher!)")
    print("5. Images pruefen (Groesse + UDF)")
    print("0. Beenden")
    w = input("\nWahl: ").strip()

    if w == "1":
        print("\n⚠️  LEERE Ritek 200GB einlegen, Seite A oben!")
        ok = input("Bereit? (j/n): ")
        if ok.lower() == "j":
            run("proot-distro login debian --bind ~/omq:/repo -- bash -c 'growisofs -dvd-compat -Z /dev/sr0=/repo/dual200/sideA_main.udf' < /dev/null")
            print("\n✅ Seite A fertig! Jetzt DISC UMDREHEN!")
    elif w == "2":
        print("\n⚠️  Disc UMGEDREHT? Seite B oben?")
        ok = input("Bereit? (j/n): ")
        if ok.lower() == "j":
            run("proot-distro login debian --bind ~/omq:/repo -- bash -c 'growisofs -dvd-compat -Z /dev/sr0=/repo/dual200/sideB_omq.udf' < /dev/null")
            print("\n✅ Seite B fertig! 200GB DUAL FERTIG!")
    elif w == "3":
        run("proot-distro login debian --bind ~/omq:/repo -- bash -c 'isoinfo -d -i /dev/sr0' < /dev/null")
        print("\nWenn OMQ_SIDE_A steht = Seite A drin")
        print("Wenn OMQ_SIDE_B steht = Seite B drin")
    elif w == "4":
        print("\n🧪 Dry-Run - brennt NICHT, nur Test!")
        run("proot-distro login debian --bind ~/omq:/repo -- bash -c 'growisofs -dry-run -Z /dev/sr0=/repo/dual200/sideA_main.udf' < /dev/null")
    elif w == "5":
        run("ls -lh dual200/")
        run("file dual200/*.udf")
    elif w == "0":
        print("OMQ Burner geschlossen! 💿")
        break
    else:
        print("1-5 oder 0 waehlen!")
