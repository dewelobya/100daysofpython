# Määrittele aluksi luokka Employee ja sen alustus-metodi. Employee -luokalla on kaksi attribuuttia: id ja name.

# Tee ohjelma,
# joka lisää listaan Employee-luokan olioita. Id on laskennallinen järjestysnumero alkaen luvusta 1 ja name (nimi) kysytään käyttäjältä.
# jonka suoritus lopetetaan käyttäjän antaessa nimen sijasta '0'.
# joka lopussa tulostaa listan sisällön alla olevan esimerkin mukaisesti.
# Ohjelmassa on käytettävä: class, def, for

class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name


tyontekijat = []
id_counter = 1

while True:
    nimi = input("Anna työntekijän nimi: (0 lopetus): ")

    if nimi == "0":
        break

    tyontekija = Employee(id_counter, nimi)
    tyontekijat.append(tyontekija)
    id_counter += 1

for tyontekija in tyontekijat:
    print("Id:", tyontekija.id, "Nimi:", tyontekija.name)
