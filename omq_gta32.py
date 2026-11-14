print("="*42)
print("  OMQ GTA v32 - OMQ ETERNITY 8 ⏳")
print("="*42)
geld = 0
wanted = 0
print("ETERNITY 8! Die Ewigkeit zum 8. Mal! 32. GTA Spiel! Du bist Ewigkeit x8!")
print("1=Eternity-Rennen 2=Eternity-Heist 3=Eternity-Flucht 4=ETERNITY-MISSION 5=Eternity-Reset 6=Garage 0=Aussteigen")
while True:
    w = input("\nOMQ ETERNITY 8 > ")
    if w == "1":
        print("⏳ ETERNITY-RENNEN! Du rast durch die Ewigkeit zum 8. Mal!")
        geld += 360000; wanted += 1
    elif w == "2":
        print("⏳ ETERNITY-HEIST! Du klaust die Ewigkeit zum 8. Mal!")
        geld += 370000; wanted += 1
    elif w == "3":
        print("⏳ ETERNITY-FLUCHT! Du entkommst aus der Ewigkeit zum 8. Mal!")
        geld += 380000; wanted += 1
    elif w == "4":
        print("🎯 ETERNITY-MISSION: Die Ewigkeit 8x stehlen! Der Eternity-Coup 8!")
        print("ETERNITY-COUP 8 GESCHAFFT! +7000000$!")
        geld += 7000000; wanted += 3
    elif w == "5":
        print("🔄 Eternity-Reset! Ewigkeit neu, gleiche Kohle!")
        wanted = 0
        print("Wanted: 0 - Wieder frei!")
    elif w == "6":
        print(f"=== GARAGE ETERNITY 8 === Geld: {geld}$ | Wanted: {'⭐'*wanted}")
        print("Auto: OMQ ETERNITY 8-AUTO | Spiele: 32 GTA Spiele!")
    elif w == "0":
        print(f"Game Over! Du hast {geld}$ in OMQ Eternity 8 verdient!")
        break
    else:
        print("1 bis 6 oder 0 tippen!")
    print(f"Geld: {geld}$ | Wanted: {'⭐'*wanted}")
    if wanted >= 6:
        print("\n💥 BUSTED in der Ewigkeit 8! Game Over!")
        print(f"Endstand: {geld}$")
        break
