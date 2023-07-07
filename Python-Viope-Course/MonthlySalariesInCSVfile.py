#Tässä harjoituksessa SalaryEmployee -luokan oliot kirjoitetaan tiedostoon salary_employee.csv ja luetaan tiedostosta pilkuilla eroteltuina eli csv-muodossa. Ohjelmassa käytetään aikaisemmin rakennettuja omia my_join ja my_split funktiota. 

#Ohjelman valikko kuten alla:

#(1) Lisää työntekijöitä listaan 
#(2) Kirjoita työntekijät tiedostoon 
#(3) Lue työntekijät tiedostosta 
#(4) Tulosta työntekijät 
#(0) Lopeta
#Valikon valinnalla 1 luetaan työntekijöiden nimet ja palkat olioiden muuttujiin.
#Valikon valinnalla 2 kirjoitetaan kaikki oliot csv-tiedostoon.
#Valikon valinnalla 3 luetaan csv-tiedostosta oliot.
#Valikon valinnalla 4 tulostetaan oliot ja niiden arvot muodossa: id: 1 Nimi: Maija Mainio Palkka: 5555.
#Valikon valinnalla 0 lopetetaan ohjelman suoritus.
 
#Sinun tehtävänä on kirjoittaa valikon valinnat 2 ja 3.
 
#Kirjoita työntekijät tiedostoon
#varmista, että tiedosto salary_employee.csv on tyhjä 
#käy läpi työntekijälista ja jokaiselle oliolle luo lista, jonne olet lisännyt olion attribuutit merkkijonoina, tämä lista välitetään my_join-funktiolle
#my_join-funktion avulla listasta muodostetaan yhtenäinen merkkijono (pilkulla eroteltuna), lisää rivinvaihto ja kirjoita merkkijono tiedostoon
#kun kaikki työntekijät on käsitelty, muista sulkea tiedostokahva
#lisää loppuun koodi:  print(len(salary_employees) ," työntekijä(ä) lisätty tiedostoon salary_employee.csv")
#Lue työntekijät tiedostosta
#avaa tiedosto luettavaksi
#niin kauan kuin tiedostossa rivejä lue rivi kerrallaan
#muodosta my_split -funktiolla tiedostosta luetusta merkkijonosta työntekijän attribuutit sisältävä merkkijonolista
#luo SalaryEmployee -olio ja lisää se salary_employees -listaan
#sulje tiedosto kun kaikki rivit on luettu
#lisää loppuun vielä koodi: print(len(salary_employees) ," työntekijä(ä) luettu tiedostosta salary_employee.csv")

#Example output:
#(1) Lisää työntekijöitä listaan
#(2) Kirjoita työntekijät tiedostoon
#(3) Lue työntekijät tiedostosta
#(4) Tulosta työntekijät
#(0) Lopeta

#Valitse toiminto: 1
#Anna työntekijän nimi (0 lopetus):Maija Mainio
#Anna kuukausipalkka:5555
#Anna työntekijän nimi (0 lopetus):Jussi Juonio
#Anna kuukausipalkka:4567
#Anna työntekijän nimi (0 lopetus):Matti Meikäläinen
#Anna kuukausipalkka:3636
#Anna työntekijän nimi (0 lopetus):0
#(1) Lisää työntekijöitä listaan
#(2) Kirjoita työntekijät tiedostoon
#(3) Lue työntekijät tiedostosta
#(4) Tulosta työntekijät
#(0) Lopeta

#Valitse toiminto: 2
#3  työntekijä(ä) lisätty tiedostoon salary_employee.csv
#(1) Lisää työntekijöitä listaan
#(2) Kirjoita työntekijät tiedostoon
#(3) Lue työntekijät tiedostosta
#(4) Tulosta työntekijät
#(0) Lopeta

#Valitse toiminto: 4
#Id: 1 Nimi: Maija Mainio Kuukausipalkka: 5555
#Id: 2 Nimi: Jussi Juonio Kuukausipalkka: 4567
#Id: 3 Nimi: Matti Meikäläinen Kuukausipalkka: 3636
#(1) Lisää työntekijöitä listaan
#(2) Kirjoita työntekijät tiedostoon
#(3) Lue työntekijät tiedostosta
#(4) Tulosta työntekijät
#(0) Lopeta

#Valitse toiminto: 3
#3  työntekijä(ä) luettu tiedostosta salary_employee.csv
#(1) Lisää työntekijöitä listaan
#(2) Kirjoita työntekijät tiedostoon
#(3) Lue työntekijät tiedostosta
#(4) Tulosta työntekijät
#(0) Lopeta

#Valitse toiminto: 4
#Id: 1 Nimi: Maija Mainio Kuukausipalkka: 5555
#Id: 2 Nimi: Jussi Juonio Kuukausipalkka: 4567
#Id: 3 Nimi: Matti Meikäläinen Kuukausipalkka: 3636
#(1) Lisää työntekijöitä listaan
#(2) Kirjoita työntekijät tiedostoon
#(3) Lue työntekijät tiedostosta
#(4) Tulosta työntekijät
#(0) Lopeta

#Valitse toiminto: 0
#Palvelu suljetaan, kiitos.

