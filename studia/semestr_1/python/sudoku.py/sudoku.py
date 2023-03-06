import math
import numpy as np
import copy
# ----------------------------------------------------------------------
# tworzenie / imort tablic testy

plansza1 = np.empty((9,9),dtype="u1")
 


#-----------------------------------------------------------------------
# Funkcje

#-----------------------------------------------------------------------
# Funckcja main 
def rozwiazyanie(plansza):
    while(True):
        temp_plansza = copy.deepcopy(plansza)
        # kopia planszy by sprawdzic czy jakolwiek z funkcji zadziłała

        szukanie_w_kwadracie(plansza) #tu nie potrzeba kokretnej liczby
        for liczba in range(1,9):
            szukanie_poziomo(plansza,liczba)
            szukanie_poziomo(plansza,liczba)
            ostatnie_pozostałe_wolne_pole_w_kwadracie(plansza,liczba)
        if(plansza == temp_plansza): return wynik(plansza)

def wynik(plansza):
    print(plansza)

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
    if(plansza[i][j] == int): return True
    return False

#--------------------------------------------------------------------------------
# Funkcje Trywialne 

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
            if(czy_ustalone(plansza[i][j] == False)):
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
            if(czy_ustalone(plansza[i][j] == False)):
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
            if(czy_ustalone(plansza[i][j] == False)):
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
            if(czy_ustalone(plansza[i][j] == False)):
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
            if(czy_ustalone(plansza[i][j] == False)):
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
            if(czy_ustalone(plansza[i][j] == False)):
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
            if(czy_ustalone(plansza[i][j] == False)):
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
            if(czy_ustalone(plansza[i][j] == False)):
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
            if(czy_ustalone(plansza[i][j] == False)):
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
            if(czy_ustalone(plansza[i][j] == False)):
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

# Dla danego pola sprawdza czy w tym kwadracie istnieja inne polew ktore można wpisać to liczbe + dodatkowe miejsca poziomo juz sa zajete
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
    if(operacja == 1):
    # usun dana liczbe w pozostałych miejscach w kwadracie
        if(i%3 == 0 and j%3 == 0):
            # Jesli jest w górnej lewej kratce
            for a in range(i,i+3): 
                for b in range(j,j+3):
                    if(plansza[a][b] is tuple and plansza[a][b] != nie_usuwac):
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
                    if(plansza[a][b] is tuple and plansza[a][b] != nie_usuwac):
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
                    if(plansza[a][b] is tuple and plansza[a][b] != nie_usuwac):
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
                    if(plansza[a][b] is tuple and plansza[a][b] != nie_usuwac):
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
                    if(plansza[a][b] is tuple and plansza[a][b] != nie_usuwac):
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
                    if(plansza[a][b] is tuple and plansza[a][b] != nie_usuwac):
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
                    if(plansza[a][b] is tuple and plansza[a][b] != nie_usuwac):
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
                    if(plansza[a][b] is tuple and plansza[a][b] != nie_usuwac):
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
                    if(plansza[a][b] is tuple and plansza[a][b] != nie_usuwac):
                        try:
                            temp = list(plansza[a][b])
                            temp.remove(liczba)
                            plansza[a][b] = tuple(temp)
                        except BaseException:
                            continue
    if(operacja == 2):
    # usun liczbe w kolmnie i
        if(w_wariantach_czy_istnieje_poziomo(plansza,liczba,i) == True):
            for b in range(9):
                if(plansza[i][b] is tuple):
                        try:
                            temp = list(plansza[i][b])
                            temp.remove(liczba)
                            plansza[i][b] = tuple(temp)
                        except BaseException:
                            continue

    if(operacja == 3):
     # usun liczbe w rzedzie j
        if(w_wariantach_czy_istnieje_pionowo(plansza,liczba,j) == True):
            for a in range(9):
                if(plansza[i][b] is tuple):
                        try:
                            temp = list(plansza[i][b])
                            temp.remove(liczba)
                            plansza[i][b] = tuple(temp)
                        except BaseException:
                            continue
    if(operacja == 4):
    # usuń na konkretnym  miejscu
        if(plansza[i][j] is tuple):
            try:
                temp = list(plansza[i][j])
                temp.remove(liczba)
                plansza[i][b] = tuple(temp)
            except BaseException:
                return 0


#--------------------------------------------------------------------------------------
# Możliwe warianty
# Do każdego pola przypiujemy możliwe liczby

def warianty(plansza,liczba):
      for i in range(9):
            # Dla każdego miejsca w rzedzie
            if(czy_istnieje_poziomo(plansza,liczba,i) == False):
                # Jeżeli liczba nie występuje w danym rzedzie
                for j in range(9):
                    # Sprawdzamy po kolmnach
                    if(czy_ustalone(plansza,i,j) == False):
                    #Jeżeli na danym polu nie ma konkretnej liczby
                       if(czy_istnieje_pionowo(plansza,liczba,j) == False):
                            if(i%3 == 0 and j%3 == 0):
                                # Jesli jest w górnej lewej kratce
                                temp = 0
                                for a in range(i,i+3): 
                                    for b in range(j,j+3):
                                        if(plansza[a][b] == liczba): temp+=1
                                if(czy_istnieje_pionowo(plansza,liczba,i)):temp+=1
                                if(czy_istnieje_poziomo(plansza,liczba,j)):temp+=1
                                if(temp == 0): plansza[i][j]+=(liczba,)
                                
                            if(i%3 == 1 and j%3 == 0):
                                # Jesli jest w środkowej lewej kratce
                                temp = 0
                                for a in range(i-1,i+2): 
                                    for b in range(j,j+3):
                                        if(plansza[a][b] == liczba): temp+=1
                                if(czy_istnieje_pionowo(plansza,liczba,i)):temp+=1
                                if(czy_istnieje_poziomo(plansza,liczba,j)):temp+=1
                                if(temp == 0): plansza[i][j]+=(liczba,)
                            if(i%3 == 2 and j%3 == 0):
                            # Jesli jest w dolnej lewej kratce
                                temp = 0
                                for a in range(i-2,i+1): 
                                    for b in range(j,j+3):
                                        if(plansza[a][b] == liczba): temp+=1
                                if(czy_istnieje_pionowo(plansza,liczba,i)):temp+=1
                                if(czy_istnieje_poziomo(plansza,liczba,j)):temp+=1
                                if(temp == 0): plansza[i][j]+=(liczba,)
                            if(i%3 == 0 and j%3 == 1):
                            # Jesli jest w górnej środkowej kratce
                                temp = 0
                                for a in range(i,i+3): 
                                    for b in range(j-1,j+2):
                                        if(plansza[a][b] == liczba): temp+=1
                                if(czy_istnieje_pionowo(plansza,liczba,i)):temp+=1
                                if(czy_istnieje_poziomo(plansza,liczba,j)):temp+=1
                                if(temp == 0): plansza[i][j]+=(liczba,)
                            if(i%3 == 1 and j%3 == 1):
                            # Jesli jest na środku
                                temp = 0
                                for a in range(i-1,i+2): 
                                    for b in range(j-1,j+2):
                                        if(plansza[a][b] == liczba): temp+=1
                                if(czy_istnieje_pionowo(plansza,liczba,i)):temp+=1
                                if(czy_istnieje_poziomo(plansza,liczba,j)):temp+=1
                                if(temp == 0): plansza[i][j]+=(liczba,)
                            if(i%3 == 2 and j%3 == 1):
                            # Jesli jest w donej środkowej kratce
                                temp = 0
                                for a in range(i-2,i+1): 
                                    for b in range(j-1,j+2):
                                        if(plansza[a][b] == liczba): temp+=1
                                if(czy_istnieje_pionowo(plansza,liczba,i)):temp+=1
                                if(czy_istnieje_poziomo(plansza,liczba,j)):temp+=1
                                if(temp == 0): plansza[i][j]+=(liczba,)
                            if(i%3 == 0 and j%3 == 2):
                            # Jesli jest w górnej prawej kratce
                                temp = 0
                                for a in range(i,i+3): 
                                    for b in range(j-2,j+1):
                                        if(plansza[a][b] == liczba): temp+=1
                                if(czy_istnieje_pionowo(plansza,liczba,i)):temp+=1
                                if(czy_istnieje_poziomo(plansza,liczba,j)):temp+=1
                                if(temp == 0): plansza[i][j]+=(liczba,)
                            if(i%3 == 1 and j%3 == 2):
                            # Jesli jest w środkowej prawej kratce
                                temp = 0
                                for a in range(i-1,i+2): 
                                    for b in range(j-2,j+1):
                                        if(plansza[a][b] == liczba): temp+=1
                                if(czy_istnieje_pionowo(plansza,liczba,i)):temp+=1
                                if(czy_istnieje_poziomo(plansza,liczba,j)):temp+=1
                                if(temp == 0): plansza[i][j]+=(liczba,)
                            if(i%3 == 2 and j%3 == 2):
                            # Jesli jest w dolnej praw kratce
                                temp = 0
                                for a in range(i-2,i+1): 
                                    for b in range(j-2,j+1):
                                        if(plansza[a][b] == liczba): temp+=1
                                if(czy_istnieje_pionowo(plansza,liczba,i)):temp+=1
                                if(czy_istnieje_poziomo(plansza,liczba,j)):temp+=1
                                if(temp == 0): plansza[i][j]+=(liczba,)


# Jezeli w danym kwadracie jest tylko w jednym miejscu przewidywana dana liczba        
def jedyne_miejsce_w_kwadracie(plansza):
    for i in range(9):
            # Dla każdego miejsca w rzedzie
            for j in range(9):
                # Sprawdzamy po kolmnach
                
                #--------------------------------------------------------------
                if(plansza[i][j] is tuple and len(plansza[i][j]) == 1): plansza[i][j] = int(plansza[i][j])
                #--------------------------------------------------------------

                if(czy_ustalone(plansza,i,j) == False):
                #Jeżeli na danym polu nie ma konkretnej liczby

                    if(i%3 == 0 and j%3 == 0):
                        # Jesli jest w górnej lewej kratce
                        temp = 0
                        for konkretny_item in plansza[i][j]:
                            for a in range(i,i+3): 
                                for b in range(j,j+3):
                                    for item in plansza[a][b]:
                                        if(item == konkretny_item): temp+=1
                            if(temp==1): plansza[i][j] = konkretny_item
                                    
                                                            
                    if(i%3 == 1 and j%3 == 0):
                        # Jesli jest w środkowej lewej kratce
                        for konkretny_item in plansza[i][j]:
                            temp = 0
                            for a in range(i-1,i+2): 
                                for b in range(j,j+3):
                                    for item in plansza[a][b]:
                                        if(item == konkretny_item): temp+=1
                            if(temp==1): plansza[i][j] = konkretny_item

                    if(i%3 == 2 and j%3 == 0):
                    # Jesli jest w dolnej lewej kratce
                        for konkretny_item in plansza[i][j]:
                            temp = 0
                            for a in range(i-2,i+1): 
                                for b in range(j,j+3):
                                    for item in plansza[a][b]:
                                        if(item == konkretny_item): temp+=1
                            if(temp==1): plansza[i][j] = konkretny_item

                    if(i%3 == 0 and j%3 == 1):
                    # Jesli jest w górnej środkowej kratce
                        for konkretny_item in plansza[i][j]:                       
                            temp = 0
                            for a in range(i,i+3): 
                                for b in range(j-1,j+2):
                                    for item in plansza[a][b]:
                                        if(item == konkretny_item): temp+=1
                            if(temp==1): plansza[i][j] = konkretny_item

                    if(i%3 == 1 and j%3 == 1):
                    # Jesli jest na środku
                        for konkretny_item in plansza[i][j]:
                            temp = 0
                            for a in range(i-1,i+2): 
                                for b in range(j-1,j+2):
                                    for item in plansza[a][b]:
                                        if(item == konkretny_item): temp+=1
                            if(temp==1): plansza[i][j] = konkretny_item

                    if(i%3 == 2 and j%3 == 1):
                    # Jesli jest w donej środkowej kratce
                        for konkretny_item in plansza[i][j]:
                            temp = 0
                            for a in range(i-2,i+1): 
                                for b in range(j-1,j+2):
                                    for item in plansza[a][b]:
                                        if(item == konkretny_item): temp+=1
                            if(temp==1): plansza[i][j] = konkretny_item

                    if(i%3 == 0 and j%3 == 2):
                    # Jesli jest w górnej prawej kratce
                        for konkretny_item in plansza[i][j]:
                            temp = 0
                            for a in range(i,i+3): 
                                for b in range(j-2,j+1):
                                    for item in plansza[a][b]:
                                        if(item == konkretny_item): temp+=1
                            if(temp==1): plansza[i][j] = konkretny_item

                    if(i%3 == 1 and j%3 == 2):
                    # Jesli jest w środkowej prawej kratce
                        for konkretny_item in plansza[i][j]:
                            temp = 0
                            for a in range(i-1,i+2): 
                                for b in range(j-2,j+1):
                                    for item in plansza[a][b]:
                                        if(item == konkretny_item): temp+=1
                            if(temp==1): plansza[i][j] = konkretny_item

                    if(i%3 == 2 and j%3 == 2):
                    # Jesli jest w dolnej praw kratce
                        for konkretny_item in plansza[i][j]:
                            temp = 0
                            for a in range(i-2,i+1): 
                                for b in range(j-2,j+1):
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
                if(plansza[i][j] is tuple and len(plansza[i][j]) == 1): plansza[i][j] = int(plansza[i][j])
                #--------------------------------------------------------------

                if(czy_ustalone(plansza,i,j) == False):
                #Jeżeli na danym polu nie ma konkretnej liczby

                    for item in plansza[i][j]:
                        if(w_wariantach_czy_istnieje_poziomo(plansza,item,j) and w_wariantach_czy_istnieje_pionowo(plansza,item,i)):
                            plansza[i][j] = item
                            break
                        # Trzeba to przejzec TODO

def oczywite_dwójki_trójki(plansza):
    for i in range(9):
        # Dla każdego miejsca w rzedzie
        for j in range(9):
            # Sprawdzamy po kolmnach
            if(plansza[i][j] is tuple):
                dana_para = plansza[i][j]
                if(i%3 == 0 and j%3 == 0):
                # Jesli jest w górnej lewej kratce
                    temp = 0 # ilosc takich samych krotek
                    wystapienia_w_kwadracie = [range(10)]
                    for a in range(i,i+3): 
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
                    for a in range(i,i+3): 
                        for b in range(j,j+3):
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
                    wystapienia_w_kwadracie = [range(10)]
                    for a in range(i-1,i+2): 
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
                    for a in range(i-1,i+2): 
                        for b in range(j,j+3):
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
                    wystapienia_w_kwadracie = [range(10)]
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
                    wystapienia_w_kwadracie = [range(10)]
                    for a in range(i,i+3): 
                        for b in range(j-1,j+2):
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
                    for a in range(i,i+3): 
                        for b in range(j-1,j+2):
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
                    wystapienia_w_kwadracie = [range(10)]
                    for a in range(i-1,i+2): 
                        for b in range(j-1,j+2):
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
                    for a in range(i-1,i+2): 
                        for b in range(j-1,j+2):
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
                    wystapienia_w_kwadracie = [range(10)]
                    for a in range(i-2,i+1): 
                        for b in range(j-1,j+2):
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
                        for b in range(j-1,j+2):
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
                    wystapienia_w_kwadracie = [range(10)]
                    for a in range(i,i+3): 
                        for b in range(j-2,j+1):
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
                    for a in range(i,i+3): 
                        for b in range(j-2,j+1):
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
                # Jesli jest w środkowej prawej kratce
                    temp = 0 # ilosc takich samych krotek
                    wystapienia_w_kwadracie = [range(10)]
                    for a in range(i-1,i+2): 
                        for b in range(j-2,j+1):
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
                    for a in range(i-1,i+2): 
                        for b in range(j-2,j+1):
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
                    wystapienia_w_kwadracie = [range(10)]
                    for a in range(i-2,i+1): 
                        for b in range(j-2,j+1):
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
                        for b in range(j-2,j+1):
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


