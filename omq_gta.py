print("="*40)
print("  OMQ GTA v1.0 - LIBERTY OMQ CITY")
print("="*40)
geld = 0
wanted = 0
print("Du bist in Liberty OMQ City! Was machst du?")
print("1=Fahren  2=Mission  3=Polizei entkommen  4=Garage  0=Aussteigen")

while True:
    w = input("\nOMQ GTA > ")
    if w == "1":
        print("🚗 Du fährst durch die Stadt... BRUMM BRUMM!")
        geld += 50
        wanted += 1
        print(f"+50$ | Geld: {geld}$ | Wanted: {'⭐'*wanted}")
    elif w == "2":
        print("🎯 MISSION: Bring das Paket in 60 Sekunden!")
        print("Mission geschafft! +500$!")
        geld += 500
        wanted += 2
        print(f"Geld: {geld}$ | Wanted: {'⭐'*wanted}")
    elif w == "3":
        if wanted == 0:
            print("Du bist sauber. Kein Bulle hinter dir.")
        else:
            print("🚓🚓 Du versteckst dich in der Garage... Geschafft!")
            wanted = 0
            print("Wanted: 0 - Du bist wieder frei!")
    elif w == "4":
        print(f"=== GARAGE === Geld: {geld}$ | Wanted: {'⭐'*wanted}")
        print("Dein Auto: OMQ GT - Farbe: GOLD v3.0.0")
    elif w == "0":
        print(f"Game Over! Du hast {geld}$ verdient! OMQ GTA OUT!")
        break
    else:
        print("1,2,3,4 oder 0 tippen!")

    if wanted >= 5:
        print("\n💥 BUSTED! Die Polizei hat dich! Game Over!")
        print(f"Endstand: {geld}$")
        break
