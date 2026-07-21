rozmiar = 100
tab = [[0 for _ in range(rozmiar)] for _ in range(rozmiar)]

def narysuj_kwadrat(x,y):
    for a in range(25):
        for b in range(25):
            tab[x+a][y+b] = 1

def narysuj_prostokat(x,y):
    for a in range(20):
        for b in range(30):
            tab[x+a][y+b] = 2

def czy_narysuj_kwadrat(x,y):
    try:
        for a in range(25):
            for b in range(25):
                if (tab[x+a][y+b] > 0): return False
    except IndexError:
        return False
    return True

def czy_narysuj_prostokat(x,y):
    try:
        for a in range(20):
            for b in range(30):
                if (tab[x+a][y+b] > 0): return False
    except IndexError:
        return False
    return True

tab_wspolrzednnych = []

for x in range(rozmiar):
    for y in range(rozmiar):
        if(len(tab_wspolrzednnych) % 3 == 0):
            if(tab[x][y] == 0):
                if(czy_narysuj_kwadrat(x,y)):
                    narysuj_kwadrat(x,y)
                    tab_wspolrzednnych.append((y,x))
                    tab_wspolrzednnych.append('kwadrat')
                    # jak wyciac
                    # for row in tab:
                    #     print("".join(map(str, row)))
                    # print('\n')
        else:02
,
if(tab[x][y] == 0):
                if(czy_narysuj_prostokat(x,y)):
                    narysuj_prostokat(x,y)
                    tab_wspolrzednnych.append((y,x))
                    tab_wspolrzednnych.append('prostokat')
                    # jak wyciac
                    # for row in tab:
                    #     print("".join(map(str, row)))
                    # print('\n')

print(tab_wspolrzednnych)

for row in tab:
    print("".join(map(str, row)))
