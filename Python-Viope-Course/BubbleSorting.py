#Tee funktio bubble_sort, joka käyttää kuplalajittelualgoritmia lajitellakseen käyttäjän antamat numerot pienimmästä suurimpaan.

#Kuplalajittelu on yksinkertainen lajittelualgoritmi, joka toistuvasti vaihtaa peräkkäiset alkiot keskenään mikäli ne ovat väärässä järjestyksessä. Kts. https://en.wikipedia.org/wiki/Bubble_sort


#Example output:
#Anna lajiteltavien numeroiden lukumäärä : 5
#Anna taulukon 0 numero : 4
#Anna taulukon 1 numero : 3
#Anna taulukon 2 numero : -1
#Anna taulukon 3 numero : 9
#Anna taulukon 4 numero : 6
#Lajiteltu lista nousevassa järjestyksessä: 

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista


lukumaara = int(input("Anna lajiteltavien numeroiden lukumäärä: "))
taulukko = []

for i in range(lukumaara):
    numero = int(input(f"Anna taulukon {i} numero: "))
    taulukko.append(numero)

taulukko = bubble_sort(taulukko)

print("Lajiteltu lista nousevassa järjestyksessä:", taulukko)
