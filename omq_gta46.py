print("="*42)
print("  OMQ GTA v46 - OMQ ETERNITY 15 ⏳")
print("="*42)
geld = 0
wanted = 0
print("ETERNITY 15! Die Ewigkeit zum 15. Mal! 46. GTA Spiel! Du bist Ewigkeit x15!")
print("1=Eternity-Rennen 2=Eternity-Heist 3=Eternity-Flucht 4=ETERNITY-MISSION 5=Eternity-Reset 6=Garage 0=Aussteigen")
while True:
    w = input("\nOMQ ETERNITY 15 > ")
    if w == "1":
        print("⏳ ETERNITY-RENNEN! Du rast durch die Ewigkeit zum 15. Mal!")
        geld += 770000; wanted += 1
    elif w == "2":
        print("⏳ ETERNITY-HEIST! Du klaust die Ewigkeit zum 15. Mal!")
        geld += 780000; wanted += 1
    elif w == "3":
        print("⏳ ETERNITY-FLUCHT! Du entkommst aus der Ewigkeit zum 15. Mal!")
        geld += 790000; wanted += 1
    elif w == "4":
        print("🎯 ETERNITY-MISSION: Die Ewigkeit 15x stehlen! Der Eternity-Coup 15!")
        print("ETERNITY-COUP 15 GESCHAFFT! +21000000$!")
        geld += 21000000; wanted += 3
    elif w == "5":
        print("🔄 Eternity-Reset! Ewigkeit neu, gleiche Kohle!")
        wanted = 0
        print("Wanted: 0 - Wieder frei!")
    elif w == "6":
        print(f"=== GARAGE ETERNITY 15 === Geld: {geld}$ | Wanted: {'⭐'*wanted}")
        print("Auto: OMQ ETERNITY 15-AUTO | Spiele: 46 GTA Spiele!")
    elif w == "0":
        print(f"Game Over! Du hast {geld}$ in OMQ Eternity 15 verdient!")
        break
    else:
        print("1 bis 6 oder 0 tippen!")
    print(f"Geld: {geld}$ | Wanted: {'⭐'*wanted}")
    if wanted >= 6:
        print("\n💥 BUSTED in der Ewigkeit 15! Game Over!")
        print(f"Endstand: {geld}$")
        break
