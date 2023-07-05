# Alifunktiot # 


Tästä luvusta eteenpäin ohjelmissa, joissa on erillisiä alifunktioita, tulisi olla myös erillinen pääfunktio.

**Ch9: Tulostusalifunktion tekeminen:**

Ensimmäinen tehtävä on yksinkertaisen funktiorakenteen toteuttaminen. Tee ohjelma, jossa on pääfunktio main ja yksi alifunktio nimeltään tulostaja. Kutsuttaessa alifunktio ei vastaanota parametreja eikä palauta mitään, mutta tulostaa tekstin "Tulostusfunktio!". Pääohjelman ainoa toiminto on kutsua alifunktiota. Ohjelma tulostaa siis tekstin



Tulostusfunktio!


Muista myös laittaa ohjelmaan pääfunktiokutsu
```

if __name__ == "__main__":
    main()
```

**My solution:**

```python
def tulostaja():
    print("Tulostusfunktio!")

def main():
    tulostaja()

if __name__ == "__main__":
    main()
    
```

**Ch9: Parametrin välitys:**

Toinen tehtävä liittyy alifunktion parametrien välitykseen. Tee tehtävä, jossa on pääfunktio main ja alifunktio "toinenpotenssi". Alifunktio ottaa vastaan yhden parametrin, laskee sille toisen potenssin ja tulostaa vastauksen muodossa "Toinen potenssi on [vastaus]". Pääohjelma vastaavasti pyytää käyttäjältä lukua "Anna lukuarvo: " ja lähettää sen eteenpäin alifunktiolle. Toimiessaan oikein ohjelma toimii seuraavalla tavalla:


```
Anna lukuarvo: 10
Toinen potenssi on 100
```

Tai vaikkapa
```


Anna lukuarvo: 123123
Toinen potenssi on 15159273129
```

Muista myös laittaa ohjelmaan pääfunktiokutsu

```

if __name__ == "__main__":
    main()

```

**My Solution:**

```python

def toinenpotenssi(luku):
    tulos = luku ** 2
    print("Toinen potenssi on", tulos)

def main():
    luku = int(input("Anna lukuarvo: "))
    toinenpotenssi(luku)

if __name__ == "__main__":
    main()

```

**Ch9: Oletusparametrit:**


tulostaja-funktion toimintaa muutetaan siten, että se vastaanottaa yhden parametrin, jonka oletusarvona on "Oletustulostus" ja tulostaa saamansa arvon.


Pääfunktio taas pyytää käyttäjältä syötettä "Anna syöte (Lopeta lopettaa): ", ja mikäli käyttäjä antaa syötteen, joka on 5 tai useampi merkkiä, lähetetään se tulostaja-alifunktiolle. Muussa tapauksessa alifunktiota kutsutaan ilman parametriä. Jos käyttäjä antaa syötteen "Lopeta", ohjelma sammuu. Ohjelma toimii seuraavalla tavalla:



Anna syöte (Lopeta lopettaa): Pitkäsana
Pitkäsana
Anna syöte (Lopeta lopettaa): möh
Oletustulostus
Anna syöte (Lopeta lopettaa): Toinenkovinpitkäsana
Toinenkovinpitkäsana
Anna syöte (Lopeta lopettaa): Lopeta


Merkkijonon pituuden mittaaminen onnistuu helpoiten komennolla len().

**My solution:**

```python
def main():
    while True:
        syote = input("Anna syöte (Lopeta lopettaa): ")
        if syote == "Lopeta":
            break
        elif len(syote) >= 5:
            tulostaja(syote)
        else:
            tulostaja()


def tulostaja(tulostus="Oletustulostus"):
    print(tulostus)


if __name__ == "__main__":
    main()
```

**Ch9: Paluuarvojen hyödyntäminen**
Neljäs tehtävä lisää ohjelmaan paluuarvon. Tee ohjelma, jossa on pääfunktio main ja alifunktio pituusmitta. pituusmitta saa syötteenä parametrin ja mittaa tämän parametrin pituuden, palauttaen sen integer-arvona pääohjelmalle.


Pääohjelma pyytää käyttäjältä syötettä "Anna syote (Lopeta lopettaa): " ja lähettää syötteen mitattavaksi. Jos tulos on 0, ohjelma vastaa "Et antanut syötettä", muuten "Antamasi syöte oli [pituus] merkkiä pitkä.". Jos käyttäjä antaa arvon Lopeta, ohjelma sammuu. Ohjelma tulostaa seuraavaa:
**My solution:**

```python
def main():
    while True:
        syote = input("Anna syöte (Lopeta lopettaa): ")
        if syote == "Lopeta":
            break
        elif len(syote) == 0:
            print("Et antanut syötettä")
        else:
            print("Antamasi syöte oli {0} merkkiä pitkä.".format(len(syote)))


if __name__ == "__main__":
    main()

```python
