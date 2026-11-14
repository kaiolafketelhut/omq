print("="*42)
print("  OMQ GTA v8 - OMQ WORLD 🌍")
print("="*42)
geld = 0
wanted = 0
print("DIE WELT! Berlin + Tokyo + New York + OMQ City!")
print("1=Berlin 2=Tokyo 3=New York 4=WELT-MISSION 5=Verstecken 6=Garage 0=Aussteigen")
while True:
    w = input("\nOMQ WORLD > ")
    if w == "1":
        print("🇩🇪 BERLIN! Du rast am Brandenburger Tor vorbei - Currywurst-Power!")
        geld += 800; wanted += 1
    elif w == "2":
        print("🇯🇵 TOKYO! Neon-Lichter, Drift durch Shibuya - Mega!")
        geld += 900; wanted += 1
    elif w == "3":
        print("🗽 NEW YORK! Times Square Chaos - Taxi-Drift!")
        geld += 1000; wanted += 1
    elif w == "4":
        print("🎯 WELT-MISSION: Alle Kontinente gleichzeitig ausrauben! Der Welt-Coup!")
        print("WELT-COUP GESCHAFFT! +15000$!")
        geld += 15000; wanted += 3
    elif w == "5":
        print("🌍 Du versteckst dich im OMQ HQ in Berlin... Sicher!")
        wanted = 0
        print("Wanted: 0 - Wieder frei!")
    elif w == "6":
        print(f"=== GARAGE WORLD === Geld: {geld}$ | Wanted: {'⭐'*wanted}")
        print("Auto: OMQ GT GOLD | Jet: OMQ JET WORLD | Alles!")
    elif w == "0":
        print(f"Game Over! Du hast {geld}$ in OMQ World verdient!")
        break
    else:
        print("1 bis 6 oder 0 tippen!")
    print(f"Geld: {geld}$ | Wanted: {'⭐'*wanted}")
    if wanted >= 6:
        print("\n💥 BUSTED in OMQ World! Game Over!")
        print(f"Endstand: {geld}$")
        break
