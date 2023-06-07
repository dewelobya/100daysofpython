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

