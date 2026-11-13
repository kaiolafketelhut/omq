import random

print("=== OMQ EAL313 - DUELL: DU vs COMPUTER ===")
print("Kai Olaf Ketelhut - Berlin")
print("Gleiche Zahl! Wer braucht weniger Versuche?")

zahl = random.randint(1, 100)
print("\nZahl ist zwischen 1-100. LOS!")

# DEIN PART
versuche_du = 0
while True:
    tipp = int(input("DU - Dein Tipp: "))
    versuche_du += 1
    if tipp < zahl:
        print("⬆️ ZU KLEIN!")
    elif tipp > zahl:
        print("⬇️ ZU GROSS!")
    else:
        print(f"🎉 DU hast es in {versuche_du} Versuchen!")
        break

# COMPUTER PART - Binary Search
print("\n--- Jetzt der COMPUTER ---")
low, high = 1, 100
versuche_pc = 0
while low <= high:
    tipp_pc = (low + high) // 2
    versuche_pc += 1
    print(f"PC rät: {tipp_pc}")
    if tipp_pc < zahl:
        print("⬆️ ZU KLEIN!")
        low = tipp_pc + 1
    elif tipp_pc > zahl:
        print("⬇️ ZU GROSS!")
        high = tipp_pc - 1
    else:
        print(f"🤖 PC hat es in {versuche_pc} Versuchen!")
        break

# SIEGER
print("\n=== ERGEBNIS ===")
print(f"DU: {versuche_du} Versuche")
print(f"PC: {versuche_pc} Versuche")
if versuche_du < versuche_pc:
    print("🏆 DU GEWINNST! MENSCH SCHLÄGT MASCHINE!")
elif versuche_du > versuche_pc:
    print("🤖 PC GEWINNT! Maschine ist schneller...")
else:
    print("🤝 UNENTSCHIEDEN! Gleich stark!")
