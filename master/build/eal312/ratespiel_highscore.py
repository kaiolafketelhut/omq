import random, os, json

print("=== OMQ EAL312 - Schwierigkeit + Highscore ===")
print("Kai Olaf Ketelhut - Berlin")

print("1 = Leicht  1-10   (3 Versuche)")
print("2 = Mittel  1-100  (7 Versuche)")
print("3 = Schwer  1-1000 (10 Versuche)")
wahl = input("Wähle 1/2/3: ")

if wahl == "1":
    max_zahl, max_versuche = 10, 3
    level = "LEICHT"
elif wahl == "3":
    max_zahl, max_versuche = 1000, 10
    level = "SCHWER"
else:
    max_zahl, max_versuche = 100, 7
    level = "MITTEL"

zahl = random.randint(1, max_zahl)
print(f"\nLevel {level}: 1-{max_zahl}, du hast {max_versuche} Versuche!")

for versuch in range(1, max_versuche + 1):
    tipp = int(input(f"Versuch {versuch}/{max_versuche} - Dein Tipp: "))
    if tipp < zahl:
        print("⬆️ ZU KLEIN!")
    elif tipp > zahl:
        print("⬇️ ZU GROSS!")
    else:
        print(f"🎉 RICHTIG! {zahl} in {versuch} Versuchen! Level {level}")
        # Highscore speichern
        try:
            with open("highscore.json", "r") as f:
                scores = json.load(f)
        except:
            scores = []
        scores.append({"level": level, "versuche": versuch, "zahl": zahl})
        scores = sorted(scores, key=lambda x: x["versuche"])[:5]
        with open("highscore.json", "w") as f:
            json.dump(scores, f, indent=2)
        print("🏆 Highscore gespeichert!")
        print(scores)
        break
else:
    print(f"💀 Verloren! Zahl war {zahl}")
