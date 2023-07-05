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

**My solution:**

