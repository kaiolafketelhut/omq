import os
print("="*42)
print("  👑 OMQ GOLD LAUNCHER 👑")
print("  ALLE Spiele in einem!")
print("="*42)
print("OMQ Klassiker:")
print(" 1=OMQ Quiz  2=OMQ Welt  3=OMQ Rennen  4=OMQ Casino")
print(" 5=OMQ Schatz 6=OMQ Tycoon 7=OMQ Weltraum 8=OMQ Zeitreise")
print("GTA Saga:")
print(" 11=Liberty 12=Vice 13=San Andreas 14=Liberty 2 15=Vice 2")
print(" 16=San Andreas 2 17=City Finale 18=World 19=Galaxy 20=Multiverse")
print(" 21=Time Travel 22=Dream World 23=Underworld 24=Infinity")
print(" 25=Legend 26=Eternity 27=Universe 2")
print(" 0=Beenden")
spiele = {
 "1":"omq_quiz.py","2":"omq_welt.py","3":"omq_rennen.py","4":"omq_casino.py",
 "5":"omq_schatz.py","6":"omq_tycoon.py","7":"omq_weltraum.py","8":"omq_zeitreise.py",
 "11":"omq_gta.py","12":"omq_gta2.py","13":"omq_gta3.py","14":"omq_gta4.py","15":"omq_gta5.py",
 "16":"omq_gta6.py","17":"omq_gta7.py","18":"omq_gta8.py","19":"omq_gta9.py","20":"omq_gta10.py",
 "21":"omq_gta11.py","22":"omq_gta12.py","23":"omq_gta13.py","24":"omq_gta14.py",
 "25":"omq_gta15.py","26":"omq_gta16.py","27":"omq_gta17.py",
}
while True:
    w = input("\nLAUNCHER > ")
    if w == "0":
        print("OMQ Launcher beendet! Bis bald, Legende! 👑")
        break
    if w in spiele:
        print(f"Starte {spiele[w]}...")
        os.system(f"python3 {spiele[w]}")
    else:
        print("Nummer nicht gefunden! 0-27 tippen!")
