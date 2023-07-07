**Ch12.1 Tehtävä 1: Listan luominen**

9. luvun tehtävissä keskitytään Pythonin tehokkaimpaan sarjalliseen tietomuotoon, eli listaan. Ensimmäinen tehtävä onkin lyhyt perehdytys listan käyttämiseen. Muodosta lista, jossa on neljä alkioita, joilla on arvot "Sininen", "Punainen", "Keltainen" ja "Vihreä". Tämän jälkeen ota listasta leikkaus jossa on 1. alkio (paikalta 0), sekä tulosta listan kaikki alkiot for-lausetta apuna käyttäen. Toimiessaan ohjelma tulostaa seuraavaa:



Listan ensimmäinen alkio on: Sininen
Lista tulostettuna alkio kerrallaan:
Sininen
Punainen
Keltainen
Vihreä


**My solution:**
```python
lista = ["Sininen", "Punainen", "Keltainen", "Vihreä"]


leikkaus = lista[0]
print("Listan ensimmäinen alkio on:", leikkaus)

print("Lista tulostettuna alkio kerrallaan:")
for alkio in lista:
    print(alkio)

```

**ch12.2 Tehtävä 2: Listan käyttäminen**
Toisessa tehtävässä luodaan ostoslista käyttäen Pythonin lista-tietomuotoa. Tee ohjelma, jossa käyttäjä voi (1) lisätä tuotteita listaan, (2) poistaa tuotteita listalta tai (3) lopettaa.


Mikäli käyttäjä lisää tuotteen listaan, pyytää ohjelma syötteen "Mitä lisätään?: ") ja laittaa sen listan viimeiseksi alkioksi. Jos käyttäjä haluaa poistaa tuotteen, kertoo ohjelma "Listalla on [määrä] alkiota", ja käyttäjä antaa syötteen "Monesko niistä poistetaan?", jonka jälkeen ohjelma poistaa numeronmukaisen alkion (0 on siis 1. alkio).


Jos käyttäjä lopettaa, tulostaa ohjelma "Listalla oli tuotteet:" ja listan sisällön kokonaisuudessaan allekkain. Virheelliseen valintaan reagoidaan tulostamalla rivi "Virheellinen valinta". Tämä koskee myös sitä jos käyttäjä valitsee poistettavan alkion listan ulkopuolelta. Toimiessaan ohjelma tulostaa seuraavaa:

```python
Haluatko
(1)Lisätä listaan
(2)Poistaa listalta vai 
(3)Lopettaa?: 1
Mitä lisätään?: Omenoita
Haluatko
(1)Lisätä listaan
(2)Poistaa listalta vai 
(3)Lopettaa?: 1
Mitä lisätään?: Olutta
Haluatko
(1)Lisätä listaan
(2)Poistaa listalta vai 
(3)Lopettaa?: 2
Listalla on 2 alkiota.
Monesko niistä poistetaan?: 0
Haluatko
(1)Lisätä listaan
(2)Poistaa listalta vai 
(3)Lopettaa?: 3
Listalla oli tuotteet:
Olutta

```
tai vaihtoehtoisesti vaikkapa
```python


Haluatko
(1)Lisätä listaan
(2)Poistaa listalta vai 
(3)Lopettaa?: 2
Listalla on 0 alkiota.
Monesko niistä poistetaan?: 1231
Virheellinen valinta.
Haluatko
(1)Lisätä listaan
(2)Poistaa listalta vai 
(3)Lopettaa?: 6
Virheellinen valinta.
Haluatko
(1)Lisätä listaan
(2)Poistaa listalta vai 
(3)Lopettaa?: 3
Listalla oli tuotteet:
```
**My Solution:**

```python
lista = []

while True:
    valinta = int(input("Haluatko\n(1)Lisätä listaan\n(2)Poistaa listalta vai\n(3)Lopettaa?: "))
    if valinta == 1:
        lisays = input("Mitä lisätään?: ")
        lista.append(lisays)
    elif valinta == 2:
        try:
            pituus = len(lista)
            print("Listalla on {0} alkiota.".format(pituus))
            poisto = int(input("Monesko niistä poistetaan?: "))
            lista.pop(poisto)
        except IndexError:
            print("Virheellinen valinta.")
    elif valinta == 3:
        print("Listalla oli tuotteet: ")
        for i in lista:
            print(i)
        break
    else:
        print("Virheellinen valinta.")
```

**ch12.3 Tehtävä 3: Listan metodit**
Luvun kolmannessa tehtävässä puhutaan listasta ja tiedostojen käsittelystä. Meillä on olemassa tiedosto "sanoja.txt", joka sisältää joukon erilaisia sanoja. Tehtävänäsi on lukea sanat muistiin, laittaa ne aakkosjärjestykseen ja tulostaa ruudulle allekkain selitteen "Sanat laitettuna aakkosjärjestykseen:" alle. Toimiessaan oikein ohjelma tulostaa vaikkapa seuraavaa:

```

Sanat laitettuna aakkosjärjestykseen:
aavikkorotta
autokauppias
hattuteline
huono
kaljakori
kivitalo
kumipallo
lapio
puuveistos
rautanaula
saunatonttu
tuuli

```

Kaikki sanat alkavat pienellä kirjaimella ja niiden jälkeen on rivinvaihto. Tehtävää varten kannattaa erityisesti tutustua listan metodiin .sort, sekä muistaa rivinvaihtojen poistaminen luetuista sanoista.

**My solution:**

```python
# Avataan tiedosto lukutilassa
with open("sanoja.txt", "r") as tiedosto:
    # Luetaan tiedoston sisältö ja tallennetaan sanat listaan
    sanat = tiedosto.read().splitlines()

# Lajitellaan sanat aakkosjärjestykseen
sanat.sort()

# Tulostetaan sanat ruudulle
print("Sanat laitettuna aakkosjärjestykseen:")
for sana in sanat:
    print(sana)
```


**ch12.4 Tehtävä 4: Muistikirja listan käyttäminen tietojen muokkaamiseen pickle**
Kurssin viimeinen proseduraaliseen ohjelmointiin liittyvä tehtävä on eräänlainen päättötyö, joka kokoaa kaikki kurssilla käsitellyt asiat yhteen kokonaisuuteen. Tässä tehtävässä muokataan muistikirja-harjoitustehtävää viimeisen kerran. Koska ohjelman rakenne muuttuu melko paljon, myös "puhtaalta pöydältä" aloittaminen on ihan järkevä vaihtoehto.

 

Työssä rakennetaan muistikirja, joka käyttää merkintöjen hallintaan Pythonin lista-tietorakennetta sekä tallentaa muistikirjan bittimuotoisena tietokoneen levylle. Ohjelmassa on seuraavat ominaisuudet:
A) Ohjelmaan voidaan lisätä merkintöjä, joissa on samanlainen aikaleima kuin aiemmin.
B)Ohjelmassa voi valita merkinnän listalta, ja korvata sen uudella.
C)Ohjelmalla voi poistaa yksittäisen merkinnän listalta, sekä
D)Ohjelma lataa aiemmin luodun listan ohjelman käynnistyessä mikäli sellainen on olemassa.

 

Ohjelma käyttää tietokantanaan tiedostoa nimeltä "muistio.dat". Käynnistyessään ohjelma koittaa ladata aiemmin luodun listan ko. tiedostosta, tai mikäli tällaista ei ole olemassa tai sen lataaminen tuottaa virheen, luo uuden ilmoittaen "Virhe tiedostossa, luodaan uusi muistio.dat.". Tämän jälkeen käyttäjä voi lisätä merkintljä listalle kuten aiemmin:

 ```


Virhe tiedostossa, luodaan uusi muistio.dat.
(1) Lue muistikirjaa
(2) Lisää merkintä
(3) Muokkaa merkintää
(4) Poista merkintä
(5) Tallenna ja lopeta

Mitä haluat tehdä?: 2
Kirjoita uusi merkintä: -Osta kananmunia
(1) Lue muistikirjaa
(2) Lisää merkintä
(3) Muokkaa merkintää
(4) Poista merkintä
(5) Tallenna ja lopeta

Mitä haluat tehdä?: 2
Kirjoita uusi merkintä: -Osta perunoita
 
```
Käyttäjä voi myös halutessaan muuttaa yksittäistä merkintää valinnalla 3. Tämän jälkeen ohjelma ilmoittaa listalla olevien merkintöjen määrän "Listalla on [määrä] merkintää." Pyytää käyttäjältä muutettavan merkinnän numeron "Mitä niistä muutetaan?:". Käyttäjä ilmoittaa haluamansa luvun ja voi tämän jälkeen vaihtaa tekstin ja saa uuden aikamerkinnän. Huomaa, että pyydettäessä numeroa ohjelma ymmärtää luvun 1 tarkoittavan ensimmäistä merkintää eli listan alkiota [0].

 


**My Solution:**
```python
import time
import pickle

tiedoston_nimi = "muistio.dat"
lista = []

try:
    tiedosto = open(tiedoston_nimi, "rb")
    lista = pickle.load(tiedosto)
    tiedosto.close()
except IOError:
    print("Virhe tiedostossa, luodaan uusi muistio.dat.")
    tiedosto = open(tiedoston_nimi, "wb")

while True:
    print("(1) Lue muistikirjaa\n(2) Lisää merkintä\n(3) Muokkaa merkintää\n(4) Poista merkintä\n(5) Tallenna ja "
          "lopeta\n")

    valinta = int(input("Mitä haluat tehdä?: "))

    if (valinta == 1):
        for i in lista:
            print(i)
    elif (valinta == 2):
        lisays = input("Kirjoita uusi merkintä: ")
        aika = time.strftime("%X %x")
        kokonaisuus = lisays + ":::" + aika
        lista.append(kokonaisuus)
        pickle.dump(lista, tiedosto)
    elif (valinta == 3):
        try:
            pituus = len(lista)
            print("Listalla on {0} merkintää.".format(pituus))
            muutos_valinta = int(input("Mitä niistä muutetaan?: "))
            muutos_valinta = muutos_valinta - 1
            print(lista[muutos_valinta])
        except IndexError:
            print("Virheellinen valinta.")
        else:
            uusi_teksti = input("Anna uusi teksti: ")
            aika = time.strftime("%X %x")
            kokonaisuus = uusi_teksti + ":::" + aika
            lista.pop(muutos_valinta)
            lista.insert(muutos_valinta, kokonaisuus)
            tiedosto = open(tiedoston_nimi, "wb")
            pickle.dump(lista, tiedosto)
            tiedosto.close()
    elif (valinta == 4):
        pituus = len(lista)
        print("Listalla on {0} merkintää.".format(pituus))
        poisto_valinta = int(input("Mitä niistä poistetaan?: "))
        try:
            poisto_valinta = poisto_valinta - 1
            print("Poistettiin merkintä {0}".format(lista[poisto_valinta]))
            lista.pop(poisto_valinta)
            tiedosto = open(tiedoston_nimi, "wb")
            pickle.dump(lista, tiedosto)
            tiedosto.close()
        except IndexError:
            print("Virheellinen valinta.")
    elif (valinta == 5):
        tiedosto = open(tiedoston_nimi, "wb")
        pickle.dump(lista, tiedosto)
        print("Lopetetaan.")
        tiedosto.close()
        break
    else:
        print("Tuntematon valinta")
```
