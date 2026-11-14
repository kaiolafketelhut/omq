print("="*42)
print("  OMQ GTA v14 - OMQ INFINITY ♾️")
print("="*42)
geld = 0
wanted = 0
print("UNENDLICHKEIT! Alles gleichzeitig! Alle Welten, alle Zeiten, alle Träume!")
print("1=Infinity-Rennen 2=Infinity-Heist 3=Infinity-Flucht 4=INFINITY-MISSION 5=Reset 6=Garage 0=Aussteigen")
while True:
    w = input("\nOMQ INFINITY > ")
    if w == "1":
        print("♾️ INFINITY-RENNEN! Du rast durch ALLE Welten gleichzeitig - unendlich schnell!")
        geld += 15000; wanted += 1
    elif w == "2":
        print("♾️ INFINITY-HEIST! Du klaust ALLE Banken in ALLEN Universen!")
        geld += 18000; wanted += 1
    elif w == "3":
        print("♾️ INFINITY-FLUCHT! Unendlich viele Cops - du entkommst allen!")
        geld += 20000; wanted += 1
    elif w == "4":
        print("🎯 INFINITY-MISSION: Das unendliche Imperium stehlen! Der Infinity-Coup!")
        print("INFINITY-COUP GESCHAFFT! +200000$!")
        geld += 200000; wanted += 3
    elif w == "5":
        print("🔄 INFINITY-RESET! Alles auf Null - aber du behältst das Geld!")
        wanted = 0
        print("Wanted: 0 - Wieder frei!")
    elif w == "6":
        print(f"=== GARAGE INFINITY === Geld: {geld}$ | Wanted: {'⭐'*wanted}")
        print("Auto: OMQ INFINITY-AUTO | Alles: UNENDLICH!")
    elif w == "0":
        print(f"Game Over! Du hast {geld}$ in OMQ Infinity verdient!")
        break
    else:
        print("1 bis 6 oder 0 tippen!")
    print(f"Geld: {geld}$ | Wanted: {'⭐'*wanted}")
    if wanted >= 6:
        print("\n💥 BUSTED in der Unendlichkeit! Game Over!")
        print(f"Endstand: {geld}$")
        break
