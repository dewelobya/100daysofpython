

# Tiedostojen käyttömoodit #

**Tila	Merkki**

- `r`	Lukutila; mikäli tiedostoa ei löydy palautetaan IOError. Käsittelee tietoa merkkeinä.
- `w`	Kirjoitustila; mikäli tiedostoa ei löydy sellainen luodaan. Mikäli samanniminen tiedosto on jo olemassa se tuhotaan. Käsittelee tietoa merkkeinä.
- `a`	Kirjoitustila; mikäli tiedostoa ei löydy sellainen luodaan. Mikäli samanniminen tiedosto on jo olemassa kirjoitetaan sen perään. Käsittelee tietoa merkkeinä.
- `rb`	Lukutila; mikäli tiedostoa ei löydy palautetaan IOError. Käsittelee tietoa bittiarvoina.
- `wb`	Kirjoitustila; mikäli tiedostoa ei löydy sellainen luodaan. Mikäli samanniminen tiedosto on jo olemassa kirjoitetaan sen perään. Käsittelee tietoa bittiarvoina.

**Example:**

Lähedekoodi:
```python

01  # -*- coding: cp1252 -*-
02
03  luku = 1024
04
05  tiedosto = open("lukutiedosto.txt","w")
06  tiedosto.write( str(luku) )
07  tiedosto.close()
08
09  luettu_luku = 0
10  tiedosto = open("lukutiedosto.txt","r")
11  luettu_luku = int(tiedosto.readline())
12  tiedosto.close()
13  
14  print("Luettiin",luettu_luku,"joka muunnettiin numeroksi:")
15  luettu_luku = luettu_luku *2
16  print(luettu_luku)


```

Tuloste:
```
>>> 
Luettiin 1024 joka muunnettiin numeroksi:
2048
>>>

```
Itseasiassa useimmat Python-koodit aloittava kommenttirivi

```python
 # -*- coding: cp1252 -*-
```

tarkoittaa, että ohjelmassa käytetään merkkitaulukkoa 1252. 

Jos Python-koodin alussa on teksti
```python
# -*- coding: UTF8 -*-

```
tarkoittaa se sitä, että koodi on kirjoitettu UTF8-merkkitaulukkoa tukevalla käyttöjärjestelmällä.

# Ch8, Tehtävä 1: Tiedostoon kirjoittaminen #

**Challenge Instructions:**

Tee ohjelma, joka ensin pyytää käyttäjältä tiedoston nimen, ja tämän jälkeen tekstin, jonka käyttäjä haluaa tiedostoon kirjoitettavan. Tämän jälkeen ohjelma tekee tiedoston, kirjoittaa tuloksen ja antaa ilmoituksen "Luotiin tiedosto [tiedostonnimi] ja siihen tallennettiin teksti: [sisältö]." Toimiessaan oikein ohjelma tulostaa vaikkapa seuraavan tekstin:

Minkäniminen tiedosto luodaan?: loki.txt
Mitä kirjoitetaan tiedostoon?: Attencion, attencion. 10, 10, 22, 33, Adios.
Luotiin tiedosto loki.txt ja siihen tallennettiin teksti: Attencion, attencion. 10, 10, 22, 33, Adios.

**My Solution:**

```python
tiedoston_nimi = input("Minkäniminen tiedosto luodaan?: ")
sisalto = input("Mitä kirjoitetaan tiedostoon?: ")

with open(tiedoston_nimi, 'w') as tiedosto:
    tiedosto.write(sisalto)

print(f"Luotiin tiedosto {tiedoston_nimi} ja siihen tallennettiin teksti: {sisalto}.")

```

---> output too long 

**My solution:**

```python 
tiedoston_nimi = str(input("Minkäniminen tiedosto luodaan?: "))
sisalto = str(input("Mitä kirjoitetaan tiedostoon?: "))

try:
    tiedosto = open(tiedoston_nimi, "w")
    tiedosto.write(sisalto)
    tiedosto.close()
    print("Luotiin tiedosto {0} ja siihen tallennettiin teksti: {1}".format(tiedoston_nimi, sisalto))
except IOError:
    print("Error")
```

--- Correct 


# Ch8, Tehtävä 2: Luetun datan seulonta, muuttujannimet #

**Challenge Instructions:**
Lähdekooditiedoston kanssa samaan hakemistoon on tallennettuna tiedosto "merkkijonoja.txt". Tämä tiedosto sisältää satunnaisesti luotuja merkkijonoja, joissa esiintyy kahdenlaisia merkkijonoja: sellaisia, joissa on kirjaimia ja mahdollisesti numeroita, sekä sellaisia, joissa on kirjaimia, numeroita ja erikoismerkkejä (€,#,{, §, jne). Tehtävänäsi on tehdä ohjelma, joka lukee tiedostosta rivin, testaa onko merkkijono sellainen, joka sisältää vain kirjaimia ja numeroita, ja sen mukaan tulostaa joko "[merkkijono] kelpaa salasanaksi" jos on, tai "[merkkijono] sisältää virheellisiä merkkejä." mikäli siinä on ei-alfanumeerisia merkkejä. Toimiessaan ohjelma tulostaa seuraavaa:

```
5345m345ö34l kelpaa salasanaksi.
no2no123non4 kelpaa salasanaksi.
noq234n5ioqw#% sisältää virheellisiä merkkejä.
%#""SGMSGSER sisältää virheellisiä merkkejä.
doghdp5234 kelpaa salasanaksi.
sg,dermoepm sisältää virheellisiä merkkejä.
43453-frgsd sisältää virheellisiä merkkejä.
hsth())) sisältää virheellisiä merkkejä.
bmepm35wae kelpaa salasanaksi.
vmopaem2234+0+ sisältää virheellisiä merkkejä.
gsdm12313 kelpaa salasanaksi.
```

Tehtävässä kannattaa rivit lukea yksi kerrallaan ja testata .isalnum()-merkkijonometodilla. Lisäksi muista poistaa lopussa oleva rivinvaihtomerkki, se ei ole kirjain eikä numero!


**My Solution:**

```python
with open("merkkijonoja.txt", "r") as tiedosto:
    for rivi in tiedosto:
        merkkijono = rivi.rstrip("\n")  # Poista rivinvaihto merkkijonosta
        if merkkijono.isalnum():
            print(f"{merkkijono} kelpaa salasanaksi.")
        else:
            print(f"{merkkijono} sisältää virheellisiä merkkejä.")

```

# Ch8, Tehtävä 3: Muistikirja: Kirjoita ja lue muistikirjaa #

**Challenge instructions:**

Tässä tehtävässä teemme muistikirjan, joka tallennetaan erilliseen tiedostoon nimeltä "muistio.txt".


Tee ohjelma, joka antaa käyttäjälle mahdollisuuden
(1) lukea muistikirjan sisältö,
(2) Lisätä muistikirjaan merkintä tai
(3) Tyhjentää koko muistikirja
Lisäksi lisää valinta (4), joka lopettaa ohjelman. Mikäli käyttäjä valitsee 1, tulostetaan tiedoston sisältö ruudulle, mikäli 2 niin ohjelma kysee "Kirjoita uusi merkintä: " ja tallentaa merkinnän muistioon, lisäten merkinnän loppuun rivinvaihtomerkin "\n" jotta merkinnät pysyvät eri riveillä. Jos käyttäjä valitsee 3 tyhjennetään tiedosto ja tulostetaan näytölle teksti "Muistio tyhjennetty." ja valinnalla 4 ohjelma ilmoittaa "Lopetetaan." ja sammuu. Muilla valinnoilla ohjelma ilmoittaa "Tuntematon valinta.". Toimiessaan ohjelma tulostaa seuraavaa:


```
(1) Lue muistikirjaa
(2) Lisää merkintä
(3) Tyhjennä muistikirja
(4) Lopeta

Mitä haluat tehdä?: 2
Kirjoita uusi merkintä: -Osta maitoa
(1) Lue muistikirjaa
(2) Lisää merkintä
(3) Tyhjennä muistikirja
(4) Lopeta

Mitä haluat tehdä?: 1
-Osta maitoa

(1) Lue muistikirjaa
(2) Lisää merkintä
(3) Tyhjennä muistikirja
(4) Lopeta

Mitä haluat tehdä?: 4
Lopetetaan.
```

Huomaa, että nopein tapa tiedoston tyhjentämiseen on avata se tilaan "w" ja sulkea samantien.



**My Solution:**

```python
def lue_muistikirjaa():
    with open("muistio.txt", "r") as tiedosto:
        sisalto = tiedosto.read()
        print(sisalto)


def lisaa_merkinta():
    merkinta = input("Kirjoita uusi merkintä: ")
    with open("muistio.txt", "a") as tiedosto:
        tiedosto.write(merkinta + "\n")


def tyhjenna_muistikirja():
    with open("muistio.txt", "w") as tiedosto:
        tiedosto.write("")
    print("Muistio tyhjennetty.")


valinnat = ["1", "2", "3", "4"]

while True:
    print("(1) Lue muistikirjaa")
    print("(2) Lisää merkintä")
    print("(3) Tyhjennä muistikirja")
    print("(4) Lopeta")

    valinta = input("Mitä haluat tehdä?: ")

    if valinta == "1":
        lue_muistikirjaa()
    elif valinta == "2":
        lisaa_merkinta()
    elif valinta == "3":
        tyhjenna_muistikirja()
    elif valinta == "4":
        print("Lopetetaan.")
        break
    else:
        print("Tuntematon valinta.")

```
