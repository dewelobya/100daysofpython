**Ch13.1. Tehtävä 1: Luokan tekeminen ja käyttäminen**
Luvun 10 tehtävissä ei enää koodata varsinaisesti toiminnallisia ohjelmia, vaan kokeillaan erilaisten esimerkkikoodien avulla luokkamäärittelyn tekemistä ja olioiden perustoimintoja. Tämä sen vuoksi, että kurssi ei varsinaisesti keskity olio-ohjelmointiin, vaan pyrkii ainoastaan ohjaamaan siinä alkuun ja ymmärtämään miten se eroaa proseduraalisesta ohjelmoinnista.


Ensimmäisessä oliotehtävässä luodaan määritellään luokkaa nimeltä Kilpailija, jolle annettaan kaksi jäsenmuuttujaa, pisteet ja vari. Tämän jälkeen luo luokasta olio "eka", jolle annetaan muuttujan vari arvoksi sininen ja pisteet arvoksi 10. Lopuksi laita ohjelmasi vielä tulostamaan olion tiedot muodossa "Kilpailijalla [väri] on [pisteet] pistettä!", eli näin:



Kilpailijalla sininen on 10 pistettä!


**My solution:**
```python

class kilpailija:
    """Luokka määrittelee kilpailijan pisteet ja värin"""

    __pisteet = 0
    __vari = ""

    def lisaa_pisteet(self, lisays=1):
        self.__pisteet = + lisays

    def lisaa_vari(self, valinta):
        self.__vari = valinta

    def tulostus(self):
        print("Kilpailijalla {0} on {1} pistettä!".format(self.__vari, self.__pisteet))


def main():
    eka = kilpailija()
    eka.lisaa_vari("Sininen")
    eka.lisaa_pisteet(10)
    eka.tulostus()


if __name__ == "__main__":
    main()
```

**ch13.2. Tehtävä 2: Jäsenfunktion käyttäminen**
Tässä tehtävässä jatketaan edellistä tehtävää. Muuta ohjelmaasi siten, että luokalla Kilpailija on kaksi jäsenfunktiota, tilanne ja maali. Kutsuttaessa funktiota tilanne olio tulostaa "Olen [vari] ja minulla on [pisteet] pistettä!". Kutsuttaessa funktiota maali olio lisää itselleen yhden pisteen.


Pääohjelma luo luokasta olion nimeltä "eka" ja antaa sille muuttujan eka.vari arvoksi "sininen". Lopuksi ohjelma kutsuu ensin jäsenfunktiota eka.maali() ja lopuksi funktiota eka.tilanne(). Ohjelma tulostaa siis seuraavaa:



Olen sininen ja minulla on 1 pistettä!




**My solution:**

```python
class kilpailija:
    """Luokka määrittelee kilpailijan pisteet ja värin"""

    __pisteet = 0
    __vari = ""

    def lisaa_pisteet(self, lisays=1):
        self.__pisteet = + lisays

    def lisaa_vari(self, valinta):
        self.__vari = valinta

    def tilanne(self):
        print("Olen {0} ja minulla on {1} pistettä!".format(self.__vari, self.__pisteet))

    def maali(self):
        self.__pisteet = + 1


def main():
    eka = kilpailija()
    eka.lisaa_vari("sininen")
    eka.maali()
    eka.tilanne()


if __name__ == "__main__":
    main()
```

**ch13.3. Tehtävä 3: Luokan alustaminen**

Kolmannessa tehtävässä Kilpailija-luokkaa muokataan kahdella tavalla. Ensinnäkin, kirjoita luokalle seliterivi "Kilpailija: sisältää pisteet ja värin". Toisekseen, lisää luokkaan alustusfunktio __init__, jossa uusi olio pyytää itselleen värin käyttäjän syötteenä "Anna minulle väri: ".


Pääohjelmassa tulee luoda kaksi oliota ja antaa näille alustuksessa värit "sininen" ja "punainen", tämän jälkeen kutsuen molempien tilanne-jäsenfunktiota. Lopuksi ohjelma vielä tulostaa ensimmäisen olion selostetekstin komennolla print([nimi].__doc__). Ohjelma tulostaa siis seuraavaa:


Anna minulle väri: sininen
Anna minulle väri: punainen
Olen sininen ja minulla on 0 pistettä!
Olen punainen ja minulla on 0 pistettä!
Kilpailija: sisältää pisteet ja värin

**My solution:**
```python
class kilpailija:
    """Kilpailija: sisältää pisteet ja värin"""

    __pisteet = 0
    __vari = ""

    def __init__(self):
        self.__vari = input("Anna minulle väri: ")

    def tilanne(self):
        print("Olen {0} ja minulla on {1} pistettä!".format(self.__vari, self.__pisteet))


def main():
    eka = kilpailija()
    toka = kilpailija()
    eka.tilanne()
    toka.tilanne()
    print(eka.__doc__)


if __name__ == "__main__":
    main()
```
**ch13.4. Tehtävä 4: Luokan periminen**

Luvun ja samalla kurssin viimeisessä tehtävässä kokeillaan luokkien perimistä.


Määrittele kaksi luokkaa nimeltä Emo ja Lapsi. Anna Emo-luokalle kaksi jäsenmuuttujaa, arvo ja tila, sekä jäsenfunktio nimi, jolla olio tulostaisi "Minä olen emoluokka". Anna muuttujalle arvo arvoksi 0, ja muuttujalle tila arvo "Toiminnassa".


Vastaavasti Lapsi-luokka peritään Emo-luokasta. määrittele lapsiluokalle ylikirjoittava funktio nimi, jolla olio tulostaa "Minä olen lapsiluokka."


Laita pääohjelma tekemään molemmista luokista oliot, joka jälkeen yritä tulostaa molempien olioiden tila-jäsenmuuttuja, sekä kutsu kummankin olion jäsenfunktiota nimi. Jos luokat on tehty oikein, tulostaa ohjelma näin:

```
Toiminnassa
Minä olen emoluokka.
Toiminnassa
Minä olen lapsiluokka.
```
**My solution:**

```python
class Emo:
    def __init__(self):
        self.arvo = 0
        self.tila = "Toiminnassa"

    def nimi(self):
        print("Minä olen emoluokka.")

class Lapsi(Emo):
    def nimi(self):
        print("Minä olen lapsiluokka.")

# Luodaan oliot
emo_olio = Emo()
lapsi_olio = Lapsi()

# Tulostetaan jäsenmuuttujat ja kutsutaan jäsenfunktioita
print(emo_olio.tila)
emo_olio.nimi()

print(lapsi_olio.tila)
lapsi_olio.nimi()

```


