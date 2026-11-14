import random, time
print("=== OMQ EAL322 - SPEED-RUN ===")
print("Wie schnell bist du? Zeit laeuft!")
print("1-100, so wenig Versuche + so schnell wie moeglich!")
print("")

zahl = random.randint(1,100)
versuche = 0
start = time.time()

while True:
    try:
        t = int(input("Dein Tipp: "))
    except:
        print("Zahl eingeben!")
        continue
    versuche += 1
    if t < zahl:
        print("ZU KLEIN! ⬆️")
    elif t > zahl:
        print("ZU GROSS! ⬇️")
    else:
        break

ende = time.time()
dauer = round(ende - start, 1)
print("")
print(f"🎉 GESCHAFFT! Zahl: {zahl}")
print(f"Versuche: {versuche}")
print(f"Zeit: {dauer} Sekunden!")

# Bewertung
if dauer < 10 and versuche <= 5:
    print("🏆 OMQ BLITZ-CHAMPION! Unmenschlich schnell!")
elif dauer < 20:
    print("⚡ OMQ SPEED-STAR! Richtig schnell!")
elif dauer < 40:
    print("👍 OMQ SOLIDE! Gut dabei!")
else:
    print("🐢 OMQ GEMUETLICH! Naechstes Mal schneller!")

# Score
score = max(0, 1000 - int(dauer*10) - versuche*20)
print(f"Dein Score: {score} Punkte")
