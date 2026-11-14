print("="*42)
print("  OMQ GTA v12 - OMQ DREAM WORLD 💭")
print("="*42)
geld = 0
wanted = 0
print("TRAUMWELT! Hier kannst du ALLES! Fliegen, unsichtbar sein, Geld regnen lassen!")
print("1=Flug-Traum 2=Unsichtbar-Traum 3=Geldregen-Traum 4=DREAM-MISSION 5=Aufwachen 6=Garage 0=Aussteigen")
while True:
    w = input("\nOMQ DREAM WORLD > ")
    if w == "1":
        print("🦅 FLUG-TRAUM! Du fliegst über OMQ City - ohne Auto, einfach so!")
        geld += 5000; wanted += 1
    elif w == "2":
        print("👻 UNSICHTBAR-TRAUM! Niemand sieht dich - du klaust alles!")
        geld += 6000; wanted += 1
    elif w == "3":
        print("💸 GELDREGEN-TRAUM! Es regnet Geld vom Himmel - du sammelst alles!")
        geld += 8000; wanted += 1
    elif w == "4":
        print("🎯 DREAM-MISSION: Den ultimativen Traum stehlen! Der Dream-Coup!")
        print("DREAM-COUP GESCHAFFT! +90000$!")
        geld += 90000; wanted += 3
    elif w == "5":
        print("😴 Du wachst kurz auf... und träumst weiter... Sicher!")
        wanted = 0
        print("Wanted: 0 - Wieder frei!")
    elif w == "6":
        print(f"=== GARAGE DREAM === Geld: {geld}$ | Wanted: {'⭐'*wanted}")
        print("Auto: OMQ TRAUM-AUTO | Flügel: OMQ ENGEL | Alles!")
    elif w == "0":
        print(f"Game Over! Du hast {geld}$ in OMQ Dream World verdient!")
        break
    else:
        print("1 bis 6 oder 0 tippen!")
    print(f"Geld: {geld}$ | Wanted: {'⭐'*wanted}")
    if wanted >= 6:
        print("\n💥 BUSTED im Traum! Game Over!")
        print(f"Endstand: {geld}$")
        break
