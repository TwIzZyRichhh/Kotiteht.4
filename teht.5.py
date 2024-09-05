def kirjautimunen():
    oikea_kayttajatunnus = "python"
    oikea_salasana = "rules"

    yritykset = 0
    maksimiyritykset = 5

    while yritykset < maksimiyritykset:
        kayttajatunnus = input("Anna käyttäjätunnus: ")
        salasana = input("Anna salasana: ")

        if kayttajatunnus == oikea_kayttajatunnus and salasana == oikea_salasana:
            print("Tervetuloa!")
            return
        else:
            print("Väärä käyttäjätunnus tai salasana.")
            yritykset += 1

    print("Pääsy evätty.")
kirjautimunen()


