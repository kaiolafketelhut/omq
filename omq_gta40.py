print("="*42)
print("  OMQ GTA v40 - OMQ ETERNITY 12 ⏳")
print("="*42)
geld = 0
wanted = 0
print("ETERNITY 12! Die Ewigkeit zum 12. Mal! 40. GTA Spiel - JUBILÄUM! Du bist Ewigkeit x12!")
print("1=Eternity-Rennen 2=Eternity-Heist 3=Eternity-Flucht 4=ETERNITY-MISSION 5=Eternity-Reset 6=Garage 0=Aussteigen")
while True:
    w = input("\nOMQ ETERNITY 12 > ")
    if w == "1":
        print("⏳ ETERNITY-RENNEN! Du rast durch die Ewigkeit zum 12. Mal!")
        geld += 590000; wanted += 1
    elif w == "2":
        print("⏳ ETERNITY-HEIST! Du klaust die Ewigkeit zum 12. Mal!")
        geld += 600000; wanted += 1
    elif w == "3":
        print("⏳ ETERNITY-FLUCHT! Du entkommst aus der Ewigkeit zum 12. Mal!")
        geld += 610000; wanted += 1
    elif w == "4":
        print("🎯 ETERNITY-MISSION: Die Ewigkeit 12x stehlen! Der Eternity-Coup 12!")
        print("ETERNITY-COUP 12 GESCHAFFT! +15000000$!")
        geld += 15000000; wanted += 3
    elif w == "5":
        print("🔄 Eternity-Reset! Ewigkeit neu, gleiche Kohle!")
        wanted = 0
        print("Wanted: 0 - Wieder frei!")
    elif w == "6":
        print(f"=== GARAGE ETERNITY 12 === Geld: {geld}$ | Wanted: {'⭐'*wanted}")
        print("Auto: OMQ ETERNITY 12-AUTO | Spiele: 40 GTA Spiele - JUBILÄUM!")
    elif w == "0":
        print(f"Game Over! Du hast {geld}$ in OMQ Eternity 12 verdient!")
        break
    else:
        print("1 bis 6 oder 0 tippen!")
    print(f"Geld: {geld}$ | Wanted: {'⭐'*wanted}")
    if wanted >= 6:
        print("\n💥 BUSTED in der Ewigkeit 12! Game Over!")
        print(f"Endstand: {geld}$")
        break
