**Tehtävä 1: Try-rakenne**

Ensimmäinen tehtävä on useampaan kertaan jo vastaantullut merkkijonon kääntäminen kokonaisluvuksi. Tee virheenkorjausrakenne, jossa käyttäjältä pyydetään luku "Anna luku: ", ja mikäli tyyppimuunnos onnistuu, tulostetaan "Syöte oli kelvollinen." ja virheen tapahtuessa "Virheellinen syöte!". Ohjelma tulostaa toimiessaan seuraavaa:
```python
Anna luku: Apina
Virheellinen syöte!
```

tai vaihtoehtoisesti


```python
Anna luku: 234
Syöte oli kelvollinen.
```

Virheiden kiinniottoon sopivin luokka on tässä tehtävässä yleisluokka "Exception". Lisäksi tulostuksessa kannattaa tutustua siihen, kuinka try-rakenteen else-osio toimii.

**My solution:**
```python
def käännä_kokonaisluvuksi(merkkijono):
    try:
        luku = int(merkkijono)
        print("Syöte oli kelvollinen.")
    except ValueError:
        print("Virheellinen syöte!")

luku_str = input("Anna luku: ")
käännä_kokonaisluvuksi(luku_str)
```

**Tehtävä 2: Usean virheen kiinniotto**
Toisessa tehtävässä luodaan ohjelma, joka osaa selviytyä useammasta virhetyypistä. Tee ohjelma, joka pyytää käyttäjältä tiedoston nimen, sekä avaa ja lukee tiedoston sisällön. Tämän jälkeen ohjelma yrittää muuttaa tiedostosta luetun arvon kokonaisluvuksi, sekä lisätä siihen arvon 313. Jos kaikki menee oikein, ohjelma tulostaa vastauksen "Saatiin tulos [tulos]". Jos annettu tiedoston nimi on virheellinen, tulostetaan "Virheellinen tiedostonnimi". Jos taas tiedoston sisältö on virheellinen eikä käänny kokonaisluvuksi, tulostetaan "Tiedoston sisältö virheellinen!". Toimiessaan ohjelma tulostaakin seuraavaa:

```

>>>
Anna tiedoston nimi: hu
Virheellinen tiedostonnimi
>>> 
Anna tiedoston nimi: muistio.txt
Tiedoston sisältö virheellinen!
>>> 
Anna tiedoston nimi: luku.txt
Saatiin tulos 626
>>> 
```

Ohjelma on järkevintä toteuttaa yhdellä virheenkäsittelyrakenteella, jolla on omat käsittelijät IOError ja ValueError-virheille.


**My solution:**
```python

def lue_tiedosto(tiedoston_nimi):
    try:
        with open(tiedoston_nimi, 'r') as tiedosto:
            sisältö = tiedosto.read()
            arvo = int(sisältö)
            tulos = arvo + 313
            print("Saatiin tulos", tulos)
    except IOError:
        print("Virheellinen tiedostonnimi")
    except ValueError:
        print("Tiedoston sisältö virheellinen!")

tiedoston_nimi = input("Anna tiedoston nimi: ")
lue_tiedosto(tiedoston_nimi)

```

**Tehtävä 3: Nelilaskin: syötteiden tarkastaminen**
Luvun kolmas tehtävä jatkaa edellisessäkin luvussa työstettyä nelilaskinta. Tähän asti ohjelma on ollut sen varassa, että käyttäjä antaa aina laskimelle oikeita lukuarvoja, mutta virheenkäsittelyn avulla tämäkin ongelma voidaan poistaa.


Tee siis ohjelmakoodiin muutokset, joilla käyttäjän antamat syötteet tarkastetaan ennen kuin ne hyväksytään laskimeen numeroiksi. Helpointa tämä on tehdä luomalla erillinen alifunktio, joka pyytää käyttäjältä niin kauan uutta lukua kunnes tyyppimuunnos kokonaisluvuksi onnistuu. Tämän jälkeen alifunktio palauttaa lukuarvon laskimelle. Jos käyttäjän syöttämä luku on virheellinen, tulostetaan "Virheellinen syöte!" ja lukua pyydetään uudestaan. Toimiessaan oikein ohjelma tulostaa vaikkapa seuraavaa:
```

Anna luku: fge
Virheellinen syöte!
Anna luku: 10
Anna luku: 15
(1) +
(2) -
(3) *
(4) /
(5)sin(luku1/luku2)
(6)cos(luku1/luku2)
(7)Vaihda luvut
(8)Lopeta
Valitut luvut: 10 15
Tee valinta (1-8): 7
Anna luku: apina
Virheellinen syöte!
Anna luku: 20
Anna luku: 9
(1) +
(2) -
(3) *
(4) /
(5)sin(luku1/luku2)
(6)cos(luku1/luku2)
(7)Vaihda luvut
(8)Lopeta
Valitut luvut: 20 9
Tee valinta (1-8): 8
```

**My solution:**
import math

def pyyda_luku():
    while True:
        syote = input("Anna luku: ")
        try:
            luku = int(syote)
            return luku
        except ValueError:
            print("Virheellinen syöte!")

luku_1 = pyyda_luku()
luku_2 = pyyda_luku()

while True:
    print("(1) +\n(2) -\n(3) *\n(4) /\n(5) sin(luku1/luku2)\n(6) cos(luku1/luku2)\n(7) Vaihda luvut\n(8) Lopeta")

    print("Valitut luvut: {0} {1}".format(luku_1, luku_2))
    valinta = int(input("Tee valinta (1-8): "))

    if valinta == 1:
        print("Tulos on:", luku_1 + luku_2)
    elif valinta == 2:
        print("Tulos on:", luku_1 - luku_2)
    elif valinta == 3:
        print("Tulos on:", luku_1 * luku_2)
    elif valinta == 4:
        print("Tulos on:", luku_1 / luku_2)
    elif valinta == 5:
        print("Tulos on:", math.sin(luku_1 / luku_2))
    elif valinta == 6:
        print("Tulos on:", math.cos(luku_1 / luku_2))
    elif valinta == 7:
        luku_1 = pyyda_luku()
        luku_2 = pyyda_luku()
    elif valinta == 8:
        break
    else:
        print("Valintaa ei tunnistettu.")


**Tehtävä 4: Muistikirja: muistikirjan vaihtaminen**

Myös muistikirja on tähän asti toiminut sen varassa, että käyttäjä ei yritä lukea muistiota ennen kuin tiedostoon on kirjoitettu jotain. Tällä kertaa muistikirja-ohjelmaan lisätäänkin kaksi uutta toimintoa; ensinnäkin ohjelman tulee tarkastaa käynnistyessään onko tiedosto "muistio.txt" olemassa, ja tarvittaessa luoda tämänniminen tiedosto. Mikäli näin tehdään ilmoittaa ohjelma "Oletusmuistiota ei löydy, luodaan tiedosto".


Toisekseen, lisää ohjelmaan mahdollisuus vaihtaa muistiotiedostoa kesken ohjelman suorituksen lisäämällä ohjelmaan valinta "(4) Vaihda muistiota", jonka jälkeen ohjelma pyytää uutta muistiotiedostoa "Anna tiedoston nimi: " ja tarvittaessa luo tämännimisen tiedoston jälleen antaen ilmoituksen "Tiedostoa ei löydy, luodaan tiedosto.". Lisäksi ohjelma kertoo päävalikossa mitä tiedostoa tällähetkellä käytetään; "Käytetään muistiota: [tiedostonnimi]". Toimiessaan oikein ohjelma tulostaa vaikkapa seuraavaa:

```
Oletusmuistioa ei löydy, luodaan tiedosto.
Käytetään muistiota:  muistio.txt
(1) Lue muistikirjaa
(2) Lisää merkintä
(3) Tyhjennä muistikirja
(4) Vaihda muistiota
(5) Lopeta

Mitä haluat tehdä?: 2
Kirjoita uusi merkintä: -Osta maitoa
Käytetään muistiota:  muistio.txt
(1) Lue muistikirjaa
(2) Lisää merkintä
(3) Tyhjennä muistikirja
(4) Vaihda muistiota
(5) Lopeta

Mitä haluat tehdä?: 4
Anna tiedoston nimi: uusimuistio.txt
Tiedostoa ei löydy, luodaan tiedosto.
Käytetään muistiota:  uusimuistio.txt
(1) Lue muistikirjaa
(2) Lisää merkintä
(3) Tyhjennä muistikirja
(4) Vaihda muistiota
(5) Lopeta

Mitä haluat tehdä?: 2
Kirjoita uusi merkintä: -Osta ananas
Käytetään muistiota:  uusimuistio.txt
(1) Lue muistikirjaa
(2) Lisää merkintä
(3) Tyhjennä muistikirja
(4) Vaihda muistiota
(5) Lopeta

Mitä haluat tehdä?: 1
-Osta ananas:::13:53:00 01/04/09

Käytetään muistiota:  uusimuistio.txt
(1) Lue muistikirjaa
(2) Lisää merkintä
(3) Tyhjennä muistikirja
(4) Vaihda muistiota
(5) Lopeta

Mitä haluat tehdä?: 5
Lopetetaan.

```
Ohjelman toteuttamisessa kannattaa lähestyä ongelmaa siten, että käytettävän tiedoston nimi on tallennettuna muuttujaan, jonka arvoa muutetaan jos tiedostoa vaihdetaan. Lisäksi tiedoston olemassaolon tarkastun on helpointa toteuttaa yrittämällä avata tiedosto ja sulkemalla se samantien; jos ohjelma palauttaa IOErrorin voidaan samanniminen tiedosto luoda kirjoitustilalla.


**My Solution:**

```python
import time
import os

tiedoston_nimi = "muistio.txt"

# Check if the default muistio file exists, create it if not
if not os.path.exists(tiedoston_nimi):
    print("Oletusmuistioa ei löydy, luodaan tiedosto.")
    tiedosto = open(tiedoston_nimi, "w")
    tiedosto.close()

while True:
    print("Käytetään muistiota:", tiedoston_nimi)
    print("(1) Lue muistikirjaa")
    print("(2) Lisää merkintä")
    print("(3) Tyhjennä muistikirja")
    print("(4) Vaihda muistiota")
    print("(5) Lopeta\n")

    valinta = int(input("Mitä haluat tehdä?: "))

    if valinta == 1:
        tiedosto = open(tiedoston_nimi, "r")
        sisalto = tiedosto.read()
        print(sisalto)
        tiedosto.close()
    elif valinta == 2:
        tiedosto = open(tiedoston_nimi, "a")
        lisays = input("Kirjoita uusi merkintä: ")
        aika = time.strftime("%X %x")
        tiedosto.write(lisays + ":::" + aika + "\n")
        tiedosto.close()
    elif valinta == 3:
        tiedosto = open(tiedoston_nimi, "w")
        print("Muistio tyhjennetty.")
        tiedosto.close()
    elif valinta == 4:
        uusi_tiedosto = input("Anna tiedoston nimi: ")
        if not os.path.exists(uusi_tiedosto):
            print("Tiedostoa ei löydy, luodaan tiedosto.")
            tiedosto = open(uusi_tiedosto, "w")
            tiedosto.close()
        tiedoston_nimi = uusi_tiedosto
    elif valinta == 5:
        print("Lopetetaan.")
        break
    else:
        print("Tuntematon valinta")

```

