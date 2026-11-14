print("="*42)
print("  OMQ GTA v19 - OMQ BEYOND 🌌")
print("="*42)
geld = 0
wanted = 0
print("BEYOND! Jenseits des Omniverse! Jenseits von ALLEM! Du bist BEYOND!")
print("1=Beyond-Rennen 2=Beyond-Heist 3=Beyond-Flucht 4=BEYOND-MISSION 5=Beyond-Reset 6=Garage 0=Aussteigen")
while True:
    w = input("\nOMQ BEYOND > ")
    if w == "1":
        print("🌌 BEYOND-RENNEN! Du rast jenseits von ALLEM!")
        geld += 100000; wanted += 1
    elif w == "2":
        print("🌌 BEYOND-HEIST! Du klaust das Jenseits!")
        geld += 110000; wanted += 1
    elif w == "3":
        print("🌌 BEYOND-FLUCHT! Du entkommst aus dem Jenseits!")
        geld += 120000; wanted += 1
    elif w == "4":
        print("🎯 BEYOND-MISSION: Das Jenseits stehlen! Der Beyond-Coup!")
        print("BEYOND-COUP GESCHAFFT! +700000$!")
        geld += 700000; wanted += 3
    elif w == "5":
        print("🔄 Beyond-Reset! Jenseits neu, gleiche Kohle!")
        wanted = 0
        print("Wanted: 0 - Wieder frei!")
    elif w == "6":
        print(f"=== GARAGE BEYOND === Geld: {geld}$ | Wanted: {'⭐'*wanted}")
        print("Auto: OMQ BEYOND-AUTO | Ort: Jenseits von ALLEM!")
    elif w == "0":
        print(f"Game Over! Du hast {geld}$ in OMQ Beyond verdient!")
        break
    else:
        print("1 bis 6 oder 0 tippen!")
    print(f"Geld: {geld}$ | Wanted: {'⭐'*wanted}")
    if wanted >= 6:
        print("\n💥 BUSTED jenseits von ALLEM! Game Over!")
        print(f"Endstand: {geld}$")
        break
