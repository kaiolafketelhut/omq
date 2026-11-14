import random
print("=== OMQ EAL320 - TURNIER ===")
print("Best-of-5! Wer zuerst 3 Siege hat, gewinnt!")
print("")
def pc(zahl):
    lo,hi,n=1,100,0
    while lo<=hi:
        t=(lo+hi)//2; n+=1
        if t<zahl: lo=t+1
        elif t>zahl: hi=t-1
        else: return n
du_wins=pc_wins=runde=0
while du_wins<3 and pc_wins<3:
    runde+=1
    print(f"--- RUNDE {runde} | Stand: DU {du_wins} : {pc_wins} PC ---")
    zahl=random.randint(1,100); n=0
    while True:
        try: t=int(input("Dein Tipp: "))
        except: continue
        n+=1
        if t<zahl: print("⬆️ ZU KLEIN!")
        elif t>zahl: print("⬇️ ZU GROSS!")
        else: break
    p=pc(zahl)
    print(f"DU: {n} - PC: {p} - Zahl: {zahl}")
    if n<p:
        du_wins+=1; print("🏆 Runde für DICH!")
    elif n>p:
        pc_wins+=1; print("🤖 Runde für PC!")
    else: print("🤝 Unentschieden!")
    print("")
print("=== TURNIER ENDE ===")
print(f"Endstand: DU {du_wins} : {pc_wins} PC")
if du_wins==3: print("🎉🎉🎉 TURNIER-SIEGER: DU!!! 🏆 OMQ CHAMPION!")
else: print("🤖 TURNIER-SIEGER: PC... Revanche?")
