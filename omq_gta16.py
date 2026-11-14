print("="*42)
print("  OMQ GTA v16 - OMQ ETERNITY ⏳")
print("="*42)
geld = 0
wanted = 0
print("EWIGKEIT! Nach der Legende kommt die Ewigkeit! Du lebst für immer!")
print("1=Ewigkeits-Rennen 2=Ewigkeits-Heist 3=Ewigkeits-Flucht 4=ETERNITY-MISSION 5=Ewigkeits-Schlaf 6=Garage 0=Aussteigen")
while True:
    w = input("\nOMQ ETERNITY > ")
    if w == "1":
        print("⏳ EWIGKEITS-RENNEN! Du rast für immer - niemals müde, niemals langsam!")
        geld += 40000; wanted += 1
    elif w == "2":
        print("⏳ EWIGKEITS-HEIST! Du klaust für die Ewigkeit - unendlich reich!")
        geld += 45000; wanted += 1
    elif w == "3":
        print("⏳ EWIGKEITS-FLUCHT! Du entkommst für immer - keiner kriegt dich je!")
        geld += 50000; wanted += 1
    elif w == "4":
        print("🎯 ETERNITY-MISSION: Das ewige Imperium stehlen! Der Eternity-Coup!")
        print("ETERNITY-COUP GESCHAFFT! +400000$!")
        geld += 400000; wanted += 3
    elif w == "5":
        print("😴 Ewigkeits-Schlaf! 1000 Jahre schlafen - und frisch aufwachen!")
        wanted = 0
        print("Wanted: 0 - Wieder frei!")
    elif w == "6":
        print(f"=== GARAGE ETERNITY === Geld: {geld}$ | Wanted: {'⭐'*wanted}")
        print("Auto: OMQ ETERNITY-AUTO | Leben: UNENDLICH!")
    elif w == "0":
        print(f"Game Over! Du hast {geld}$ in OMQ Eternity verdient!")
        break
    else:
        print("1 bis 6 oder 0 tippen!")
    print(f"Geld: {geld}$ | Wanted: {'⭐'*wanted}")
    if wanted >= 6:
        print("\n💥 BUSTED in der Ewigkeit! Game Over!")
        print(f"Endstand: {geld}$")
        break
