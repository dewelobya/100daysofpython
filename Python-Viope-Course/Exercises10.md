## Moduulit ##

Lisäkirjasto käyttöönotetaan avainsanalla import. Lisäkirjastojen käyttöönotto suoritetaan tavallisesti heti ohjelmakoodin tai funktion alkussa, jotta lähdekoodin ymmärrettävyys ja luettavuus säilyy. Esimerkiksi komennolla:

```python
import random
```
 
ilmoitetaan tulkille, että ohjelma käyttää kirjastoa nimeltä random, joka sisältää funktioita satunnaislukujen arpomiseen. Seuraavaksi voidaankin kokeilla lisäkirjaston funktion käyttämistä tekemällä lyhyt ohjelma, joka arpoo lukuja nollan ja sadan väliltä. Esimerkki 7-1: Lisäkirjaston käyttöönotto, satunnaisluku

**Lähdekoodi:**
```python

02  
03  import random
04 
05  #otetaan satunnainen kokonnaisluku väliltä 0-100
06  #tämä tehdään random-kirjaston funktiolla randint
07  luku = random.randint(0,100)
08
09  print("Ohjelma arpoi luvun",luku)
```
**Tuloste:**
```
>>> 
Ohjelma arpoi luvun 89
>>> 
Ohjelma arpoi luvun 95
>>> 
Ohjelma arpoi luvun 36
>>> 
Ohjelma arpoi luvun 85
>>> 
```

**Ch10.1.Satunnaislukukirjasto random, kolikonheitto**
Luvun ensimmäinen tehtävä perustuu random-moduulikirjaston toimintaan. Tee ohjelma, joka arpoo viisi kertaa joko luvun 0 tai 1 käyttäen random.randint-kirjastofunktiota. Mikäli ohjelma arpoo luvun 0, tulostetaan "Klaava!", mikäli 1 niin "Kruuna!". Ohjelma alkaa tulosteella "Heitetään kolikkoa viidesti:" ja toimii seuraavalla tavalla:
```

Heitetään kolikkoa viidesti:
Klaava!
Kruuna!
Kruuna!
Kruuna!
Kruuna!

```
**My solution:**

```python 
import random

def main():
    print("Heitetään kolikkoa viidesti:")
    for _ in range(5):
        luku = random.randint(0, 1)
        if luku == 0:
            print("Klaava!")
        else:
            print("Kruuna!")

if __name__ == "__main__":
    main()

 ```

**Ch10.2. Oman moduulin tekeminen**

Luvun kolmas tehtävä käsittelee oman moduulin tekemistä. Tämä tehtävä on siitä poikkeuksellinen, että tarkoitus ei olekaan kirjoittaa kokonaista ohjelmaa, vaan ainoastaan toteuttaa moduuli olemassaolevalle ohjelmalle.


Meillä on valmiina ohjelman pääfunktion sisältävä moduuli, jonka sisältö näyttää tältä:

```
import moduuli

moduuli.tulosta("Esimerkkirivi")
```

Tehtäväsi onkin nyt tuottaa ohjelmassa sisällytetty moduuli; luo koodi, jossa on tulosta-niminen funktio, joka tulostaa sille annetun parametrin ja parametrin pituuden muodossa "Saatiin syöte: [parametri].\n Syötteen pituus on [pituus] merkkiä.". Toimiessaan ohjelma tulostaa seuraavaa:

```

Saatiin syöte: Esimerkkirivi
Syötteen pituus on 13 merkkiä.

```


**My solution:**

def tulosta(syote):
    pituus = len(syote)
    print("Saatiin syöte: {0}".format(syote))
    print("Syötteen pituus on {0} merkkiä.".format(pituus))



**Ch10.3 Oman moduulin tekeminen, useita parametreja jne**
Luvun neljäs tehtävä jatkaa oman moduulin tekemistä. Tässä tehtävässä luomme ohjelman, joka testaa käyttäjän syöttämiä merkkijonoja sen mukaan, kuinka ne soveltuisivat salasanoiksi. Myös tässä tehtävässä on tarkoitus ainoastaan toteuttaa moduuli olemassaolevalle ohjelmalle.


Meillä on valmiina ohjelman pääfunktion sisältävä moduuli, jonka sisältö näyttää tältä:

```python
import tarkastaja
while True:
    testattava = input("Anna testattava sana: ")
    tulos = tarkastaja.testaa(testattava)
    if tulos == True:
        print("Antamasi sana kelpaa salasanaksi!")
        break
    else:
        print("Sana ei kelpaa.")

```
Tehtäväsi onkin luoda tähän päämoduuliin sopiva tarkastaja-moduuli. Tee moduuli, jossa on testaa-niminen funktio, joka vastaanottaa syötteen. Jos syöte on alle 5 merkkiä pitkä, sisältää pelkästään kirjaimia tai pelkästään numeroita, palauttaa ohjelma False. Muussa tapauksessa ohjelma palauttaa arvon True. Ohjelma lopetetaan kun käyttäjä antaa ensimmäisen sopivan syötteen. Toimiessaan ohjelma tulostaa seuraavaa:

```
Anna testattava sana: Testi
Sana ei kelpaa.
Anna testattava sana: 234234
Sana ei kelpaa.
Anna testattava sana: Testisana11234
Antamasi sana kelpaa salasanaksi!
```

Ohjelman ei tarvitse huomioida erikoismerkkien tilannetta, vaan ainoastaan tarkastaa, että merkkijono on 5 merkkiä tai enemmän, sekä sisältää numeroita ja kirjaimia. Merkkijonotestit .isalpha ja .isdigit ovat tässä tapauksessa hyödyllisiä apuvälineitä.

**My solution:**

```python
def testaa(syote):
    if len(syote) < 5 or syote.isalpha() or syote.isdigit():
        return False
    else:
        return True
```


**ch10.4.Nelilaskin: math-kirjaston toimintojen tuominen**
Tässä tehtävässä jatketaan luvun 4 neljättä tehtävää, laskinta. Tehtävässä lisätään laskimeen kaksi uutta tehtävää, sin ja cos. Nämä funktiot löytyvät math-moduulin sisältä, vastaavilla funktionimillä sin() ja cos(), joille molemmille voidaan antaa syötteeksi (luku_1 / luku_2). Toteuta käskyt vaihtoehdoiksi 5 ja 6, samalla siirtäen "vaihda luvut" ja "Lopeta" kohdiksi 7 ja 8. Ohjelma toimii seuraavalla tavalla:


**My solution:**
```python
import math

def laske(luku1, luku2, valinta):
    if valinta == 1:
        return luku1 + luku2
    elif valinta == 2:
        return luku1 - luku2
    elif valinta == 3:
        return luku1 * luku2
    elif valinta == 4:
        return luku1 / luku2
    elif valinta == 5:
        return math.sin(luku1 / luku2)
    elif valinta == 6:
        return math.cos(luku1 / luku2)
    else:
        return None

def main():
    luku1 = float(input("Anna ensimmäinen luku: "))
    luku2 = float(input("Anna toinen luku: "))

    while True:
        print("(1) +")
        print("(2) -")
        print("(3) *")
        print("(4) /")
        print("(5) sin(luku1/luku2)")
        print("(6) cos(luku1/luku2)")
        print("(7) Vaihda luvut")
        print("(8) Lopeta")
        print("Valitut luvut:", luku1, luku2)
        valinta = int(input("Tee valinta (1-8): "))

        if valinta == 7:
            luku1 = float(input("Anna ensimmäinen luku: "))
            luku2 = float(input("Anna toinen luku: "))
        elif valinta == 8:
            break
        else:
            tulos = laske(luku1, luku2, valinta)
            if tulos is None:
                print("Virheellinen valinta!")
            else:
                if valinta in [1, 2, 3, 4]:
                    print("Tulos on:", int(tulos))  # Convert the result to an integer
                else:
                    print("Tulos on:", tulos)

if __name__ == "__main__":
    main()
```
(ei toimi) 

**ch10.5. Muistikirja: päiväyksen luominen TODO-listaan**
Luvun viimeinen tehtävä liittyy muistikirjan käsittelyyn. Tällä kertaa ohjelmaa muutetaan siten, että ohjelma lisää muistikirjamerkinnän perään päiväyksen ja kellonajan, josta käy ilmi milloin merkintä on tehty.Lisäksi laita viestin ja päiväyksen väliin eroitin ":::" (kolme kaksoispistettä).


Päiväys saadaan esimerkiksi time-moduulista komennolla

```

	
>>> import time		
>>> time.strftime("%X %x")
'19:01:34 01/03/09'
>>> 
```

**My solution:**

```python
import time

def lisaa_merkinta(muistikirja):
    merkinta = input("Kirjoita uusi merkintä: ")
    paivays = time.strftime("%X %x")  # Hae nykyinen päiväys ja kellonaika
    merkinta = f"{merkinta}:::{paivays}"  # Yhdistä merkintä ja päiväys erotinmerkillä ":::"
    muistikirja.append(merkinta)
    print("Merkintä lisätty onnistuneesti.")

def lue_muistikirjaa(muistikirja):
    if len(muistikirja) == 0:
        print("Muistikirjassa ei ole merkintöjä.")
    else:
        for i, merkinta in enumerate(muistikirja, start=1):
            print(f"{i}) {merkinta}")

def tyhjenna_muistikirja(muistikirja):
    muistikirja.clear()
    print("Muistikirja tyhjennetty.")

def main():
    muistikirja = []
    while True:
        print("(1) Lue muistikirjaa")
        print("(2) Lisää merkintä")
        print("(3) Tyhjennä muistikirja")
        print("(4) Lopeta")

        valinta = input("Mitä haluat tehdä?: ")

        if valinta == "1":
            lue_muistikirjaa(muistikirja)
        elif valinta == "2":
            lisaa_merkinta(muistikirja)
        elif valinta == "3":
            tyhjenna_muistikirja(muistikirja)
        elif valinta == "4":
            print("Lopetetaan.")
            break
        else:
            print("Virheellinen valinta. Yritä uudelleen.")

if __name__ == "__main__":
    main()

```

(ei toimi)

**My solution:**

```python

import time

tiedoston_nimi = "muistio.txt"

try:
    tiedosto = open(tiedoston_nimi, "r")
    tiedosto.close()
except IOError:
    print("Oletusmuistioa ei löydy, luodaan tiedosto.")

while True:
    print("(1) Lue muistikirjaa\n(2) Lisää merkintä\n(3) Tyhjennä muistikirja\n(4) Lopeta\n")

    valinta = int(input("Mitä haluat tehdä?: "))

    if (valinta == 1):
        tiedosto = open(tiedoston_nimi, "r")
        sisalto = tiedosto.read()
        print(sisalto)
        tiedosto.close()
    elif (valinta == 2):
        tiedosto = open(tiedoston_nimi, "a")
        lisays = input("Kirjoita uusi merkintä: ")
        aika = time.strftime("%X %x")
        tiedosto.write(lisays + ":::" + aika)
        tiedosto.close()
    elif (valinta == 3):
        tiedosto = open(tiedoston_nimi, "w")
        print("Muistio tyhjennetty.")
        tiedosto.close()
    elif (valinta == 4):
        print("Lopetetaan.")
        break
    else:
        print("Tuntematon valinta")

```
