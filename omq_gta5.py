print("="*42)
print("  OMQ GTA v5 - VICE OMQ CITY 2 🌴")
print("="*42)
geld = 0
wanted = 0
print("Zurück in Vice! Yacht, Strand, Drogenbaron!")
print("1=Yacht 2=Strand-Rennen 3=Jet-Ski 4=Mission 5=Verstecken 6=Garage 0=Aussteigen")
while True:
    w = input("\nVICE 2 > ")
    if w == "1":
        print("🛥️ YACHT-PARTY! Du feierst auf deiner Yacht mit 100 Leuten!")
        geld += 400; wanted += 1
    elif w == "2":
        print("🏖️ STRAND-RENNEN! Du rast am Strand entlang - alle schauen!")
        geld += 350; wanted += 1
    elif w == "3":
        print("🌊 JET-SKI! Du springst über Wellen! Mega Sprünge!")
        geld += 600; wanted += 2
    elif w == "4":
        print("🎯 MISSION: Drogenbaron in Vice City stürzen! Große Sache!")
        print("BARON BESIEGT! +4000$!")
        geld += 4000; wanted += 3
    elif w == "5":
        print("🌴 Du versteckst dich in deiner Villa... Sicher!")
        wanted = 0
        print("Wanted: 0 - Wieder frei!")
    elif w == "6":
        print(f"=== GARAGE VICE 2 === Geld: {geld}$ | Wanted: {'⭐'*wanted}")
        print("Auto: OMQ GT GOLD | Yacht: OMQ YACHT 2 | Jet-Ski: OMQ WAVE")
    elif w == "0":
        print(f"Game Over! Du hast {geld}$ in Vice 2 verdient!")
        break
    else:
        print("1 bis 6 oder 0 tippen!")
    print(f"Geld: {geld}$ | Wanted: {'⭐'*wanted}")
    if wanted >= 6:
        print("\n💥 BUSTED in Vice 2! Game Over!")
        print(f"Endstand: {geld}$")
        break
