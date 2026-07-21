import random
import numpy
import time

def cut_rod(p,n):
    if n == 0:
        return 0
    max_val = 0
    for i in range(1, n + 1):
        max_val = max(max_val, p[i - 1] + cut_rod(p, n - i))
    return max_val

#---------------------------------------------------------------------------


def memorized_cut_rod(p,n):
    tab = [0 for _ in range(n+1)]
    def cut_rodt(p,n):
        if tab[n] > 0: return tab[n]
        if n == 0:
            return 0
        max_val = 0
        for i in range(1, n + 1):
            max_val = max(max_val, p[i - 1] + cut_rodt(p, n - i))
            tab[n] = max_val
        return max_val
    return cut_rodt(p,n)

#---------------------------------------------------------------------------

def memorized_cut_rod_solution(p,n):
    tab = [0 for _ in range(n+1)]
    sol = [0 for _ in range(n+1)]
    def cut_rodt(p,n):
        tab, sol
        if tab[n] > 0: return tab[n]
        if n == 0:
            return 0
        max_val, cut = 0, 0
        for i in range(1, n + 1):
            if (max_val < p[i - 1] + cut_rodt(p, n - i)): cut = i
            max_val =p[i - 1] + cut_rodt(p, n - i)
        sol[n] = cut
        tab[n] = max_val
        return max_val
    cut_rodt(p,n)
    return sol

#---------------------------------------------------------------------------

def bottom_up_lcs_solution(x,y):
    max_l ,l= 0, ''
    # x, y = list(x),list(y)
    for _x in range(len(x)):
        for _y in range(len(y)):
            if y[_y] != x[_x]: continue
            temp = 1
            while True:
                if y[_y + temp] != x[_x + temp]: break
                temp += 1
            if temp > max_l: max_l, l = temp, y[:temp]


    return l

#---------------------------------------------------------------------------
def  bottom_up_lcs(x,y):
    max_l = 0
    # x, y = list(x),list(y)
    for _x in range(len(x)):
        for _y in range(len(y)):
            if y[_y] != x[_x]: continue
            temp = 1
            while True:
                if y[_y + temp] != x[_x + temp]: break
                temp += 1
            if temp > max_l: max_l = temp,


    return max_l
#---------------------------------------------------------------------------

def memorized_lcs(x,y):
    max_l = 0
    tab = []
    # x, y = list(x),list(y)
    for _x in range(len(x)):
        if _x not in tab:
            tab.append(_x)
            for _y in range(len(y)):
                if y[_y] != x[_x]: continue
                temp = 1
                while True:
                    if y[_y + temp] != x[_x + temp]: break
                    temp += 1
                if temp > max_l: max_l = temp


    return max_l

#--------------------------------------------------

def lcs(x ,y):
    max_l = 0
    # x, y = list(x),list(y)
    for _y in range(len(y)):
        if y[_y] != x[0]: continue
        temp = 1
        while True:
            if y[_y + temp] != x[temp]: break
            temp += 1
        if temp > max_l: max_l = temp


    return max(max_l, lcs(x[1:],y))

#----------------------------------------------

if __name__ == '__main__':

    def test_sortowania(algorytm, tablica,a, nazwa_algorytmu):
        start_time = time.time()
        algorytm(tablica,a)
        end_time = time.time()
        print(f"{nazwa_algorytmu}: {end_time - start_time:.6f} sekundy")
    
    def test_sortowaniat(algorytm, tablica,a,nazwa_algorytmu):
        start_time = time.time()
        algorytm(tablica,a)
        end_time = time.time()
        print(f"{nazwa_algorytmu}: {end_time - start_time:.6f} sekundy")
        
    main_table = numpy.arange(random.randint(5,7))

    for item in main_table:
        main_table[item] = int(random.randint(70,130)) + main_table[item - 1]

    strmain_table = numpy.arange(random.randint(5,7))

    for item in strmain_table:
        strmain_table[item] = str(random.randint(80,120))

    #---------------------------------------------------------------------------

    print(main_table)

    test_sortowania(cut_rod, main_table.copy(),len(main_table), "cut_rod")
    test_sortowania(memorized_cut_rod_solution, main_table.copy(),len(main_table), "memorized_cut_rod_solution")
    test_sortowania(memorized_cut_rod, main_table.copy(),len(main_table), "memorized_cut_rod")

    #---------------------------------------------------------------------------
        
    test_sortowaniat(lcs, main_table.copy(),len(main_table), "lcs")
    test_sortowaniat(memorized_lcs, main_table.copy(),len(main_table), "memorized_lcs")
    test_sortowaniat(bottom_up_lcs, main_table.copy(),len(main_table), "memorized_cut_rod")
    test_sortowaniat(bottom_up_lcs_solution, main_table.copy(),len(main_table), "bottom_up_lcs_solution")

    #----------------------------------------------------------------------------

    print(memorized_lcs("acefged", "efgsbhi"))

    print(bottom_up_lcs_solution("acefged", "efgsbhi"))
