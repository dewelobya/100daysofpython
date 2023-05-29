# Viope Python course non-stop 3 OP 

**Chapter 6.1: If-structure Challenge Instructions:**


Kolmannen luvun tehtävät aloitetaan yksinkertaisen if-rakenteen luomisella. 
Ohjelma pyytää käyttäjältä luvun ja tallentaa sen muuttujaan. 
Mikäli luku on parillinen, ohjelma tulostaa vastauksen "Antamasi luku oli parillinen". 
If-rakenteen ehtolauseeseen tarvittavat parametrit löydät luvun taulukosta, 
ja helpoin tapa toteuttaa ohjelma onkin käyttää jakojäännös-operaattoria, testaten onko jakojäännös 0. 
Ohjelman ei tarvitse myöskään reagoida virheellisiin syötteisiin eikä desimaalilukuihin. 
Ohjelma tulostaa seuraavan vastauksen:

```
Anna luku: 24
Antamasi luku oli parillinen.
```
tai vaihtoehtoisesti
```
Anna luku: 11

```

Eli ei mitään, mikäli luku ei ole parillinen.


**My solution:**
```python
luku = int(input("Anna luku: "))

if luku % 2 == 0:
    print("Antamasi luku oli parillinen.")
```


**Chapter 6.2: If-else-structure Challenge Instructions:**

Toinen harjoitustehtävä on jo hieman lähempänä varsinaista ohjelmointia, ja samalla hieman monimutkaisempi. Tehtävässä luodaan kaksi if-else-rakennetta, joista toinen sijoitetaan ensimmäisen sisään tyyliin:

```

if [valinta]:
	[koodia]
	
	if [Valinta]:
		[koodia]
	else:
		[koodia}
else:
	[koodia]

```
Ohjelmassa käyttäjältä pyydetään nimi ja salasana. Jos nimi on väärin, tulostaa ohjelma "Nimi oli väärin.". Jos nimi on oikein, pyydetään salasanaa. Jos salasana on oikein, tulostetaan "Salasana ja nimi oli oikein!", muussa tapauksessa "Salasana oli väärin.". Toteuta oikeaksi nimi-salasana-pariksi Erkki ja Esimerkki. Ohjelma tulostaa toimiessaan seuraavanlaisia vastauksia:

```
Anna nimi: Petteri
Nimi oli väärin.
```

tai vaihtoehtoisesti


```
Anna nimi: Erkki
Anna salasana: Kanada
Salasana oli väärin.
```

tai vaihtoehtoisesti

```

Anna nimi: Erkki
Anna salasana: Esimerkki
Salasana ja nimi oli oikein!
```

**First attempt (not correct)**

``` python
oikea_nimi = "Erkki"
oikea_salasana = "Esimerkki"

nimi = input("Anna nimi: ")
salasana = input("Anna salasana: ")

if nimi == oikea_nimi and salasana == oikea_salasana :
    print("Salasana ja nimi oli oikein!")
    if nimi == oikea_nimi:
        print("Nimi oli oikein.")
    else:
        print("Nimi oli väärin.")
else:
    print("Salasana ja nimi oli väärin.")
```
    
**My Solution:**
```python
nimi = str(input("Anna nimi: "))

if nimi == "Erkki":
    salasana = input("Anna salasana: ")
    if salasana == "Esimerkki":
        print("Salasana ja nimi oli oikein!")
    else:
        print("Salasana oli väärin.")
else:
    print("Nimi oli väärin.")
```
    
    
    
    

**Challenge Instructions:**

**My Solution:**

```python 

```


## Post Data with the Javascript XMLHttpRequest Method ##

**The Lesson:**

**Example:**

```python

```


**Challenge Instructions:**

**My Solution:**

```python 

```
    
