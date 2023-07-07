#Supermarket

hinnat = [10, 14, 22, 33, 44, 13, 22, 55, 66, 77]
ostokset = []
kokonaissumma = 0

print("Supermarket")
print("===========")

while True:
    tuote_numero = int(input("Valitse tuote (1-10) 0 lopetus: "))

    if tuote_numero == 0:
        break

    if tuote_numero >= 1 and tuote_numero <= 10:
        tuote_hinta = hinnat[tuote_numero - 1]
        ostokset.append((tuote_numero, tuote_hinta))
        kokonaissumma += tuote_hinta
        print("Tuote:", tuote_numero, "Hinta:", tuote_hinta)
    else:
        print("Virheellinen tuotenumero!")

print("Yhteensä:", kokonaissumma)
maksu = int(input("Maksu: "))
vaihto = maksu - kokonaissumma
print("Vaihto:", vaihto)
