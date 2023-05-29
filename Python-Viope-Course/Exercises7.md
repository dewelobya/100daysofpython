

**Challenge Instructions: 7.1 While-structure**

Tämän luvun ensimmäinen tehtävä on yksinkertaisen while-rakenteen toteuttaminen. Tehtävänä onkin luoda ohjelma, joka tulostaa joka kierroksella kierrosluvun, millä tällä hetkellä ollan. Ohjelma aloittaa kierroksesta 0, ja jatkaa tästä eteenpäin 4 kierrosta. Toimiessaan ohjelma tulostaa seuraavan tekstin:


```
Olemme kierroksella 0
Olemme kierroksella 1
Olemme kierroksella 2
Olemme kierroksella 3
Olemme kierroksella 4
```

Toistorakenteen ehto kannattaa suunnitella kahta muuttujaa käyttäen, joista toinen määrää ylärajan ja toiseen lasketaan aina käynnissä oleva kierros.


Example output:
```
Olemme kierroksella 0
Olemme kierroksella 1
Olemme kierroksella 2
Olemme kierroksella 3
Olemme kierroksella 4
```

**My Solution:**

```python 
kierros = 0
while kierros <= 4:
    print("Olemme kierroksella", kierros)
    kierros += 1
```


**Challenge Instructions: 7.2 While-rakenne avoimella katkaisulla**

Tämän luvun ohjelmointitehtävä liittyy avoimeen toistoon, jossa toistorakenne toteutetaan siten, että käyttäjän syötteet ratkaisevat sen milloin ohjelma lopetetaan.


Toteuta ohjelma, joka joka kierroksen alussa pyytää käyttäjältä merkkijonon ja tulostaa sen ruudulle. Ainoan poikkeuksen tähän tekee tilanne, jossa käyttäjä kirjoittaa tekstin "lopeta", jolloin ohjelma tulostaa tekstin "Lopetit ohjelman" ja sammuu. Toimiessaan oikein ohjelma tulostaa seuraavaa:


```
Kirjoita jotain: testi
testi
Kirjoita jotain: Urjala
Urjala
Kirjoita jotain: lopeta
Lopetit ohjelman.
```

Ohjelma kannattaa sijoittaa yhden "while True:"-rakenteen sisään, ja katkaisuehto sitoa if-valintarakenteeseen ja break-käskyyn.


**My solution:**

```python
while True:
    syote = input("Kirjoita jotain: ")

    if syote == "lopeta":
        print("Lopetit ohjelman.")
        break
    else:
        print(syote)
```


**Challenge Instructions:7.3 For structure and in range**
Kolmas tehtävä käyttää for-toistorakennetta ja se on hieman aiempia monimutkaisempi. Tee ohjelma, joka pyytää käyttäjältä kierrosmäärän. Tämän jälkeen tee ohjelma, joka laskee kierroslukujen kertymän. Eli jos käyttäjä antaa syötteen 3, laskee ohjelma 0+1+2, jos 5 niin 0+1+2+3+4. Lopuksi ohjelma tulostaa käyttäjälle lopputuloksen muodossa "Kertymäksi saatiin:" ja vastaus.


Toimiessaan oikein ohjelma tulostaa seuraavaa:


```
Kuinka monta kierrosta?: 3
Kertymäksi saatiin: 3

```
Tehtävässä kannattaa kokeilla kuinka kierrosluvun lisääminen muuttujaan toimii, eli vaikkapa tulos = tulos + kierrosluku.

**My Solution:**

```python 

kierros = int(input("Kuinka monta kierrosta?: "))
kertyma = 0

for i in range(kierros):
    kertyma += i

print("Kertymäksi saatiin:", kertyma)


```


**Challenge Instructions: 7.4 Nelilaskin: useampi laskutehtävä, numeron vaihtaminen**
Luvun viimeisessä tehtävässä jatkamme eteenpäin aiemmin tekemäämme laskinta. Tällä kertaa ohjelmaan tehdään seuraavat lisätoiminnot: (A) laskin ei sammu heti laskutoimituksen jälkeen, vaan käyttäjä voi valita useamman laskutehtävän ja ohjelma sammuu vasta kun käyttäjä valitsee 6, sekä (B) Käyttäjä voi valinnalla 5 vaihtaa käyttämänsä luvut. Toimiessaan ohjlma toimii esimerkiksi seuraavalla tavalla:



Anna ensimmäinen luku: 10
Anna toinen luku: 15
(1) +
(2) -
(3) *
(4) /
(5)Vaihda luvut
(6)Lopeta
Valitut luvut: 10 15
Tee valinta (1-6): 2
Tulos on: -5
(1) +
(2) -
(3) *
(4) /
(5)Vaihda luvut
(6)Lopeta
Valitut luvut: 10 15
Tee valinta (1-6): 5
Anna uusi ensimmäinen luku: 20
Anna uusi toinen luku: 10
(1) +
(2) -
(3) *
(4) /
(5)Vaihda luvut
(6)Lopeta
Valitut luvut: 20 10
Tee valinta (1-6): 6


Jälleen kerran koko varsinainen ohjelma kannattaa sijoittaa toistorakenteen sisään, jolloin katkaisu on helppo toteuttaa break-käskyllä.


**First attempt:**

```python
while True:
    luku1 = int(input("Anna ensimmäinen luku: "))
    luku2 = int(input("Anna toinen luku: "))
    valitut_luvut = [luku1, luku2]

    while True:
        print("(1) +")
        print("(2) -")
        print("(3) *")
        print("(4) /")
        print("(5) Vaihda luvut")
        print("(6) Lopeta")
        valinta = int(input("Tee valinta (1-6): "))

        if valinta == 1:
            tulos = luku1 + luku2
            print("Tulos on:", tulos)
        elif valinta == 2:
            tulos = luku1 - luku2
            print("Tulos on:", tulos)
        elif valinta == 3:
            tulos = luku1 * luku2
            print("Tulos on:", tulos)
        elif valinta == 4:
            tulos = luku1 / luku2
            print("Tulos on:", tulos)
        elif valinta == 5:
            luku1 = int(input("Anna uusi ensimmäinen luku: "))
            luku2 = int(input("Anna uusi toinen luku: "))
            valitut_luvut = [luku1, luku2]
        elif valinta == 6:
            print("Lopetit ohjelman.")
            break
        else:
            print("Valintaa ei tunnistettu.")

    if valinta == 6:
        break

```

**My solution:**

```python

luku1 = int(input("Anna ensimmäinen luku: "))
luku2 = int(input("Anna toinen luku: "))

while True:

    print("""(1) +
(2) -
(3) *
(4) /
(5) Vaihda luvut
(6) Lopeta""")

    print("Valitut luvut: {0} {1}".format(luku1, luku2))
    valinta = int(input("Tee valinta (1-6): "))

    if valinta == 1:
        print("Tulos on:", luku1 + luku2)
    elif valinta == 2:
        print("Tulos on:", luku1 - luku2)
    elif valinta == 3:
        print("Tulos on:", luku1 * luku2)
    elif valinta == 4:
        print("Tulos on:", luku1 / luku2)
    elif valinta == 5:
        luku1 = int(input("Anna uusi ensimmäinen luku: "))
        luku2 = int(input("Anna uusi toinen luku: "))
    elif valinta == 6:
        break
    else:
        print("Valintaa ei tunnistettu.")

```
