print("="*42)
print("  OMQ GTA v17 - OMQ UNIVERSE 2 🌌")
print("="*42)
geld = 0
wanted = 0
print("UNIVERSE 2! Das Universum neu gestartet! Noch größer, noch wilder!")
print("1=Universe-Rennen 2=Universe-Heist 3=Universe-Flucht 4=UNIVERSE-MISSION 5=Universe-Reset 6=Garage 0=Aussteigen")
while True:
    w = input("\nOMQ UNIVERSE 2 > ")
    if w == "1":
        print("🌌 UNIVERSE-RENNEN! Du rast durch ein NEUES Universum!")
        geld += 60000; wanted += 1
    elif w == "2":
        print("🌌 UNIVERSE-HEIST! Du klaust ein ganzes neues Universum!")
        geld += 70000; wanted += 1
    elif w == "3":
        print("🌌 UNIVERSE-FLUCHT! Du entkommst aus dem neuen Universum!")
        geld += 80000; wanted += 1
    elif w == "4":
        print("🎯 UNIVERSE-MISSION: Das neue Universum stehlen! Der Universe-Coup!")
        print("UNIVERSE-COUP GESCHAFFT! +500000$!")
        geld += 500000; wanted += 3
    elif w == "5":
        print("🔄 Universe-Reset! Neues Universum, gleiche Kohle!")
        wanted = 0
        print("Wanted: 0 - Wieder frei!")
    elif w == "6":
        print(f"=== GARAGE UNIVERSE 2 === Geld: {geld}$ | Wanted: {'⭐'*wanted}")
        print("Auto: OMQ UNIVERSE 2-AUTO | Universum: 2.0!")
    elif w == "0":
        print(f"Game Over! Du hast {geld}$ in OMQ Universe 2 verdient!")
        break
    else:
        print("1 bis 6 oder 0 tippen!")
    print(f"Geld: {geld}$ | Wanted: {'⭐'*wanted}")
    if wanted >= 6:
        print("\n💥 BUSTED im neuen Universum! Game Over!")
        print(f"Endstand: {geld}$")
        break
