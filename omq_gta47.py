print("="*42)
print("  OMQ GTA v47 - OMQ INFINITY 15 ♾️")
print("="*42)
geld = 0
wanted = 0
print("INFINITY 15! Die Unendlichkeit zum 15. Mal! 47. GTA Spiel! Du bist Unendlichkeit x15!")
print("1=Infinity-Rennen 2=Infinity-Heist 3=Infinity-Flucht 4=INFINITY-MISSION 5=Infinity-Reset 6=Garage 0=Aussteigen")
while True:
    w = input("\nOMQ INFINITY 15 > ")
    if w == "1":
        print("♾️ INFINITY-RENNEN! Du rast durch die Unendlichkeit zum 15. Mal!")
        geld += 800000; wanted += 1
    elif w == "2":
        print("♾️ INFINITY-HEIST! Du klaust die Unendlichkeit zum 15. Mal!")
        geld += 810000; wanted += 1
    elif w == "3":
        print("♾️ INFINITY-FLUCHT! Du entkommst aus der Unendlichkeit zum 15. Mal!")
        geld += 820000; wanted += 1
    elif w == "4":
        print("🎯 INFINITY-MISSION: Die Unendlichkeit 15x stehlen! Der Infinity-Coup 15!")
        print("INFINITY-COUP 15 GESCHAFFT! +22000000$!")
        geld += 22000000; wanted += 3
    elif w == "5":
        print("🔄 Infinity-Reset! Unendlichkeit neu, gleiche Kohle!")
        wanted = 0
        print("Wanted: 0 - Wieder frei!")
    elif w == "6":
        print(f"=== GARAGE INFINITY 15 === Geld: {geld}$ | Wanted: {'⭐'*wanted}")
        print("Auto: OMQ INFINITY 15-AUTO | Spiele: 47 GTA Spiele!")
    elif w == "0":
        print(f"Game Over! Du hast {geld}$ in OMQ Infinity 15 verdient!")
        break
    else:
        print("1 bis 6 oder 0 tippen!")
    print(f"Geld: {geld}$ | Wanted: {'⭐'*wanted}")
    if wanted >= 6:
        print("\n💥 BUSTED in der Unendlichkeit 15! Game Over!")
        print(f"Endstand: {geld}$")
        break
