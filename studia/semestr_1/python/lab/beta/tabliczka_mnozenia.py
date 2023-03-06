def utworz_tablice(wymiar):
    # Tworzenie tablicy o danych wymiarach
    tablica = []
    for i in range(wymiar):
        tablica.append([])
        for _ in range(wymiar):
            tablica[i].append([])
    # Zapełnienie tablicy liczbami na brzgach
    for i in range(wymiar): tablica[0][i] = str(i)
    for i in range(wymiar): tablica[i][0] = str(i)
    # Uzupełnienie tablicy w pozostałych miejscach
    for i in range(1,wymiar):
        for j in range(1,wymiar):
            tablica[i][j] = i*j
    #print(tablica)
    return tablica

def utworz_tablice_niestandardowa(pocztek,koniec):
    # Tworzenie tablicy o danych wymiarach
    wymiar = koniec-pocztek
    if(wymiar < 1): return
    tablica = []
    for i in range(wymiar):
        tablica.append([])
        for _ in range(wymiar):
            tablica[i].append([])
    # Zapełnienie tablicy liczbami na brzgach
    for i in range(pocztek,koniec): tablica[0][i-pocztek] = str(i)
    for i in range(pocztek,koniec): tablica[i-pocztek][0] = str(i)
    # Uzupełnienie tablicy w pozostałych miejscach
    for i in range(1,wymiar):
        for j in range(1,wymiar):
            tablica[i][j] = int(tablica[0][i])*int(tablica[j][0])
    #print(tablica)
    return tablica



temp1 = utworz_tablice(10)
print(temp1)

temp2 = utworz_tablice_niestandardowa(10,16)
print(format(temp2))