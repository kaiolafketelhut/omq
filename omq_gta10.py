print("="*42)
print("  OMQ GTA v10 - OMQ MULTIVERSE 🌀")
print("="*42)
geld = 0
wanted = 0
print("DAS MULTIVERSE! Parallel-Universen! Du bist überall gleichzeitig!")
print("1=Universum A 2=Universum B 3=Universum C 4=MULTIVERSE-MISSION 5=Verstecken 6=Garage 0=Aussteigen")
while True:
    w = input("\nOMQ MULTIVERSE > ")
    if w == "1":
        print("🅰️ UNIVERSUM A! Du rast durch eine Welt wo alles aus Gold ist!")
        geld += 2000; wanted += 1
    elif w == "2":
        print("🅱️ UNIVERSUM B! Hier bist du der Bürgermeister von OMQ City!")
        geld += 2500; wanted += 1
    elif w == "3":
        print("🅲 UNIVERSUM C! Hier fliegen Autos und Geld fällt vom Himmel!")
        geld += 3000; wanted += 1
    elif w == "4":
        print("🎯 MULTIVERSE-MISSION: Alle Universen gleichzeitig ausrauben! Der Multiverse-Coup!")
        print("MULTIVERSE-COUP GESCHAFFT! +40000$!")
        geld += 40000; wanted += 3
    elif w == "5":
        print("🌀 Du springst in ein anderes Universum... Sicher!")
        wanted = 0
        print("Wanted: 0 - Wieder frei!")
    elif w == "6":
        print(f"=== GARAGE MULTIVERSE === Geld: {geld}$ | Wanted: {'⭐'*wanted}")
        print("Auto: OMQ GT MULTIVERSE | UFO: OMQ UFO 2 | Alles in allen Universen!")
    elif w == "0":
        print(f"Game Over! Du hast {geld}$ in OMQ Multiverse verdient!")
        break
    else:
        print("1 bis 6 oder 0 tippen!")
    print(f"Geld: {geld}$ | Wanted: {'⭐'*wanted}")
    if wanted >= 6:
        print("\n💥 BUSTED im Multiverse! Game Over!")
        print(f"Endstand: {geld}$")
        break
