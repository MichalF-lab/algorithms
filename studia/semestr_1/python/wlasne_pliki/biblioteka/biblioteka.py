# ToDo list
# 39-43 ogarnac zmienne globalne w funkcji lokalnej


# s____ -> schemat zmiennej
s_czy_wypozyczona = bool
s_id_ksiazki = int
s_autor = {
    'imie': str,
    'nazwisko': str,
    'rok_urodzenia': int
    }
# iterator po id ksiazki
id_ksiazki = 0
# dane pojedyńczej ksiazki !! lista bo jest ona mutowalna
ksiazka = [] # id_ksiazki, czy_wypozyczona, autor
# zbiór książek
ksiazki = [] # ksiazka
#lista autorów
autorzy = [] 

# kilka losowych autorów
autor1 = {'imie':'Andrzej', 'nazwisko':'Sapkowski', 'rok_urodzenia':1965}
autor2 = {'imie':'Jakub', 'nazwisko':'Domagała', 'rok_urodzenia':1982}
autor3 = {'imie':'Tomek', 'nazwisko':'Zawada', 'rok_urodzenia':1913}

# dodanie autorów do listy
autorzy.append(autor1)
autorzy.append(autor2)
autorzy.append(autor3)

def dodaj_autora(imie,nazwisko,rok_urodzenia):
    autor = {'imie':imie, 'nazwisko':nazwisko, 'rok_urodzenia':rok_urodzenia}
    autorzy.append(autor)

def dodaj_ksiazke(tytul,autor):
    ksiazka = [id_ksiazki,0,tytul,autor]
    ksiazki.append(ksiazka)
    # inkrementacja_id_ksiazki()


 #def inkrementacja_id_ksiazki():
    # id_ksiazki+=1

dodaj_autora('Janek','Stachowiak',1998)

dodaj_ksiazke("maly ksiaze", autorzy[0])
dodaj_ksiazke("w pustynie i puszczy", autorzy[2])


print(ksiazki)




# print(autorzy)
#print(autorzy[0]['imie'])
#print(ksiazka)