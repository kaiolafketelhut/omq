import random

print("=== OMQ EAL311 - DU rätst! ===")
print("Kai Olaf Ketelhut - Berlin")
zahl = random.randint(1, 100)
versuche = 0

while True:
    try:
        tipp = int(input("Dein Tipp (1-100): "))
    except:
        print("Nur Zahlen!")
        continue
    versuche += 1
    if tipp < zahl:
        print("⬆️ ZU KLEIN! Höher!")
    elif tipp > zahl:
        print("⬇️ ZU GROSS! Tiefer!")
    else:
        print(f"🎉 RICHTIG! Zahl war {zahl} in {versuche} Versuchen!")
        break
