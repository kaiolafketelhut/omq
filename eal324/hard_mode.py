import random
print("=== OMQ EAL324 - HARD MODE ===")
print("1 bis 1000! Nur 10 Leben!")
print("Ein Fehler = 1 Leben weg!")
print("")

zahl = random.randint(1,1000)
leben = 10
versuche = 0

while leben > 0:
    print(f"\nLeben: {'❤️'*leben} ({leben})")
    try: t = int(input("Tipp 1-1000: "))
    except:
        print("Zahl eingeben!")
        continue
    versuche += 1
    if t == zahl:
        print(f"\n🎉 UNGLAUBLICH! Zahl {zahl} in {versuche} Versuchen!")
        print(f"Du hast noch {leben} Leben uebrig!")
        if leben >= 8: print("🏆 OMQ HARDCORE-LEGENDE!")
        elif leben >= 5: print("⚡ OMQ HARD-PROFI!")
        else: print("👍 OMQ UEBERLEBENSKUENSTLER!")
        break
    leben -= 1
    if t < zahl: print("ZU KLEIN! ⬆️")
    else: print("ZU GROSS! ⬇️")
    if leben > 0:
        print(f"Noch {leben} Leben! Weiter!")
else:
    print(f"\n💀 GAME OVER! Die Zahl war {zahl}")
    print("Hard Mode ist brutal - versuch es nochmal!")

print(f"\nDein Run: {versuche} Versuche")
