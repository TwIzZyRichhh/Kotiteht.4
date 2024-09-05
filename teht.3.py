luvut = []

while True:
    syote = input("Anna luku (tyhjä lopettaa): ")
    if syote == "":
        break
    try:
        luku = float(syote)
        luvut.append(luku)
    except ValueError:
        print("Syötä kelvollinen luku.")
        continue
if luvut:
    pienin = min(luvut)
    suurin = max(luvut)
    print(f"Pienin annettu luku on: {pienin}")
    print(f"Suurin annettu luku on: {suurin}")
else:
    print("Et syöttänyt yhtään lukua.")
