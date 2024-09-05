while True:
    tuumat = float(input("Anna tuumamäärä: "))
    if tuumat < 0:
        print("Ohjelma lopetetaan.")
        break

    senttimetrit = tuumat * 2.54
    print(f"{tuumat} tuumaa on {senttimetrit} cm")
