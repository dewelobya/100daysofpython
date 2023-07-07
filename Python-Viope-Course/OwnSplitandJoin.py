#Tässä harjoituksessa tehdään kaksi funktiota

#my_split: joka jakaa ensimmäisenä parametrina annetun lauseen toisena parametrina annetun erotinmerkin erottelemiin listan alkioihin, funktio palauttaa tuloksena listan.
#my_join: joka liittää ensimmäisenä parametrina annetun listan alkiot merkkijonoksi, jossa alkioiden väliin on lisätty toisena parametrina annettava merkki, fuktio palauttaa merkkijonon.
#Harjoituksessa ei saa käyttää Pythonin valmiita split- ja join-funktioita.


#Example output:
#Kirjoita lause:Tämä on lyhyt lause
#Tämä,on,lyhyt,lause
#Tämä 
#on 
#lyhyt 
#lause
# The output of the program must be exactly the same as the example output (the most strict comparison level)

def my_split(lause, erotinmerkki):
    sana = ""
    lista = []
    for merkki in lause:
        if merkki != erotinmerkki:
            sana += merkki
        else:
            lista.append(sana)
            sana = ""
    lista.append(sana)
    return lista


def my_join(lista, erotinmerkki):
    merkkijono = ""
    for i, sana in enumerate(lista):
        merkkijono += sana
        if i < len(lista) - 1:
            merkkijono += erotinmerkki
    return merkkijono


lause = input("Kirjoita lause: ")
erotinmerkki = ","
split_lista = my_split(lause, erotinmerkki)

print(my_join(split_lista, "\n"))
print(*split_lista, sep="\n")
