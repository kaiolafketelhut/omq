print("="*42)
print("  OMQ GTA v45 - OMQ INFINITY 14 ♾️")
print("="*42)
geld = 0
wanted = 0
print("INFINITY 14! Die Unendlichkeit zum 14. Mal! 45. GTA Spiel! Du bist Unendlichkeit x14!")
print("1=Infinity-Rennen 2=Infinity-Heist 3=Infinity-Flucht 4=INFINITY-MISSION 5=Infinity-Reset 6=Garage 0=Aussteigen")
while True:
    w = input("\nOMQ INFINITY 14 > ")
    if w == "1":
        print("♾️ INFINITY-RENNEN! Du rast durch die Unendlichkeit zum 14. Mal!")
        geld += 740000; wanted += 1
    elif w == "2":
        print("♾️ INFINITY-HEIST! Du klaust die Unendlichkeit zum 14. Mal!")
        geld += 750000; wanted += 1
    elif w == "3":
        print("♾️ INFINITY-FLUCHT! Du entkommst aus der Unendlichkeit zum 14. Mal!")
        geld += 760000; wanted += 1
    elif w == "4":
        print("🎯 INFINITY-MISSION: Die Unendlichkeit 14x stehlen! Der Infinity-Coup 14!")
        print("INFINITY-COUP 14 GESCHAFFT! +20000000$!")
        geld += 20000000; wanted += 3
    elif w == "5":
        print("🔄 Infinity-Reset! Unendlichkeit neu, gleiche Kohle!")
        wanted = 0
        print("Wanted: 0 - Wieder frei!")
    elif w == "6":
        print(f"=== GARAGE INFINITY 14 === Geld: {geld}$ | Wanted: {'⭐'*wanted}")
        print("Auto: OMQ INFINITY 14-AUTO | Spiele: 45 GTA Spiele!")
    elif w == "0":
        print(f"Game Over! Du hast {geld}$ in OMQ Infinity 14 verdient!")
        break
    else:
        print("1 bis 6 oder 0 tippen!")
    print(f"Geld: {geld}$ | Wanted: {'⭐'*wanted}")
    if wanted >= 6:
        print("\n💥 BUSTED in der Unendlichkeit 14! Game Over!")
        print(f"Endstand: {geld}$")
        break
