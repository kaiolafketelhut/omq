print("="*42)
print("  OMQ GTA v37 - OMQ INFINITY 10 ♾️")
print("="*42)
geld = 0
wanted = 0
print("INFINITY 10! Die Unendlichkeit zum 10. Mal! ZWEISTELLIG! 37. GTA Spiel! Du bist Unendlichkeit x10!")
print("1=Infinity-Rennen 2=Infinity-Heist 3=Infinity-Flucht 4=INFINITY-MISSION 5=Infinity-Reset 6=Garage 0=Aussteigen")
while True:
    w = input("\nOMQ INFINITY 10 > ")
    if w == "1":
        print("♾️ INFINITY-RENNEN! Du rast durch die Unendlichkeit zum 10. Mal!")
        geld += 500000; wanted += 1
    elif w == "2":
        print("♾️ INFINITY-HEIST! Du klaust die Unendlichkeit zum 10. Mal!")
        geld += 510000; wanted += 1
    elif w == "3":
        print("♾️ INFINITY-FLUCHT! Du entkommst aus der Unendlichkeit zum 10. Mal!")
        geld += 520000; wanted += 1
    elif w == "4":
        print("🎯 INFINITY-MISSION: Die Unendlichkeit 10x stehlen! Der Infinity-Coup 10!")
        print("INFINITY-COUP 10 GESCHAFFT! +12000000$!")
        geld += 12000000; wanted += 3
    elif w == "5":
        print("🔄 Infinity-Reset! Unendlichkeit neu, gleiche Kohle!")
        wanted = 0
        print("Wanted: 0 - Wieder frei!")
    elif w == "6":
        print(f"=== GARAGE INFINITY 10 === Geld: {geld}$ | Wanted: {'⭐'*wanted}")
        print("Auto: OMQ INFINITY 10-AUTO | Spiele: 37 GTA Spiele!")
    elif w == "0":
        print(f"Game Over! Du hast {geld}$ in OMQ Infinity 10 verdient!")
        break
    else:
        print("1 bis 6 oder 0 tippen!")
    print(f"Geld: {geld}$ | Wanted: {'⭐'*wanted}")
    if wanted >= 6:
        print("\n💥 BUSTED in der Unendlichkeit 10! Game Over!")
        print(f"Endstand: {geld}$")
        break
