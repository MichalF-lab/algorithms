 
# # liczba = 2

# # plansza =[[(9,2,3,4,5)],[()]]

# # if(plansza[0][0] is tuple):
# #     try:
# #         temp = list(plansza[0][0])
# #         temp.remove(liczba)
# #         plansza[0][0] = tuple(temp)
# #         print("działa")
# #     except BaseException:
# #         print("nie dziala")
# # print(plansza)


# def NWW(*tab):
#     for i in tab:
#         print("cokolwiek")
#         iterator1 = iter(tab)
#         iterator2 = iter(tab)
#         next(iterator2)
#         while (iterator1 != iterator2):
#             if (iterator1 > iterator2):
#                 iterator1+=iterator2
#             else:
#                 iterator2+=iterator1
#         print(tab[i])


# print(NWW(90,17,22))

# import numpy as np

# def stwórz_plansze():
#     plansza = np.empty((9,9),dtype="u1")
#     return plansza

# def uzupelni_plansze_z_pliku(plik, plansza, liczba):
#      file = open(plik)
#      for line in file:
#         f = file.readline()
#         if("Grid" in str(f) and str(liczba) in str(f)):
#             # dla każdego wiersza
#             f = file.readline()
#             for i in range(9):
#                 print(f) # TODO ten print musi byc
#                 # dla każdego numerku
#                 for zmienna in range(9):
#                     if(int(f[zmienna]) != 0):
#                         plansza[i][zmienna] = int(f[zmienna])
#                     #print(f[zmienna])
#                 f = file.readline()
                    
#      return plansza


# def wypisz(plansza):
#     for i in plansza:
#         print(" ".join([str(k) for k in i]))



# plansza_1 = stwórz_plansze()
# plansza_1 = uzupelni_plansze_z_pliku("studia\semestr_1\python\sudoku.py\sudoku.txt",plansza_1,10)
# print(plansza_1)
# print(plansza_1[0][0])

M = 9
def puzzle(a):
    for i in range(M):
        for j in range(M):
            print(a[i][j],end = " ")
        print()
def solve(grid, row, col, num):
    for x in range(9):
        if grid[row][x] == num:
            return False
             
    for x in range(9):
        if grid[x][col] == num:
            return False
 
 
    startRow = row - row % 3
    startCol = col - col % 3
    for i in range(3):
        for j in range(3):
            if grid[i + startRow][j + startCol] == num:
                return False
    return True
 
def Suduko(grid, row, col):
 
    if (row == M - 1 and col == M):
        return True
    if col == M:
        row += 1
        col = 0
    if grid[row][col] > 0:
        return Suduko(grid, row, col + 1)
    for num in range(1, M + 1, 1): 
     
        if solve(grid, row, col, num):
         
            grid[row][col] = num
            if Suduko(grid, row, col + 1):
                return True
        grid[row][col] = 0
    return False
 
'''0 means the cells where no value is assigned'''
grid = [[2, 5, 0, 0, 3, 0, 9, 0, 1],
        [0, 1, 0, 0, 0, 4, 0, 0, 0],
    [4, 0, 7, 0, 0, 0, 2, 0, 8],
    [0, 0, 5, 2, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 9, 8, 1, 0, 0],
    [0, 4, 0, 0, 0, 3, 0, 0, 0],
    [0, 0, 0, 3, 6, 0, 0, 7, 2],
    [0, 7, 0, 0, 0, 0, 0, 0, 3],
    [9, 0, 3, 0, 0, 0, 6, 0, 4]]
 
if (Suduko(grid, 0, 0)):
    puzzle(grid)
else:
    print("Solution does not exist:(")