temp1 = lambda x: x+1
# print(temp1(8))

temp2 = lambda x,y: x*y
# print(temp2(12,11))

# funkcja wyższego rzędu
    
def funkcja(f,liczba):
    return f(liczba)

# print(funkcja(lambda x: x+1, 7))
# print(funkcja(lambda x: x*x, 7))

tab1 = [1,2,4,56,7,2334,6,8532,5,32135]

# def sort1(tab):
#     tab.sort()

# tab2 = lambda tab: tab.sort1()

# print(tab2(tab1))

import random
count = 100
tab_rand1 = [random.randint(1,15) for i in range(count)]
# print(dir(random))

tab_rand1.sort()
# print(tab_rand1)

# import numpy as np
# import matplotlib.pyplot as plt

# plt.scatter(tab_rand1,range(count))
# plt.show

def suma(a,b):
    x = lambda a: b + b
    return x(b)

mnozenia = lambda a,b: a*b

# print(mnozenia(21,3))

tab_lam_rand1 = [random.randint(0,i) for i in range(count)]
tab_lam_rand2 = [(lambda a: i-10)(i) for i in range(count)]
print(tab_lam_rand2)

