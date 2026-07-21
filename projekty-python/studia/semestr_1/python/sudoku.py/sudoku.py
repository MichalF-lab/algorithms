# tworzenie tablicy
import numpy as np

# Głeboka kopia sudoku
import copy

# Przydatne do sprawdzania czy cos jest liczba
import numbers

# Dane to zdefiniowania indywidualnie
lokalizcja = "studia\semestr_1\python\sudoku.py\sudoku.txt"

# ----------------------------------------------------------------------
# tworzenie / imort tablic testy

# plansza1 = np.empty((9,9),dtype="u1")

# planszza na ktorej oprujemmy
def stwórz_plansze():
    plansza = np.empty((9,9),dtype="u1")
    return plansza

def uzupelni_plansze_z_pliku(plik, plansza, liczba):
     file = open(plik)
     for line in file:
        f = file.readline()
        if("Grid" in str(f) and str(liczba) in str(f)):
            # dla każdego wiersza
            f = file.readline()
            for i in range(9):
                print(f) # TODO ten print musi byc
                # dla każdego numerku
                for zmienna in range(9):
                    if(int(f[zmienna]) != 0):
                        plansza[i][zmienna] = int(f[zmienna])
                    #print(f[zmienna])
                f = file.readline()
                    
     return plansza

#-----------------------------------------------------------------------
# implementacja kilku tablic + testy

#plansza_1 = stwórz_plansze()
#plansza_1 = uzupelni_plansze_z_pliku(lokalizcja,plansza_1,19)
#print(plansza_1)
# print((1,) == tuple)
# test = (1,)
# print(isinstance(test,numbers.Number))

#-----------------------------------------------------------------------
#Funkcje podstawowe wykorzystywane w innych funkcjach

def czy_istnieje_poziomo(plansza,liczba,nr_rzedu):
    for i in range(9):
        if (plansza[i][nr_rzedu] == liczba): return True
    return False

def czy_istnieje_pionowo(plansza,liczba,nr_rzedu):
    for i in range(9):
        if (plansza[nr_rzedu][i] == liczba): return True
    return False

def czy_ustalone(plansza,i,j):
    
    if(plansza[i][j] == 0): return False
    temp = np.empty((1),dtype="u1")
    # Jeśli jest w szybkiej tablicy
    if(type(plansza[i][j]) == type(temp[0])): return True
    # Jeśli jest w tablicy z wariantami
    if(isinstance(plansza[i][j], numbers.Number)): return True
    return False

#--------------------------------------------------------------------------------
# Funkcje Trywialne (jedyne wolne miejsce)

def szukanie_poziomo(plansza,liczba):
        for i in range(9):
            # Dla każdego miejsca w rzedzie
            if(czy_istnieje_poziomo(plansza,liczba,i) == False):
                # Jeżeli liczba nie występuje w danym rzedzie
                for j in range(9):
                    # Sprawdzamy po kolmnach
                    if(czy_ustalone(plansza,i,j) == False):
                        #Jeżeli na danym polu nie ma konkretnej liczby
                        #Sprawdzamy czy pozostałe miejsca sa zajęte
                        temp = 0
                        for miejsce in range(9):
                            if(czy_ustalone(plansza,i,miejsce)==False): temp+=1
                        # jeżeli wszystkie pozostałe miejsca sa zajęte to w to miejsce pasuje tylko jedna liczba
                        if(temp==1): plansza[i][j] = liczba


def szukanie_pionowo(plansza,liczba):
        for i in range(9):
            # Dla każdego miejsca w rzedzie
            if(czy_istnieje_pionowo(plansza,liczba,i) == False):
                # Jeżeli liczba nie występuje w danej kolumnie
                for j in range(9):
                    # Sprawdzamy po kolmnach
                    if(czy_ustalone(plansza,j,i) == False):
                        #Jeżeli na danym polu nie ma konkretnej liczby
                        #Sprawdzamy czy pozostałe miejsca sa zajęte
                        temp = 0
                        for miejsce in range(9):
                            if(czy_ustalone(plansza,miejsce,j)==False): temp+=1
                        # jeżeli wszystkie pozostałe miejsca sa zajęte to w to miejsce pasuje tylko jedna liczba
                        if(temp==1): plansza[j][i] = liczba


def szukanie_w_kwadracie(plansza):
    #piewrsza komórka
    for i in range(3):
        for j in range(3):
            if(czy_ustalone(plansza,i,j)):
                temp = 0
                for temp_i in range(3):
                    for temp_j in range(3):
                        if(plansza[i][j] == False): temp+=1
                if(temp != 1): return # zakończ jeżeli sa dwa wolne miejsca
                tab = [range(1,9)]
                for temp_i in range(3):
                    for temp_j in range(3):
                        if(plansza[i][j] == True): tab.remove(plansza[temp_i][temp_j])
                plansza[i][j] = int(tab)
    #druga komoórka
    for i in range(3,6):
        for j in range(3):
            if(czy_ustalone(plansza,i,j)):
                temp = 0
                for temp_i in range(3):
                    for temp_j in range(3):
                        if(plansza[i][j] == False): temp+=1
                if(temp != 1): return # zakończ jeżeli sa dwa wolne miejsca
                tab = [range(1,9)]
                for temp_i in range(3):
                    for temp_j in range(3):
                        if(plansza[i][j] == True): tab.remove(plansza[temp_i][temp_j])
                plansza[i][j] = int(tab)
    #trzecia komórka
    for i in range(6,9):
        for j in range(3):
            if(czy_ustalone(plansza,i,j)):
                temp = 0
                for temp_i in range(3):
                    for temp_j in range(3):
                        if(plansza[i][j] == False): temp+=1
                if(temp != 1): return # zakończ jeżeli sa dwa wolne miejsca
                tab = [range(1,9)]
                for temp_i in range(3):
                    for temp_j in range(3):
                        if(plansza[i][j] == True): tab.remove(plansza[temp_i][temp_j])
                plansza[i][j] = int(tab)
    #czwarta komórka
    for i in range(3):
        for j in range(3,6):
            if(czy_ustalone(plansza,i,j)):
                temp = 0
                for temp_i in range(3):
                    for temp_j in range(3):
                        if(plansza[i][j] == False): temp+=1
                if(temp != 1): return # zakończ jeżeli sa dwa wolne miejsca
                tab = [range(1,9)]
                for temp_i in range(3):
                    for temp_j in range(3):
                        if(plansza[i][j] == True): tab.remove(plansza[temp_i][temp_j])
                plansza[i][j] = int(tab)
    #piata komórka
    for i in range(3,6):
        for j in range(3,6):
            if(czy_ustalone(plansza,i,j)):
                temp = 0
                for temp_i in range(3):
                    for temp_j in range(3):
                        if(plansza[i][j] == False): temp+=1
                if(temp != 1): return # zakończ jeżeli sa dwa wolne miejsca
                tab = [range(1,9)]
                for temp_i in range(3):
                    for temp_j in range(3):
                        if(plansza[i][j] == True): tab.remove(plansza[temp_i][temp_j])
                plansza[i][j] = int(tab)
    #szósta komórka
    for i in range(6,9):
        for j in range(3,6):
            if(czy_ustalone(plansza,i,j)):
                temp = 0
                for temp_i in range(3):
                    for temp_j in range(3):
                        if(plansza[i][j] == False): temp+=1
                if(temp != 1): return # zakończ jeżeli sa dwa wolne miejsca
                tab = [range(1,9)]
                for temp_i in range(3):
                    for temp_j in range(3):
                        if(plansza[i][j] == True): tab.remove(plansza[temp_i][temp_j])
                plansza[i][j] = int(tab)
    #siódma komórka
    for i in range(3):
        for j in range(6,9):
            if(czy_ustalone(plansza,i,j)):
                temp = 0
                for temp_i in range(3):
                    for temp_j in range(3):
                        if(plansza[i][j] == False): temp+=1
                if(temp != 1): return # zakończ jeżeli sa dwa wolne miejsca
                tab = [range(1,9)]
                for temp_i in range(3):
                    for temp_j in range(3):
                        if(plansza[i][j] == True): tab.remove(plansza[temp_i][temp_j])
                plansza[i][j] = int(tab)
    #ósma komórka
    for i in range(3,6):
        for j in range(6,9):
            if(czy_ustalone(plansza,i,j)):
                temp = 0
                for temp_i in range(3):
                    for temp_j in range(3):
                        if(plansza[i][j] == False): temp+=1
                if(temp != 1): return # zakończ jeżeli sa dwa wolne miejsca
                tab = [range(1,9)]
                for temp_i in range(3):
                    for temp_j in range(3):
                        if(plansza[i][j] == True): tab.remove(plansza[temp_i][temp_j])
                plansza[i][j] = int(tab)
    #dziewiąta komórka
    for i in range(6,9):
        for j in range(6,9):
            if(czy_ustalone(plansza,i,j)):
                temp = 0
                for temp_i in range(3):
                    for temp_j in range(3):
                        if(plansza[i][j] == False): temp+=1
                if(temp != 1): return # zakończ jeżeli sa dwa wolne miejsca
                tab = [range(1,9)]
                for temp_i in range(3):
                    for temp_j in range(3):
                        if(plansza[i][j] == True): tab.remove(plansza[temp_i][temp_j])
                plansza[i][j] = int(tab)

#---------------------------------------------------------------------------------------------------
# Funkcje niecobardziej zawansowane

#Dla danego pola sprawdza czy w tym kwadracie istnieja inne polew ktore można wpisać to liczbe
def ostatnie_pozostałe_wolne_pole_w_kwadracie(plansza,liczba):
    for i in range(3):
        for j in range(3):
            if(czy_ustalone(plansza,i,j) == False):
                # print(plansza[i][j])
                if(i%3 == 0 and j%3 == 0):
                    # Jesli jest w górnej lewej kratce
                    if(
                        czy_istnieje_pionowo(plansza,liczba,i+1) == True and
                        czy_istnieje_pionowo(plansza,liczba,i+2) == True and

                        czy_istnieje_poziomo(plansza,liczba,j+1) == True and
                        czy_istnieje_poziomo(plansza,liczba,j+2) == True
                    ):
                        plansza[i][j] = liczba
                if(i%3 == 1 and j%3 == 0):
                # Jesli jest w środkowej lewej kratce
                    if(
                        czy_istnieje_pionowo(plansza,liczba,i+1) == True and
                        czy_istnieje_pionowo(plansza,liczba,i-1) == True and

                        czy_istnieje_poziomo(plansza,liczba,j+1) == True and
                        czy_istnieje_poziomo(plansza,liczba,j+2) == True
                    ):
                        plansza[i][j] = liczba
                if(i%3 == 2 and j%3 == 0):
                # Jesli jest w dolnej lewej kratce
                    if(
                        czy_istnieje_pionowo(plansza,liczba,i-1) == True and
                        czy_istnieje_pionowo(plansza,liczba,i-2) == True and

                        czy_istnieje_poziomo(plansza,liczba,j+1) == True and
                        czy_istnieje_poziomo(plansza,liczba,j+2) == True
                    ):
                        plansza[i][j] = liczba
                if(i%3 == 0 and j%3 == 1):
                # Jesli jest w górnej środkowej kratce
                    if(
                        czy_istnieje_pionowo(plansza,liczba,i+1) == True and
                        czy_istnieje_pionowo(plansza,liczba,i+2) == True and

                        czy_istnieje_poziomo(plansza,liczba,j+1) == True and
                        czy_istnieje_poziomo(plansza,liczba,j-1) == True
                    ):
                        plansza[i][j] = liczba
                if(i%3 == 1 and j%3 == 1):
                # Jesli jest na środku
                    if(
                        czy_istnieje_pionowo(plansza,liczba,i+1) == True and
                        czy_istnieje_pionowo(plansza,liczba,i-1) == True and

                        czy_istnieje_poziomo(plansza,liczba,j+1) == True and
                        czy_istnieje_poziomo(plansza,liczba,j-1) == True
                    ):
                        plansza[i][j] = liczba
                if(i%3 == 2 and j%3 == 1):
                # Jesli jest w donej środkowej kratce
                    if(
                        czy_istnieje_pionowo(plansza,liczba,i-1) == True and
                        czy_istnieje_pionowo(plansza,liczba,i-2) == True and

                        czy_istnieje_poziomo(plansza,liczba,j+1) == True and
                        czy_istnieje_poziomo(plansza,liczba,j-1) == True
                    ):
                        plansza[i][j] = liczba
                if(i%3 == 0 and j%3 == 2):
                # Jesli jest w górnej prawej kratce
                    if(
                        czy_istnieje_pionowo(plansza,liczba,i+1) == True and
                        czy_istnieje_pionowo(plansza,liczba,i+2) == True and

                        czy_istnieje_poziomo(plansza,liczba,j-1) == True and
                        czy_istnieje_poziomo(plansza,liczba,j-2) == True
                    ):
                        plansza[i][j] = liczba
                if(i%3 == 1 and j%3 == 2):
                # Jesli jest w środkowej prawej kratce
                    if(
                        czy_istnieje_pionowo(plansza,liczba,i+1) == True and
                        czy_istnieje_pionowo(plansza,liczba,i-1) == True and

                        czy_istnieje_poziomo(plansza,liczba,j-1) == True and
                        czy_istnieje_poziomo(plansza,liczba,j-2) == True
                    ):
                        plansza[i][j] = liczba
                if(i%3 == 2 and j%3 == 2):
                # Jesli jest w dolnej praw kratce
                    if(
                        czy_istnieje_pionowo(plansza,liczba,i-1) == True and
                        czy_istnieje_pionowo(plansza,liczba,i-2) == True and

                        czy_istnieje_poziomo(plansza,liczba,j-1) == True and
                        czy_istnieje_poziomo(plansza,liczba,j-2) == True
                    ):
                        plansza[i][j] = liczba

# Dla danego pola sprawdza czy w tym kwadracie istnieja inne polew ktore można wpisać to liczbe + dodatkowe miejsca poziomo juz sa zajete (w inne pola nie da sie nawet zalozyc ze bedzzie ta liczba)
def ostatnie_pozostałe_wolne_pole_w_kwadracie_poziomo(plansza,liczba):
    for i in range(3):
        for j in range(3):
            if(czy_ustalone(plansza[i][j] == False)):
                if(i%3 == 0 and j%3 == 0):
                    # Jesli jest w górnej lewej kratce
                    if(
                        czy_istnieje_pionowo(plansza,liczba,i+1) == True and
                        czy_istnieje_pionowo(plansza,liczba,i+2) == True and

                        czy_ustalone(plansza,i,j+1) == True and
                        czy_ustalone(plansza,i,j+2) == True
                    ):
                        plansza[i][j] = liczba
                if(i%3 == 1 and j%3 == 0):
                # Jesli jest w środkowej lewej kratce
                    if(
                        czy_istnieje_pionowo(plansza,liczba,i+1) == True and
                        czy_istnieje_pionowo(plansza,liczba,i-1) == True and

                        
                        czy_ustalone(plansza,i,j+1) == True and
                        czy_ustalone(plansza,i,j+2) == True
                    ):
                        plansza[i][j] = liczba
                if(i%3 == 2 and j%3 == 0):
                # Jesli jest w dolnej lewej kratce
                    if(
                        czy_istnieje_pionowo(plansza,liczba,i-1) == True and
                        czy_istnieje_pionowo(plansza,liczba,i-2) == True and

                        czy_ustalone(plansza,i,j+1) == True and
                        czy_ustalone(plansza,i,j+2) == True
                    ):
                        plansza[i][j] = liczba
                if(i%3 == 0 and j%3 == 1):
                # Jesli jest w górnej środkowej kratce
                    if(
                        czy_istnieje_pionowo(plansza,liczba,i+1) == True and
                        czy_istnieje_pionowo(plansza,liczba,i+2) == True and

                        czy_ustalone(plansza,i,j+1) == True and
                        czy_ustalone(plansza,i,j-1) == True
                    ):
                        plansza[i][j] = liczba
                if(i%3 == 1 and j%3 == 1):
                # Jesli jest na środku
                    if(
                        czy_istnieje_pionowo(plansza,liczba,i+1) == True and
                        czy_istnieje_pionowo(plansza,liczba,i-1) == True and

                        czy_ustalone(plansza,i,j+1) == True and
                        czy_ustalone(plansza,i,j-1) == True
                    ):
                        plansza[i][j] = liczba
                if(i%3 == 2 and j%3 == 1):
                # Jesli jest w donej środkowej kratce
                    if(
                        czy_istnieje_pionowo(plansza,liczba,i-1) == True and
                        czy_istnieje_pionowo(plansza,liczba,i-2) == True and

                        czy_ustalone(plansza,i,j+1) == True and
                        czy_ustalone(plansza,i,j-1) == True
                    ):
                        plansza[i][j] = liczba
                if(i%3 == 0 and j%3 == 2):
                # Jesli jest w górnej prawej kratce
                    if(
                        czy_istnieje_pionowo(plansza,liczba,i+1) == True and
                        czy_istnieje_pionowo(plansza,liczba,i+2) == True and

                        czy_ustalone(plansza,i,j-1) == True and
                        czy_ustalone(plansza,i,j-2) == True
                    ):
                        plansza[i][j] = liczba
                if(i%3 == 1 and j%3 == 2):
                # Jesli jest w środkowej prawej kratce
                    if(
                        czy_istnieje_pionowo(plansza,liczba,i+1) == True and
                        czy_istnieje_pionowo(plansza,liczba,i-1) == True and

                        czy_ustalone(plansza,i,j-1) == True and
                        czy_ustalone(plansza,i,j-2) == True
                    ):
                        plansza[i][j] = liczba
                if(i%3 == 2 and j%3 == 2):
                # Jesli jest w dolnej praw kratce
                    if(
                        czy_istnieje_pionowo(plansza,liczba,i-1) == True and
                        czy_istnieje_pionowo(plansza,liczba,i-2) == True and

                        czy_ustalone(plansza,i,j-1) == True and
                        czy_ustalone(plansza,i,j-2) == True
                    ):
                        plansza[i][j] = liczba


# Dla danego pola sprawdza czy w tym kwadracie istnieja inne polew ktore można wpisać to liczbe + dodatkowe miejsca pionowo juz sa zajete 
def ostatnie_pozostałe_wolne_pole_w_kwadracie_pionowo(plansza,liczba):
    for i in range(3):
        for j in range(3):
            if(czy_ustalone(plansza[i][j] == False)):
                if(i%3 == 0 and j%3 == 0):
                    # Jesli jest w górnej lewej kratce
                    if(
                        czy_ustalone(plansza,i+1,j) == True and
                        czy_ustalone(plansza,i+2,j) == True and

                        czy_istnieje_poziomo(plansza,liczba,j+1) == True and
                        czy_istnieje_poziomo(plansza,liczba,j+2) == True
                    ):
                        plansza[i][j] = liczba
                if(i%3 == 1 and j%3 == 0):
                # Jesli jest w środkowej lewej kratce
                    if(
                        czy_ustalone(plansza,i+1,j) == True and
                        czy_ustalone(plansza,i-1,j) == True and

                        czy_istnieje_poziomo(plansza,liczba,j+1) == True and
                        czy_istnieje_poziomo(plansza,liczba,j+2) == True
                    ):
                        plansza[i][j] = liczba
                if(i%3 == 2 and j%3 == 0):
                # Jesli jest w dolnej lewej kratce
                    if(
                        czy_ustalone(plansza,i-1,j) == True and
                        czy_ustalone(plansza,i-2,j) == True and

                        czy_istnieje_poziomo(plansza,liczba,j+1) == True and
                        czy_istnieje_poziomo(plansza,liczba,j+2) == True
                    ):
                        plansza[i][j] = liczba
                if(i%3 == 0 and j%3 == 1):
                # Jesli jest w górnej środkowej kratce
                    if(
                        czy_ustalone(plansza,i+1,j) == True and
                        czy_ustalone(plansza,i+2,j) == True and

                        czy_istnieje_poziomo(plansza,liczba,j+1) == True and
                        czy_istnieje_poziomo(plansza,liczba,j-1) == True
                    ):
                        plansza[i][j] = liczba
                if(i%3 == 1 and j%3 == 1):
                # Jesli jest na środku
                    if(
                        czy_ustalone(plansza,i+1,j) == True and
                        czy_ustalone(plansza,i-1,j) == True and

                        czy_istnieje_poziomo(plansza,liczba,j+1) == True and
                        czy_istnieje_poziomo(plansza,liczba,j-1) == True
                    ):
                        plansza[i][j] = liczba
                if(i%3 == 2 and j%3 == 1):
                # Jesli jest w donej środkowej kratce
                    if(
                        czy_ustalone(plansza,i-1,j) == True and
                        czy_ustalone(plansza,i-2,j) == True and

                        czy_istnieje_poziomo(plansza,liczba,j+1) == True and
                        czy_istnieje_poziomo(plansza,liczba,j-1) == True
                    ):
                        plansza[i][j] = liczba
                if(i%3 == 0 and j%3 == 2):
                # Jesli jest w górnej prawej kratce
                    if(
                        czy_ustalone(plansza,i+1,j) == True and
                        czy_ustalone(plansza,i+2,j) == True and

                        czy_istnieje_poziomo(plansza,liczba,j-1) == True and
                        czy_istnieje_poziomo(plansza,liczba,j-2) == True
                    ):
                        plansza[i][j] = liczba
                if(i%3 == 1 and j%3 == 2):
                # Jesli jest w środkowej prawej kratce
                    if(
                        czy_ustalone(plansza,i+1,j) == True and
                        czy_ustalone(plansza,i-1,j) == True and

                        czy_istnieje_poziomo(plansza,liczba,j-1) == True and
                        czy_istnieje_poziomo(plansza,liczba,j-2) == True
                    ):
                        plansza[i][j] = liczba
                if(i%3 == 2 and j%3 == 2):
                # Jesli jest w dolnej praw kratce
                    if(
                        czy_ustalone(plansza,i-1,j) == True and
                        czy_ustalone(plansza,i-2,j) == True and

                        czy_istnieje_poziomo(plansza,liczba,j-1) == True and
                        czy_istnieje_poziomo(plansza,liczba,j-2) == True
                    ):
                        plansza[i][j] = liczba


#-------------------------------------------------------------------------------------
#Funkcje podstawowe do wariantów
def w_wariantach_czy_istnieje_poziomo(plansza,liczba,nr_rzedu):
    for i in range(9):
        for item in plansza[i][nr_rzedu]:
            if (item == liczba): return True
    return False

def w_wariantach_czy_istnieje_pionowo(plansza,liczba,nr_rzedu):
    for j in range(9):
        for item in plansza[nr_rzedu][j]:
            if (item == liczba): return True
    return False

def usun_liczbe_z_wariantów(operacja,plansza,liczba,i,j,nie_usuwac):
    
    # usun dana liczbe w pozostałych miejscach w kwadracie
    if(operacja == 1):
        if(i%3 == 0 and j%3 == 0):
            # Jesli jest w górnej lewej kratce
            for a in range(i,i+3): 
                for b in range(j,j+3):
                    if(type(plansza[a][b]) is tuple and plansza[a][b] != nie_usuwac):
                        try:
                            temp = list(plansza[a][b])
                            temp.remove(liczba)
                            plansza[a][b] = tuple(temp)
                        except BaseException:
                            continue
        if(i%3 == 1 and j%3 == 0):
            # Jesli jest w środkowej lewej kratce
            temp = 0
            for a in range(i-1,i+2): 
                for b in range(j,j+3):
                    if(type(plansza[a][b]) is tuple and plansza[a][b] != nie_usuwac):
                        try:
                            temp = list(plansza[a][b])
                            temp.remove(liczba)
                            plansza[a][b] = tuple(temp)
                        except BaseException:
                            continue
        if(i%3 == 2 and j%3 == 0):
        # Jesli jest w dolnej lewej kratce
            temp = 0
            for a in range(i-2,i+1): 
                for b in range(j,j+3):
                    if(type(plansza)[a][b] is tuple and plansza[a][b] != nie_usuwac):
                        try:
                            temp = list(plansza[a][b])
                            temp.remove(liczba)
                            plansza[a][b] = tuple(temp)
                        except BaseException:
                            continue
        if(i%3 == 0 and j%3 == 1):
        # Jesli jest w górnej środkowej kratce
            temp = 0
            for a in range(i,i+3): 
                for b in range(j-1,j+2):
                    if(type(plansza[a][b]) is tuple and plansza[a][b] != nie_usuwac):
                        try:
                            temp = list(plansza[a][b])
                            temp.remove(liczba)
                            plansza[a][b] = tuple(temp)
                        except BaseException:
                            continue
        if(i%3 == 1 and j%3 == 1):
        # Jesli jest na środku
            temp = 0
            for a in range(i-1,i+2): 
                for b in range(j-1,j+2):
                    if(type(plansza[a][b]) is tuple and plansza[a][b] != nie_usuwac):
                        try:
                            temp = list(plansza[a][b])
                            temp.remove(liczba)
                            plansza[a][b] = tuple(temp)
                        except BaseException:
                            continue
        if(i%3 == 2 and j%3 == 1):
        # Jesli jest w donej środkowej kratce
            temp = 0
            for a in range(i-2,i+1): 
                for b in range(j-1,j+2):
                    if(type(plansza[a][b]) is tuple and plansza[a][b] != nie_usuwac):
                        try:
                            temp = list(plansza[a][b])
                            temp.remove(liczba)
                            plansza[a][b] = tuple(temp)
                        except BaseException:
                            continue
        if(i%3 == 0 and j%3 == 2):
        # Jesli jest w górnej prawej kratce
            temp = 0
            for a in range(i,i+3): 
                for b in range(j-2,j+1):
                    if(type(plansza[a][b]) is tuple and plansza[a][b] != nie_usuwac):
                        try:
                            temp = list(plansza[a][b])
                            temp.remove(liczba)
                            plansza[a][b] = tuple(temp)
                        except BaseException:
                            continue
        if(i%3 == 1 and j%3 == 2):
        # Jesli jest w środkowej prawej kratce
            temp = 0
            for a in range(i-1,i+2): 
                for b in range(j-2,j+1):
                    if(type(plansza[a][b]) is tuple and plansza[a][b] != nie_usuwac):
                        try:
                            temp = list(plansza[a][b])
                            temp.remove(liczba)
                            plansza[a][b] = tuple(temp)
                        except BaseException:
                            continue
        if(i%3 == 2 and j%3 == 2):
        # Jesli jest w dolnej praw kratce
            temp = 0
            for a in range(i-2,i+1): 
                for b in range(j-2,j+1):
                    if(type(plansza[a][b]) is tuple and plansza[a][b] != nie_usuwac):
                        try:
                            temp = list(plansza[a][b])
                            temp.remove(liczba)
                            plansza[a][b] = tuple(temp)
                        except BaseException:
                            continue
    
    # usun liczbe w kolmnie i
    if(operacja == 2):
        if(w_wariantach_czy_istnieje_poziomo(plansza,liczba,i) == True):
            for b in range(9):
                if(type(plansza[i][b]) is tuple):
                        try:
                            temp = list(plansza[i][b])
                            temp.remove(liczba)
                            plansza[i][b] = tuple(temp)
                        except BaseException:
                            continue
    
    # usun liczbe w rzedzie j
    if(operacja == 3):
        if(w_wariantach_czy_istnieje_pionowo(plansza,liczba,j) == True):
            for a in range(9):
                if(type(plansza[i][b]) is tuple):
                        try:
                            temp = list(plansza[i][b])
                            temp.remove(liczba)
                            plansza[i][b] = tuple(temp)
                        except BaseException:
                            continue
    
    # usuń na konkretnym  miejscu
    if(operacja == 4):
        if(type(plansza[i][j]) is tuple):
            try:
                temp = list(plansza[i][j])
                temp.remove(liczba)
                plansza[i][b] = tuple(temp)
            except BaseException:
                return


def zmien_typ_planszy(plansza):
    temp_plansza = [[0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0],]
    for i in range(9):
        for j in range(9):
            temp_plansza[i][j] = int(plansza[i][j])
    return temp_plansza

def przelozenie_wynikow(tem_plansza,plansza):
    for i in range(9):
        for j in range(9):
            if(isinstance(tem_plansza[i][j],int)): plansza[i][j] = tem_plansza[i][j]

def porownanie_tablic(tab1,tab2):
    for i in range(9):
        for j in range(9):
            if(tab1[i][j] != tab2[i][j]): return False
    return True

#--------------------------------------------------------------------------------------
# Możliwe warianty

# Do każdego pola przypiujemy możliwe liczby
def warianty(plansza,liczba):
      #print(liczba)
      for i in range(9):
            # Dla każdego miejsca w rzedzie
            #print(i)
            if(czy_istnieje_pionowo(plansza,liczba,i) == False):
                # Jeżeli liczba nie występuje w danym rzedzie
                for j in range(9):
                    # Sprawdzamy po kolmnach
                    if(czy_ustalone(plansza,i,j) == False): 
                        #print("tyu")
                    #Jeżeli na danym polu nie ma konkretnej liczby
                        if(czy_istnieje_poziomo(plansza,liczba,j) == False):
                            if(i%3 == 0 and j%3 == 0):
                                temp = 0
                                # Jesli jest w górnej lewej kratce
                                for a in range(i,i+3): 
                                    for b in range(j,j+3):
                                        if(plansza[a][b] == liczba and isinstance(plansza[a][b], numbers.Number)): temp+=1
                                if(czy_istnieje_pionowo(plansza,liczba,i)):temp+=1
                                if(czy_istnieje_poziomo(plansza,liczba,j)):temp+=1
                                
                            if(i%3 == 1 and j%3 == 0):
                                # Jesli jest w środkowej lewej kratce
                                temp = 0
                                for a in range(i-1,i+2): 
                                    for b in range(j,j+3):
                                        if(plansza[a][b] == liczba and isinstance(plansza[a][b], numbers.Number)): temp+=1
                                if(czy_istnieje_pionowo(plansza,liczba,i)):temp+=1
                                if(czy_istnieje_poziomo(plansza,liczba,j)):temp+=1
                                
                            if(i%3 == 2 and j%3 == 0):
                            # Jesli jest w dolnej lewej kratce
                                temp = 0
                                for a in range(i-2,i+1): 
                                    for b in range(j,j+3):
                                        if(plansza[a][b] == liczba and isinstance(plansza[a][b], numbers.Number)): temp+=1
                                if(czy_istnieje_pionowo(plansza,liczba,i)):temp+=1
                                if(czy_istnieje_poziomo(plansza,liczba,j)):temp+=1
                                
                            if(i%3 == 0 and j%3 == 1):
                            # Jesli jest w górnej środkowej kratce
                                temp = 0
                                for a in range(i,i+3): 
                                    for b in range(j-1,j+2):
                                        if(plansza[a][b] == liczba and isinstance(plansza[a][b], numbers.Number)): temp+=1
                                if(czy_istnieje_pionowo(plansza,liczba,i)):temp+=1
                                if(czy_istnieje_poziomo(plansza,liczba,j)):temp+=1
                                
                            if(i%3 == 1 and j%3 == 1):
                            # Jesli jest na środku
                                temp = 0
                                for a in range(i-1,i+2): 
                                    for b in range(j-1,j+2):
                                        if(plansza[a][b] == liczba and isinstance(plansza[a][b], numbers.Number)): temp+=1
                                if(czy_istnieje_pionowo(plansza,liczba,i)):temp+=1
                                if(czy_istnieje_poziomo(plansza,liczba,j)):temp+=1

                            if(i%3 == 2 and j%3 == 1):
                            # Jesli jest w donej środkowej kratce
                                temp = 0
                                for a in range(i-2,i+1): 
                                    for b in range(j-1,j+2):
                                        if(plansza[a][b] == liczba and isinstance(plansza[a][b], numbers.Number)): temp+=1
                                if(czy_istnieje_pionowo(plansza,liczba,i)):temp+=1
                                if(czy_istnieje_poziomo(plansza,liczba,j)):temp+=1
                                
                            if(i%3 == 0 and j%3 == 2):
                            # Jesli jest w górnej prawej kratce
                                temp = 0
                                for a in range(i,i+3): 
                                    for b in range(j-2,j+1):
                                        if(plansza[a][b] == liczba and isinstance(plansza[a][b], numbers.Number)): temp+=1
                                if(czy_istnieje_pionowo(plansza,liczba,i)):temp+=1
                                if(czy_istnieje_poziomo(plansza,liczba,j)):temp+=1
                                
                            if(i%3 == 1 and j%3 == 2):
                            # Jesli jest w środkowej prawej kratce
                                temp = 0
                                for a in range(i-1,i+2): 
                                    for b in range(j-2,j+1):
                                        if(plansza[a][b] == liczba and isinstance(plansza[a][b], numbers.Number)): temp+=1
                                if(czy_istnieje_pionowo(plansza,liczba,i)):temp+=1
                                if(czy_istnieje_poziomo(plansza,liczba,j)):temp+=1
                                
                            if(i%3 == 2 and j%3 == 2):
                            # Jesli jest w dolnej praw kratce
                                temp = 0
                                for a in range(i-2,i+1): 
                                    for b in range(j-2,j+1):
                                        if(plansza[a][b] == liczba and isinstance(plansza[a][b], numbers.Number)): temp+=1
                                if(czy_istnieje_pionowo(plansza,liczba,i)):temp+=1
                                if(czy_istnieje_poziomo(plansza,liczba,j)):temp+=1
                            
                            if(temp == 0):
                                #print(plansza[i][j])
                                if(isinstance(plansza[i][j], tuple)): plansza[i][j] += (liczba,)
                                elif(plansza[i][j] == 0): plansza[i][j] = (liczba,)
                                else :plansza[i][j]=(plansza[i][j],)+(liczba,)
                                #print(plansza[i][j])
                            #if(liczba == 4 and temp == 0): print(plansza[i][j],i,j)

# Jezeli w danym kwadracie jest tylko w jednym miejscu przewidywana dana liczba        
def jedyne_miejsce_w_kwadracie(plansza):
    for i in range(9):
            # Dla każdego miejsca w rzedzie
            for j in range(9):
                # Sprawdzamy po kolmnach
                
                #--------------------------------------------------------------
                if(plansza[i][j] is tuple and len(plansza[i][j]) == 1): 
                    plansza[i][j] = int(plansza[i][j])
                    continue
                #--------------------------------------------------------------
                if(czy_ustalone(plansza,i,j) == False and isinstance(plansza[i][j],tuple)):
                #Jeżeli na danym polu nie ma konkretnej liczby
                    
                    #print("asdsad")
                    if(i%3 == 0 and j%3 == 0):
                        # Jesli jest w górnej lewej kratce
                        temp = 0
                        for konkretny_item in plansza[i][j]:
                            for a in range(i,i+3): 
                                for b in range(j,j+3):
                                    if(isinstance(plansza[a][b],tuple)):
                                        for item in plansza[a][b]:
                                            if(item == konkretny_item): temp+=1
                                    
                                                            
                    if(i%3 == 1 and j%3 == 0):
                        # Jesli jest w środkowej lewej kratce
                        for konkretny_item in plansza[i][j]:
                            temp = 0
                            for a in range(i-1,i+2): 
                                for b in range(j,j+3):
                                    if(isinstance(plansza[a][b],tuple)):
                                        for item in plansza[a][b]:
                                            if(item == konkretny_item): temp+=1
                                    

                    if(i%3 == 2 and j%3 == 0):
                    # Jesli jest w dolnej lewej kratce
                        for konkretny_item in plansza[i][j]:
                            temp = 0
                            for a in range(i-2,i+1): 
                                for b in range(j,j+3):
                                      if(isinstance(plansza[a][b],tuple)):
                                        for item in plansza[a][b]:
                                            if(item == konkretny_item): temp+=1
                            

                    if(i%3 == 0 and j%3 == 1):
                    # Jesli jest w górnej środkowej kratce
                        for konkretny_item in plansza[i][j]:                       
                            temp = 0
                            for a in range(i,i+3): 
                                for b in range(j-1,j+2):
                                    if(isinstance(plansza[a][b],tuple)):
                                        for item in plansza[a][b]:
                                            if(item == konkretny_item): temp+=1

                    if(i%3 == 1 and j%3 == 1):
                    # Jesli jest na środku
                        for konkretny_item in plansza[i][j]:
                            temp = 0
                            for a in range(i-1,i+2): 
                                for b in range(j-1,j+2):
                                     if(isinstance(plansza[a][b],tuple)):
                                        for item in plansza[a][b]:
                                            if(item == konkretny_item): temp+=1
                            

                    if(i%3 == 2 and j%3 == 1):
                    # Jesli jest w donej środkowej kratce
                        for konkretny_item in plansza[i][j]:
                            temp = 0
                            for a in range(i-2,i+1): 
                                for b in range(j-1,j+2):
                                      if(isinstance(plansza[a][b],tuple)):
                                        for item in plansza[a][b]:
                                            if(item == konkretny_item): temp+=1
                            

                    if(i%3 == 0 and j%3 == 2):
                    # Jesli jest w górnej prawej kratce
                        for konkretny_item in plansza[i][j]:
                            temp = 0
                            for a in range(i,i+3): 
                                for b in range(j-2,j+1):
                                     if(isinstance(plansza[a][b],tuple)):
                                        for item in plansza[a][b]:
                                            if(item == konkretny_item): temp+=1
                            

                    if(i%3 == 1 and j%3 == 2):
                    # Jesli jest w środkowej prawej kratce
                        for konkretny_item in plansza[i][j]:
                            temp = 0
                            for a in range(i-1,i+2): 
                                for b in range(j-2,j+1):
                                     if(isinstance(plansza[a][b],tuple)):
                                        for item in plansza[a][b]:
                                            if(item == konkretny_item): temp+=1
                            

                    if(i%3 == 2 and j%3 == 2):
                    # Jesli jest w dolnej praw kratce
                        for konkretny_item in plansza[i][j]:
                            temp = 0
                            for a in range(i-2,i+1): 
                                for b in range(j-2,j+1):
                                      if(isinstance(plansza[a][b],tuple)):
                                        for item in plansza[a][b]:
                                            if(item == konkretny_item): temp+=1
                            
                    if(temp==1): plansza[i][j] = konkretny_item
                                
# Jeżeli tylko w jednymiejscu pionowo lub poziomo przewidujemy ze bedzie liczba
def jedyne_pole_poziomo_lub_pionowo(plansza):
    for i in range(9):
        # Dla każdego miejsca w rzedzie
        for j in range(9):
            # Sprawdzamy po kolmnach
                            #--------------------------------------------------------------
                if(isinstance(plansza[i][j],tuple) and len(plansza[i][j]) == 1): plansza[i][j] = int(plansza[i][j][0])
                #--------------------------------------------------------------

                # if(czy_ustalone(plansza,i,j) == False):
                # #Jeżeli na danym polu nie ma konkretnej liczby

                #     for item in plansza[i][j]:
                #         if(w_wariantach_czy_istnieje_poziomo(plansza,item,j) and w_wariantach_czy_istnieje_pionowo(plansza,item,i)):
                #             plansza[i][j] = item
                #             break
                #         # Trzeba to przejzec TODO

# Nie da sie tego łatwo wytłumaczyc
def oczywite_dwojki_trojki(plansza):
    for i in range(9):
        # Dla każdego miejsca w rzedzie
        for j in range(9):
            # Sprawdzamy po kolmnach
            if(isinstance(plansza[i][j], tuple)):
                dana_para = plansza[i][j]
                wystapienia_w_kwadracie = [0 for i in range(10)]
                try:
                    if(i%3 == 0 and j%3 == 0):
                    # Jesli jest w górnej lewej kratce
                        temp = 0 # ilosc takich samych krotek
                        for a in range(i,i+3): 
                            for b in range(j,j+3):
                                if(plansza[a][b] == dana_para): temp+= 1
                                if(isinstance(plansza[a][b],numbers.Number) == False):
                                    for item in plansza[a][b]:
                                        wystapienia_w_kwadracie[item] += 1
                        #-------------------------------------------------------------
                        # Pary z takimi samymi liczbami
                        if (temp == 2 and len(dana_para[i][j]) == 2):
                            # sa 2 miejsca takie same w kratce
                            for item in dana_para:
                                usun_liczbe_z_wariantów(1,plansza,item,i,j,dana_para)
                        if (temp == 3 and len(dana_para[i][j]) == 3):
                            # sa 3 miejsca takie same w kratce
                            for item in dana_para:
                                usun_liczbe_z_wariantów(1,plansza,item,i,j,dana_para)
                        if (temp == 4 and len(dana_para[i][j]) == 4):
                            # sa 4 miejsca takie same w kratce
                            for item in dana_para:
                                usun_liczbe_z_wariantów(1,plansza,item,i,j,dana_para)
                        if (temp == 5 and len(dana_para[i][j]) == 5):
                            # jest 5 takich miejsc w kratce
                            for item in dana_para:
                                usun_liczbe_z_wariantów(1,plansza,item,i,j,dana_para)
                        #-------------------------------------------------------------
                        # Pary nie talkie same
                        # oczywiste trojki
                        podejrzane_liczby = []
                        for liczba in range(10):
                            if(wystapienia_w_kwadracie[liczba]>=3): podejrzane_liczby.append(liczba)
                        # sprawdzamy ktore liczby wystepuja przynajmniej 3 razy w kratce
                        temp_3 = [] #ilosc komórek git jak jest 3
                        for a in range(i,i+3): 
                            for b in range(j,j+3):
                                if(isinstance(plansza[a][b],tuple)):
                                    if(len(plansza[a][b]) == 2 and plansza[a][b][1] in podejrzane_liczby and plansza[a][b][2] in podejrzane_liczby): temp_3.append((a,b))
                        if(len(temp_3) == 3):
                        # Jeżeli znaleźliśmy takie 3 komorki co maja po 2 liczby i one wystepuja po 2 razy
                            sprawdzenie = () # TODO czy napewnpo
                            for item in temp_3:
                                for d_item in item:
                                    sprawdzenie += plansza[item[0]][item[1]][d_item] 
                            for item in sprawdzenie:
                                if(sprawdzenie.count(item) != 2):
                                # Jeżli jakiś elemnet nie wystepuje 2 razy
                                    return
                            # znalezienie tych liczb w innych komorkach
                            sprawdzenie = set(sprawdzenie)
                            # zbiór liczb
                            for item in sprawdzenie:
                                for a in range(i,i+3): 
                                    for b in range(j,j+3):
                                        if((a,b) in temp_3):continue
                                        usun_liczbe_z_wariantów(4,plansza,item,a,b)
                    

                    if(i%3 == 1 and j%3 == 0):
                        # Jesli jest w środkowej lewej kratce
                        temp = 0 # ilosc takich samych krotek
                        # wystapienia_w_kwadracie = [range(10)]
                        for a in range(i-1,i+2): 
                            for b in range(j,j+3):
                                if(plansza[a][b] == dana_para): temp+= 1
                                if(isinstance(plansza[a][b],numbers.Number) == False):
                                    for item in plansza[a][b]:
                                        wystapienia_w_kwadracie[item] += 1
                        #-------------------------------------------------------------
                        # Pary z takimi samymi liczbami
                        if (temp == 2 and len(dana_para[i][j]) == 2):
                            # sa 2 miejsca takie same w kratce
                            for item in dana_para:
                                usun_liczbe_z_wariantów(1,plansza,item,i,j,dana_para)
                        if (temp == 3 and len(dana_para[i][j]) == 3):
                            # sa 3 miejsca takie same w kratce
                            for item in dana_para:
                                usun_liczbe_z_wariantów(1,plansza,item,i,j,dana_para)
                        if (temp == 4 and len(dana_para[i][j]) == 4):
                            # sa 4 miejsca takie same w kratce
                            for item in dana_para:
                                usun_liczbe_z_wariantów(1,plansza,item,i,j,dana_para)
                        if (temp == 5 and len(dana_para[i][j]) == 5):
                            # jest 5 takich miejsc w kratce
                            for item in dana_para:
                                usun_liczbe_z_wariantów(1,plansza,item,i,j,dana_para)
                        #-------------------------------------------------------------
                        # Pary nie talkie same
                        # oczywiste trojki
                        podejrzane_liczby = []
                        for liczba in range(10):
                            if(wystapienia_w_kwadracie[liczba]>=3): podejrzane_liczby.append(liczba)
                        # sprawdzamy ktore liczby wystepuja przynajmniej 3 razy w kratce
                        temp_3 = [] #ilosc komórek git jak jest 3
                        for a in range(i-1,i+2): 
                            for b in range(j,j+3):
                                if(isinstance(plansza[a][b],tuple)):
                                    if(len(plansza[a][b]) == 2 and plansza[a][b][1] in podejrzane_liczby and plansza[a][b][2] in podejrzane_liczby): temp_3.append((a,b))
                        if(len(temp_3) == 3):
                        # Jeżeli znaleźliśmy takie 3 komorki co maja po 2 liczby i one wystepuja po 2 razy
                            sprawdzenie = () # TODO czy napewnpo
                            for item in temp_3:
                                for d_item in item:
                                    sprawdzenie += plansza[item[0]][item[1]][d_item] 
                            for item in sprawdzenie:
                                if(sprawdzenie.count(item) != 2):
                                # Jeżli jakiś elemnet nie wystepuje 2 razy
                                    return
                            # znalezienie tych liczb w innych komorkach
                            sprawdzenie = set(sprawdzenie)
                            # zbiór liczb
                            for item in sprawdzenie:
                                for a in range(i-1,i+2): 
                                    for b in range(j,j+3):
                                        if((a,b) in temp_3):continue
                                        usun_liczbe_z_wariantów(4,plansza,item,a,b)
                        
                    if(i%3 == 2 and j%3 == 0):
                    # Jesli jest w dolnej lewej kratce
                        temp = 0 # ilosc takich samych krotek
                        # wystapienia_w_kwadracie = [range(10)]
                        for a in range(i-2,i+1): 
                            for b in range(j,j+3):
                                if(plansza[a][b] == dana_para): temp+= 1
                                for item in plansza[a][b]:
                                    wystapienia_w_kwadracie[item] += 1
                        #-------------------------------------------------------------
                        # Pary z takimi samymi liczbami
                        if (temp == 2 and len(dana_para[i][j]) == 2):
                            # sa 2 miejsca takie same w kratce
                            for item in dana_para:
                                usun_liczbe_z_wariantów(1,plansza,item,i,j,dana_para)
                        if (temp == 3 and len(dana_para[i][j]) == 3):
                            # sa 3 miejsca takie same w kratce
                            for item in dana_para:
                                usun_liczbe_z_wariantów(1,plansza,item,i,j,dana_para)
                        if (temp == 4 and len(dana_para[i][j]) == 4):
                            # sa 4 miejsca takie same w kratce
                            for item in dana_para:
                                usun_liczbe_z_wariantów(1,plansza,item,i,j,dana_para)
                        if (temp == 5 and len(dana_para[i][j]) == 5):
                            # jest 5 takich miejsc w kratce
                            for item in dana_para:
                                usun_liczbe_z_wariantów(1,plansza,item,i,j,dana_para)
                        #-------------------------------------------------------------
                        # Pary nie talkie same
                        # oczywiste trojki
                        podejrzane_liczby = []
                        for liczba in range(10):
                            if(wystapienia_w_kwadracie[liczba]>=3): podejrzane_liczby.append(liczba)
                        # sprawdzamy ktore liczby wystepuja przynajmniej 3 razy w kratce
                        temp_3 = [] #ilosc komórek git jak jest 3
                        for a in range(i-2,i+1): 
                            for b in range(j,j+3):
                                if(isinstance(plansza[a][b],tuple)):
                                    if(len(plansza[a][b]) == 2 and plansza[a][b][1] in podejrzane_liczby and plansza[a][b][2] in podejrzane_liczby): temp_3.append((a,b))
                        if(len(temp_3) == 3):
                        # Jeżeli znaleźliśmy takie 3 komorki co maja po 2 liczby i one wystepuja po 2 razy
                            sprawdzenie = () # TODO czy napewnpo
                            for item in temp_3:
                                for d_item in item:
                                    sprawdzenie += plansza[item[0]][item[1]][d_item] 
                            for item in sprawdzenie:
                                if(sprawdzenie.count(item) != 2):
                                # Jeżli jakiś elemnet nie wystepuje 2 razy
                                    return
                            # znalezienie tych liczb w innych komorkach
                            sprawdzenie = set(sprawdzenie)
                            # zbiór liczb
                            for item in sprawdzenie:
                                for a in range(i-2,i+1): 
                                    for b in range(j,j+3):
                                        if((a,b) in temp_3):continue
                                        usun_liczbe_z_wariantów(4,plansza,item,a,b)


                    if(i%3 == 0 and j%3 == 1):
                    # Jesli jest w górnej środkowej kratce
                        temp = 0 # ilosc takich samych krotek
                        # wystapienia_w_kwadracie = [range(10)]
                        for a in range(i,i+3): 
                            for b in range(j-1,j+2):
                                if(plansza[a][b] == dana_para): temp+= 1
                                if(isinstance(plansza[a][b],numbers.Number) == False):
                                    for item in plansza[a][b]:
                                        wystapienia_w_kwadracie[item] += 1
                        #-------------------------------------------------------------
                        # Pary z takimi samymi liczbami
                        if (temp == 2 and len(dana_para[i][j]) == 2):
                            # sa 2 miejsca takie same w kratce
                            for item in dana_para:
                                usun_liczbe_z_wariantów(1,plansza,item,i,j,dana_para)
                        if (temp == 3 and len(dana_para[i][j]) == 3):
                            # sa 3 miejsca takie same w kratce
                            for item in dana_para:
                                usun_liczbe_z_wariantów(1,plansza,item,i,j,dana_para)
                        if (temp == 4 and len(dana_para[i][j]) == 4):
                            # sa 4 miejsca takie same w kratce
                            for item in dana_para:
                                usun_liczbe_z_wariantów(1,plansza,item,i,j,dana_para)
                        if (temp == 5 and len(dana_para[i][j]) == 5):
                            # jest 5 takich miejsc w kratce
                            for item in dana_para:
                                usun_liczbe_z_wariantów(1,plansza,item,i,j,dana_para)
                        #-------------------------------------------------------------
                        # Pary nie talkie same
                        # oczywiste trojki
                        podejrzane_liczby = []
                        for liczba in range(10):
                            if(wystapienia_w_kwadracie[liczba]>=3): podejrzane_liczby.append(liczba)
                        # sprawdzamy ktore liczby wystepuja przynajmniej 3 razy w kratce
                        temp_3 = [] #ilosc komórek git jak jest 3
                        for a in range(i,i+3): 
                            for b in range(j-1,j+2):
                                if(isinstance(plansza[a][b],tuple)):
                                    if(len(plansza[a][b]) == 2 and plansza[a][b][1] in podejrzane_liczby and plansza[a][b][2] in podejrzane_liczby): temp_3.append((a,b))
                        if(len(temp_3) == 3):
                        # Jeżeli znaleźliśmy takie 3 komorki co maja po 2 liczby i one wystepuja po 2 razy
                            sprawdzenie = () # TODO czy napewnpo
                            for item in temp_3:
                                for d_item in item:
                                    sprawdzenie += plansza[item[0]][item[1]][d_item] 
                            for item in sprawdzenie:
                                if(sprawdzenie.count(item) != 2):
                                # Jeżli jakiś elemnet nie wystepuje 2 razy
                                    return
                            # znalezienie tych liczb w innych komorkach
                            sprawdzenie = set(sprawdzenie)
                            # zbiór liczb
                            for item in sprawdzenie:
                                for a in range(i,i+3): 
                                    for b in range(j-1,j+2):
                                        if((a,b) in temp_3):continue
                                        usun_liczbe_z_wariantów(4,plansza,item,a,b)
                        

                    if(i%3 == 1 and j%3 == 1):
                    # Jesli jest na środku
                        temp = 0 # ilosc takich samych krotek
                        # wystapienia_w_kwadracie = [range(10)]
                        for a in range(i-1,i+2): 
                            for b in range(j-1,j+2):
                                if(plansza[a][b] == dana_para): temp+= 1
                                if(isinstance(plansza[a][b],numbers.Number) == False):
                                    for item in plansza[a][b]:
                                        wystapienia_w_kwadracie[item] += 1
                        #-------------------------------------------------------------
                        # Pary z takimi samymi liczbami
                        if (temp == 2 and len(dana_para[i][j]) == 2):
                            # sa 2 miejsca takie same w kratce
                            for item in dana_para:
                                usun_liczbe_z_wariantów(1,plansza,item,i,j,dana_para)
                        if (temp == 3 and len(dana_para[i][j]) == 3):
                            # sa 3 miejsca takie same w kratce
                            for item in dana_para:
                                usun_liczbe_z_wariantów(1,plansza,item,i,j,dana_para)
                        if (temp == 4 and len(dana_para[i][j]) == 4):
                            # sa 4 miejsca takie same w kratce
                            for item in dana_para:
                                usun_liczbe_z_wariantów(1,plansza,item,i,j,dana_para)
                        if (temp == 5 and len(dana_para[i][j]) == 5):
                            # jest 5 takich miejsc w kratce
                            for item in dana_para:
                                usun_liczbe_z_wariantów(1,plansza,item,i,j,dana_para)
                        #-------------------------------------------------------------
                        # Pary nie talkie same
                        # oczywiste trojki
                        podejrzane_liczby = []
                        for liczba in range(10):
                            if(wystapienia_w_kwadracie[liczba]>=3): podejrzane_liczby.append(liczba)
                        # sprawdzamy ktore liczby wystepuja przynajmniej 3 razy w kratce
                        temp_3 = [] #ilosc komórek git jak jest 3
                        for a in range(i-1,i+2): 
                            for b in range(j-1,j+2):
                                if(isinstance(plansza[a][b],tuple)):
                                    if(len(plansza[a][b]) == 2 and plansza[a][b][1] in podejrzane_liczby and plansza[a][b][2] in podejrzane_liczby): temp_3.append((a,b))
                        if(len(temp_3) == 3):
                        # Jeżeli znaleźliśmy takie 3 komorki co maja po 2 liczby i one wystepuja po 2 razy
                            sprawdzenie = () # TODO czy napewnpo
                            for item in temp_3:
                                for d_item in item:
                                    sprawdzenie += plansza[item[0]][item[1]][d_item] 
                            for item in sprawdzenie:
                                if(sprawdzenie.count(item) != 2):
                                # Jeżli jakiś elemnet nie wystepuje 2 razy
                                    return
                            # znalezienie tych liczb w innych komorkach
                            sprawdzenie = set(sprawdzenie)
                            # zbiór liczb
                            for item in sprawdzenie:
                                for a in range(i-1,i+2): 
                                    for b in range(j-1,j+2):
                                        if((a,b) in temp_3):continue
                                        usun_liczbe_z_wariantów(4,plansza,item,a,b)
                        

                    if(i%3 == 2 and j%3 == 1):
                    # Jesli jest w donej środkowej kratce
                        temp = 0 # ilosc takich samych krotek
                        # wystapienia_w_kwadracie = [range(10)]
                        for a in range(i-2,i+1): 
                            for b in range(j-1,j+2):
                                if(plansza[a][b] == dana_para): temp+= 1
                                if(isinstance(plansza[a][b],numbers.Number) == False):
                                    for item in plansza[a][b]:
                                        wystapienia_w_kwadracie[item] += 1
                        #-------------------------------------------------------------
                        # Pary z takimi samymi liczbami
                        if (temp == 2 and len(dana_para[i][j]) == 2):
                            # sa 2 miejsca takie same w kratce
                            for item in dana_para:
                                usun_liczbe_z_wariantów(1,plansza,item,i,j,dana_para)
                        if (temp == 3 and len(dana_para[i][j]) == 3):
                            # sa 3 miejsca takie same w kratce
                            for item in dana_para:
                                usun_liczbe_z_wariantów(1,plansza,item,i,j,dana_para)
                        if (temp == 4 and len(dana_para[i][j]) == 4):
                            # sa 4 miejsca takie same w kratce
                            for item in dana_para:
                                usun_liczbe_z_wariantów(1,plansza,item,i,j,dana_para)
                        if (temp == 5 and len(dana_para[i][j]) == 5):
                            # jest 5 takich miejsc w kratce
                            for item in dana_para:
                                usun_liczbe_z_wariantów(1,plansza,item,i,j,dana_para)
                        #-------------------------------------------------------------
                        # Pary nie talkie same
                        # oczywiste trojki
                        podejrzane_liczby = []
                        for liczba in range(10):
                            if(wystapienia_w_kwadracie[liczba]>=3): podejrzane_liczby.append(liczba)
                        # sprawdzamy ktore liczby wystepuja przynajmniej 3 razy w kratce
                        temp_3 = [] #ilosc komórek git jak jest 3
                        for a in range(i-2,i+1): 
                            for b in range(j-1,j+2):
                                if(isinstance(plansza[a][b],tuple)):
                                    if(len(plansza[a][b]) == 2 and plansza[a][b][1] in podejrzane_liczby and plansza[a][b][2] in podejrzane_liczby): temp_3.append((a,b))
                        if(len(temp_3) == 3):
                        # Jeżeli znaleźliśmy takie 3 komorki co maja po 2 liczby i one wystepuja po 2 razy
                            sprawdzenie = () # TODO czy napewnpo
                            for item in temp_3:
                                for d_item in item:
                                    sprawdzenie += plansza[item[0]][item[1]][d_item] 
                            for item in sprawdzenie:
                                if(sprawdzenie.count(item) != 2):
                                # Jeżli jakiś elemnet nie wystepuje 2 razy
                                    return
                            # znalezienie tych liczb w innych komorkach
                            sprawdzenie = set(sprawdzenie)
                            # zbiór liczb
                            for item in sprawdzenie:
                                for a in range(i-2,i+1): 
                                    for b in range(j-1,j+2):    
                                        if((a,b) in temp_3):continue
                                        usun_liczbe_z_wariantów(4,plansza,item,a,b)
                        

                    if(i%3 == 0 and j%3 == 2):
                    # Jesli jest w górnej prawej kratce
                        temp = 0 # ilosc takich samych krotek
                        for a in range(i,i+3): 
                            for b in range(j-2,j+1):
                                if(plansza[a][b] == dana_para): temp+= 1
                                if(isinstance(plansza[a][b],numbers.Number) == False):
                                    for item in plansza[a][b]:
                                        wystapienia_w_kwadracie[item] += 1
                        #-------------------------------------------------------------
                        # Pary z takimi samymi liczbami
                        if (temp == 2 and len(dana_para[i][j]) == 2):
                            # sa 2 miejsca takie same w kratce
                            for item in dana_para:
                                usun_liczbe_z_wariantów(1,plansza,item,i,j,dana_para)
                        if (temp == 3 and len(dana_para[i][j]) == 3):
                            # sa 3 miejsca takie same w kratce
                            for item in dana_para:
                                usun_liczbe_z_wariantów(1,plansza,item,i,j,dana_para)
                        if (temp == 4 and len(dana_para[i][j]) == 4):
                            # sa 4 miejsca takie same w kratce
                            for item in dana_para:
                                usun_liczbe_z_wariantów(1,plansza,item,i,j,dana_para)
                        if (temp == 5 and len(dana_para[i][j]) == 5):
                            # jest 5 takich miejsc w kratce
                            for item in dana_para:
                                usun_liczbe_z_wariantów(1,plansza,item,i,j,dana_para)
                        #-------------------------------------------------------------
                        # Pary nie talkie same
                        # oczywiste trojki
                        podejrzane_liczby = []
                        for liczba in range(10):
                            if(wystapienia_w_kwadracie[liczba]>=3): podejrzane_liczby.append(liczba)
                        # sprawdzamy ktore liczby wystepuja przynajmniej 3 razy w kratce
                        temp_3 = [] #ilosc komórek git jak jest 3
                        for a in range(i,i+3): 
                            for b in range(j-2,j+1):
                                if(isinstance(plansza[a][b],tuple)):
                                    if(len(plansza[a][b]) == 2 and plansza[a][b][1] in podejrzane_liczby and plansza[a][b][2] in podejrzane_liczby): temp_3.append((a,b))
                        if(len(temp_3) == 3):
                        # Jeżeli znaleźliśmy takie 3 komorki co maja po 2 liczby i one wystepuja po 2 razy
                            sprawdzenie = () # TODO czy napewnpo
                            for item in temp_3:
                                for d_item in item:
                                    sprawdzenie += plansza[item[0]][item[1]][d_item] 
                            for item in sprawdzenie:
                                if(sprawdzenie.count(item) != 2):
                                # Jeżli jakiś elemnet nie wystepuje 2 razy
                                    return
                            # znalezienie tych liczb w innych komorkach
                            sprawdzenie = set(sprawdzenie)
                            # zbiór liczb
                            for item in sprawdzenie:
                                for a in range(i,i+3): 
                                    for b in range(j-2,j+1):
                                        if((a,b) in temp_3):continue
                                        usun_liczbe_z_wariantów(4,plansza,item,a,b)
                        

                    if(i%3 == 1 and j%3 == 2):
                        #print(plansza[j][i])
                    # Jesli jest w środkowej prawej kratce
                        temp = 0 # ilosc takich samych krotek
                        # wystapienia_w_kwadracie = [range(10)]
                        for a in range(i-1,i+2): 
                            for b in range(j-2,j+1):
                                if(plansza[a][b] == dana_para): temp+= 1
                                if(isinstance(plansza[a][b],numbers.Number) == False):
                                    for item in plansza[a][b]:
                                        wystapienia_w_kwadracie[item] += 1
                        #-------------------------------------------------------------
                        # Pary z takimi samymi liczbami
                        #print(temp)
                        if (temp == 2 and len(dana_para[i][j]) == 2):
                            # sa 2 miejsca takie same w kratce
                            for item in dana_para:
                                usun_liczbe_z_wariantów(1,plansza,item,i,j,dana_para)
                        if (temp == 3 and len(dana_para[i][j]) == 3):
                            # sa 3 miejsca takie same w kratce
                            for item in dana_para:
                                usun_liczbe_z_wariantów(1,plansza,item,i,j,dana_para)
                        if (temp == 4 and len(dana_para[i][j]) == 4):
                            # sa 4 miejsca takie same w kratce
                            for item in dana_para:
                                usun_liczbe_z_wariantów(1,plansza,item,i,j,dana_para)
                        if (temp == 5 and len(dana_para[i][j]) == 5):
                            # jest 5 takich miejsc w kratce
                            for item in dana_para:
                                usun_liczbe_z_wariantów(1,plansza,item,i,j,dana_para)
                        #-------------------------------------------------------------
                        # Pary nie talkie same
                        # oczywiste trojki
                        podejrzane_liczby = []
                        for liczba in range(10):
                            if(wystapienia_w_kwadracie[liczba]>=3): podejrzane_liczby.append(liczba)
                        # sprawdzamy ktore liczby wystepuja przynajmniej 3 razy w kratce
                        temp_3 = [] #ilosc komórek git jak jest 3
                        for a in range(i-1,i+2): 
                            for b in range(j-2,j+1):
                                if(isinstance(plansza[a][b],tuple)):
                                    if(len(plansza[a][b]) == 2 and plansza[a][b][1] in podejrzane_liczby and plansza[a][b][2] in podejrzane_liczby): temp_3.append((a,b))
                        if(len(temp_3) == 3):
                        # Jeżeli znaleźliśmy takie 3 komorki co maja po 2 liczby i one wystepuja po 2 razy
                            sprawdzenie = () # TODO czy napewnpo
                            for item in temp_3:
                                for d_item in item:
                                    sprawdzenie += plansza[item[0]][item[1]][d_item] 
                            for item in sprawdzenie:
                                if(sprawdzenie.count(item) != 2):
                                # Jeżli jakiś elemnet nie wystepuje 2 razy
                                    return
                            # znalezienie tych liczb w innych komorkach
                            sprawdzenie = set(sprawdzenie)
                            # zbiór liczb
                            for item in sprawdzenie:
                                for a in range(i-1,i+2): 
                                    for b in range(j-2,j+1):
                                        if((a,b) in temp_3):continue
                                        usun_liczbe_z_wariantów(4,plansza,item,a,b)
                        

                    if(i%3 == 2 and j%3 == 2):
                    # Jesli jest w dolnej praw kratce
                        temp = 0 # ilosc takich samych krotek
                        # wystapienia_w_kwadracie = [range(10)]
                        for a in range(i-2,i+1): 
                            for b in range(j-2,j+1):
                                if(plansza[a][b] == dana_para): temp+= 1
                                if(isinstance(plansza[a][b],numbers.Number) == False):
                                    for item in plansza[a][b]:
                                        wystapienia_w_kwadracie[item] += 1
                        #-------------------------------------------------------------
                        # Pary z takimi samymi liczbami
                        if (temp == 2 and len(dana_para[i][j]) == 2):
                            # sa 2 miejsca takie same w kratce
                            for item in dana_para:
                                usun_liczbe_z_wariantów(1,plansza,item,i,j,dana_para)
                        if (temp == 3 and len(dana_para[i][j]) == 3):
                            # sa 3 miejsca takie same w kratce
                            for item in dana_para:
                                usun_liczbe_z_wariantów(1,plansza,item,i,j,dana_para)
                        if (temp == 4 and len(dana_para[i][j]) == 4):
                            # sa 4 miejsca takie same w kratce
                            for item in dana_para:
                                usun_liczbe_z_wariantów(1,plansza,item,i,j,dana_para)
                        if (temp == 5 and len(dana_para[i][j]) == 5):
                            # jest 5 takich miejsc w kratce
                            for item in dana_para:
                                usun_liczbe_z_wariantów(1,plansza,item,i,j,dana_para)
                        #-------------------------------------------------------------
                        # Pary nie talkie same
                        # oczywiste trojki
                        podejrzane_liczby = []
                        for liczba in range(10):
                            if(wystapienia_w_kwadracie[liczba]>=3): podejrzane_liczby.append(liczba)
                        # sprawdzamy ktore liczby wystepuja przynajmniej 3 razy w kratce
                        temp_3 = [] #ilosc komórek git jak jest 3
                        for a in range(i-2,i+1): 
                            for b in range(j-2,j+1):
                                if(isinstance(plansza[a][b],tuple)):
                                    if(len(plansza[a][b]) == 2 and plansza[a][b][1] in podejrzane_liczby and plansza[a][b][2] in podejrzane_liczby): temp_3.append((a,b))
                        if(len(temp_3) == 3):
                        # Jeżeli znaleźliśmy takie 3 komorki co maja po 2 liczby i one wystepuja po 2 razy
                            sprawdzenie = () # TODO czy napewnpo
                            for item in temp_3:
                                for d_item in item:
                                    sprawdzenie += plansza[item[0]][item[1]][d_item] 
                            for item in sprawdzenie:
                                if(sprawdzenie.count(item) != 2):
                                # Jeżli jakiś elemnet nie wystepuje 2 razy
                                    return
                            # znalezienie tych liczb w innych komorkach
                            sprawdzenie = set(sprawdzenie)
                            # zbiór liczb
                            for item in sprawdzenie:
                                for a in range(i-2,i+1): 
                                    for b in range(j-2,j+1):
                                        if((a,b) in temp_3):continue
                                        usun_liczbe_z_wariantów(4,plansza,item,a,b)
                    #if(temp != 1): print(temp)
                except BaseException:
                    #print("nie")
                    continue
#-----------------------------------------------------------------------
# Funckcja main 
def rozwiazyanie(plansza):
    while(True):
        start_plansza = copy.deepcopy(plansza)
        # kopia planszy by sprawdzic czy jakolwiek z funkcji zadziłała

        #tu nie potrzeba kokretnej liczby
        szukanie_w_kwadracie(plansza)
        
        for liczba in range(1,9):
            szukanie_poziomo(plansza,liczba)
            szukanie_poziomo(plansza,liczba)
            #ostatnie_pozostałe_wolne_pole_w_kwadracie(plansza,liczba)

        # Warianty
        temp_plansza = zmien_typ_planszy(plansza)

        #print(temp_plansza)
        for liczba in range(1,10):
            warianty(temp_plansza,liczba)
        
        #print(temp_plansza)
        oczywite_dwojki_trojki(temp_plansza)
        #print(temp_plansza)

        jedyne_miejsce_w_kwadracie(temp_plansza)
        jedyne_pole_poziomo_lub_pionowo(temp_plansza)
        #print(temp_plansza)

        przelozenie_wynikow(temp_plansza,plansza)

        #if(plansza.all() == start_plansza.all()): return plansza
        if(porownanie_tablic(start_plansza,plansza)): return plansza



# Niestety nie działa dla wszystkich plansz
plansza_1 = stwórz_plansze()
plansza_1 = uzupelni_plansze_z_pliku(lokalizcja,plansza_1,6)
print(plansza_1)
print("Tu rozwiazanie")
print(rozwiazyanie(plansza_1))


# Szablony do wykorzystania

# if(i%3 == 0 and j%3 == 0):
# # Jesli jest w górnej lewej kratce
    
# if(i%3 == 1 and j%3 == 0):
#     # Jesli jest w środkowej lewej kratce
    
# if(i%3 == 2 and j%3 == 0):
# # Jesli jest w dolnej lewej kratce
    
# if(i%3 == 0 and j%3 == 1):
# # Jesli jest w górnej środkowej kratce
    
# if(i%3 == 1 and j%3 == 1):
# # Jesli jest na środku
    
# if(i%3 == 2 and j%3 == 1):
# # Jesli jest w donej środkowej kratce
    
# if(i%3 == 0 and j%3 == 2):
# # Jesli jest w górnej prawej kratce
    
# if(i%3 == 1 and j%3 == 2):
# # Jesli jest w środkowej prawej kratce
    
# if(i%3 == 2 and j%3 == 2):
# # Jesli jest w dolnej praw kratce


# if(i%3 == 0 and j%3 == 0):
# # Jesli jest w górnej lewej kratce
    
# if(i%3 == 1 and j%3 == 0):
#     # Jesli jest w środkowej lewej kratce
    
# if(i%3 == 2 and j%3 == 0):
# # Jesli jest w dolnej lewej kratce
    
# if(i%3 == 0 and j%3 == 1):
# # Jesli jest w górnej środkowej kratce
    
# if(i%3 == 1 and j%3 == 1):
# # Jesli jest na środku
    
# if(i%3 == 2 and j%3 == 1):
# # Jesli jest w donej środkowej kratce
    
# if(i%3 == 0 and j%3 == 2):
# # Jesli jest w górnej prawej kratce
    
# if(i%3 == 1 and j%3 == 2):
# # Jesli jest w środkowej prawej kratce
    
# if(i%3 == 2 and j%3 == 2):
# # Jesli jest w dolnej praw kratce


                            # if(i%3 == 0 and j%3 == 0):
                            #     # Jesli jest w górnej lewej kratce
                            #     # TODO wymyslic lepszy sposób
                            #     temp = 0
                            #     for a in range(i,i+3): 
                            #         for b in range(j,j+3):

                                
                            # if(i%3 == 1 and j%3 == 0):
                            #     # Jesli jest w środkowej lewej kratce
                            #     temp = 0
                            #     for a in range(i-1,i+2): 
                            #         for b in range(j,j+3):

                            # if(i%3 == 2 and j%3 == 0):
                            # # Jesli jest w dolnej lewej kratce
                            #     temp = 0
                            #     for a in range(i-2,i+1): 
                            #         for b in range(j,j+3):

                            # if(i%3 == 0 and j%3 == 1):
                            # # Jesli jest w górnej środkowej kratce
                            #     temp = 0
                            #     for a in range(i,i+3): 
                            #         for b in range(j-1,j+2):

                            # if(i%3 == 1 and j%3 == 1):
                            # # Jesli jest na środku
                            #     temp = 0
                            #     for a in range(i-1,i+2): 
                            #         for b in range(j-1,j+2):

                            # if(i%3 == 2 and j%3 == 1):
                            # # Jesli jest w donej środkowej kratce
                            #     temp = 0
                            #     for a in range(i-2,i+1): 
                            #         for b in range(j-1,j+2):

                            # if(i%3 == 0 and j%3 == 2):
                            # # Jesli jest w górnej prawej kratce
                            #     temp = 0
                            #     for a in range(i,i+3): 
                            #         for b in range(j-2,j+1):

                            # if(i%3 == 1 and j%3 == 2):
                            # # Jesli jest w środkowej prawej kratce
                            #     temp = 0
                            #     for a in range(i-1,i+2): 
                            #         for b in range(j-2,j+1):

                            # if(i%3 == 2 and j%3 == 2):
                            # # Jesli jest w dolnej praw kratce
                            #     temp = 0
                            #     for a in range(i-2,i+1): 
                            #         for b in range(j-2,j+1):


