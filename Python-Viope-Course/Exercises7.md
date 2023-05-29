

**Chapger 7.1 While-structure**

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


## 7.2 While-rakenne avoimella katkaisulla ##

**The Lesson:**
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


**Example:**

```python

```


**Challenge Instructions:**

**My Solution:**

```python 

```
