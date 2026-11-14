print("="*42)
print("  OMQ GTA v18 - OMQ OMNIVERSE 🌌")
print("="*42)
geld = 0
wanted = 0
print("OMNIVERSE! ALLE Universen zusammen! Du bist der Herr aller Universen!")
print("1=Omniverse-Rennen 2=Omniverse-Heist 3=Omniverse-Flucht 4=OMNIVERSE-MISSION 5=Omniverse-Reset 6=Garage 0=Aussteigen")
while True:
    w = input("\nOMQ OMNIVERSE > ")
    if w == "1":
        print("🌌 OMNIVERSE-RENNEN! Du rast durch ALLE Universen gleichzeitig!")
        geld += 80000; wanted += 1
    elif w == "2":
        print("🌌 OMNIVERSE-HEIST! Du klaust ALLE Universen!")
        geld += 90000; wanted += 1
    elif w == "3":
        print("🌌 OMNIVERSE-FLUCHT! Du entkommst aus ALLEN Universen!")
        geld += 100000; wanted += 1
    elif w == "4":
        print("🎯 OMNIVERSE-MISSION: ALLE Universen stehlen! Der Omniverse-Coup!")
        print("OMNIVERSE-COUP GESCHAFFT! +600000$!")
        geld += 600000; wanted += 3
    elif w == "5":
        print("🔄 Omniverse-Reset! Alle Universen neu, gleiche Kohle!")
        wanted = 0
        print("Wanted: 0 - Wieder frei!")
    elif w == "6":
        print(f"=== GARAGE OMNIVERSE === Geld: {geld}$ | Wanted: {'⭐'*wanted}")
        print("Auto: OMQ OMNIVERSE-AUTO | Universen: ALLE!")
    elif w == "0":
        print(f"Game Over! Du hast {geld}$ in OMQ Omniverse verdient!")
        break
    else:
        print("1 bis 6 oder 0 tippen!")
    print(f"Geld: {geld}$ | Wanted: {'⭐'*wanted}")
    if wanted >= 6:
        print("\n💥 BUSTED im Omniverse! Game Over!")
        print(f"Endstand: {geld}$")
        break
