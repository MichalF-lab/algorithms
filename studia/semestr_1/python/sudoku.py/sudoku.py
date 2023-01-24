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

def oczywite_dwójki_trójki(plansza):
    for i in range(9):
        # Dla każdego miejsca w rzedzie
        for j in range(9):
            # Sprawdzamy po kolmnach
            dana_para = plansza[i][j]
            if(i%3 == 0 and j%3 == 0):
            # Jesli jest w górnej lewej kratce
                temp = 0
                for a in range(i,i+3): 
                    for b in range(j,j+3):
                        if(plansza[a][b] == dana_para): temp+=1
                if(temp == 2):
                    for item

            if(i%3 == 1 and j%3 == 0):
                # Jesli jest w środkowej lewej kratce
                temp = 0
                for a in range(i-1,i+2): 
                    for b in range(j,j+3):

            if(i%3 == 2 and j%3 == 0):
            # Jesli jest w dolnej lewej kratce
                temp = 0
                for a in range(i-2,i+1): 
                    for b in range(j,j+3):

            if(i%3 == 0 and j%3 == 1):
            # Jesli jest w górnej środkowej kratce
                temp = 0
                for a in range(i,i+3): 
                    for b in range(j-1,j+2):

            if(i%3 == 1 and j%3 == 1):
            # Jesli jest na środku
                temp = 0
                for a in range(i-1,i+2): 
                    for b in range(j-1,j+2):

            if(i%3 == 2 and j%3 == 1):
            # Jesli jest w donej środkowej kratce
                temp = 0
                for a in range(i-2,i+1): 
                    for b in range(j-1,j+2):

            if(i%3 == 0 and j%3 == 2):
            # Jesli jest w górnej prawej kratce
                temp = 0
                for a in range(i,i+3): 
                    for b in range(j-2,j+1):

            if(i%3 == 1 and j%3 == 2):
            # Jesli jest w środkowej prawej kratce
                temp = 0
                for a in range(i-1,i+2): 
                    for b in range(j-2,j+1):

            if(i%3 == 2 and j%3 == 2):
            # Jesli jest w dolnej praw kratce
                temp = 0
                for a in range(i-2,i+1): 
                    for b in range(j-2,j+1):








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


