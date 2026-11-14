print("="*42)
print("  OMQ GTA v9 - OMQ GALAXY 🚀")
print("="*42)
geld = 0
wanted = 0
print("DIE GALAXY! Mond + Mars + OMQ Station!")
print("1=Mond 2=Mars 3=OMQ Station 4=GALAXY-MISSION 5=Verstecken 6=Garage 0=Aussteigen")
while True:
    w = input("\nOMQ GALAXY > ")
    if w == "1":
        print("🌙 MOND! Du rast über den Mond - Schwerelosigkeit-Drift!")
        geld += 1200; wanted += 1
    elif w == "2":
        print("🔴 MARS! Roter Staub, Alien-Rennen - Mega!")
        geld += 1500; wanted += 1
    elif w == "3":
        print("🛰️ OMQ STATION! Weltraum-Station - Laser-Chaos!")
        geld += 2000; wanted += 1
    elif w == "4":
        print("🎯 GALAXY-MISSION: Die ganze Galaxie gleichzeitig ausrauben! Der Galaxy-Coup!")
        print("GALAXY-COUP GESCHAFFT! +25000$!")
        geld += 25000; wanted += 3
    elif w == "5":
        print("🚀 Du versteckst dich in der OMQ Rakete... Sicher!")
        wanted = 0
        print("Wanted: 0 - Wieder frei!")
    elif w == "6":
        print(f"=== GARAGE GALAXY === Geld: {geld}$ | Wanted: {'⭐'*wanted}")
        print("Auto: OMQ GT GOLD | Rakete: OMQ RAKETE | UFO: OMQ UFO | Alles!")
    elif w == "0":
        print(f"Game Over! Du hast {geld}$ in OMQ Galaxy verdient!")
        break
    else:
        print("1 bis 6 oder 0 tippen!")
    print(f"Geld: {geld}$ | Wanted: {'⭐'*wanted}")
    if wanted >= 6:
        print("\n💥 BUSTED in OMQ Galaxy! Game Over!")
        print(f"Endstand: {geld}$")
        break
