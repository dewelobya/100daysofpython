# Viope Python course non-stop 3 OP 

# Chapter 6 


Kolmannen luvun tehtävät aloitetaan yksinkertaisen if-rakenteen luomisella. 
Ohjelma pyytää käyttäjältä luvun ja tallentaa sen muuttujaan. 
Mikäli luku on parillinen, ohjelma tulostaa vastauksen "Antamasi luku oli parillinen". 
If-rakenteen ehtolauseeseen tarvittavat parametrit löydät luvun taulukosta, 
ja helpoin tapa toteuttaa ohjelma onkin käyttää jakojäännös-operaattoria, testaten onko jakojäännös 0. 
Ohjelman ei tarvitse myöskään reagoida virheellisiin syötteisiin eikä desimaalilukuihin. 
Ohjelma tulostaa seuraavan vastauksen:


# Exerices 6.2 
Tehtävä 1: If-rakenteen tekeminen

# First attempt (not correct)

´´´

oikea_nimi = "Erkki"
oikea_salasana = "Esimerkki"

nimi = input("Anna nimi: ")
salasana = input("Anna salasana: ")

if nimi == oikea_nimi and salasana == oikea_salasana :
    print("Salasana ja nimi oli oikein!")
    if nimi == oikea_nimi:
        print("Nimi oli oikein.")
    else:
        print("Nimi oli väärin.")
else:
    print("Salasana ja nimi oli väärin.")
    ´´´
    
# The correct answer: 
´´´
nimi = str(input("Anna nimi: "))

if nimi == "Erkki":
    salasana = input("Anna salasana: ")
    if salasana == "Esimerkki":
        print("Salasana ja nimi oli oikein!")
    else:
        print("Salasana oli väärin.")
else:
    print("Nimi oli väärin.")
    ´´´
    
    
    
