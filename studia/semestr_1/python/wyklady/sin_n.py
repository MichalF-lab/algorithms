import math
# import matplotlib.pyplot as plt

# ilosc_punktow = 1000

# for i in range(10):
#     tab = [math.sin(math.ceil(math.pi * 10**i)) for n in range (ilosc_punktow-1)]
#     plt.scatter(tab,ilosc_punktow)

def ile_iczb_pierwszych(n):
    ile = 0
    for i in range(1,n+1):
        if(czy_liczba_jest_pierwsza(i) == True): ile+=1
    return ile

def czy_liczba_jest_pierwsza(a):
    for i in range(2,a+1): 
        if (i==a):return True
        if (a%i == 0): return False

ile_iczb_pierwszych(11)

import matplotlib.pyplot as plt

ile = 200
tab = [ile_iczb_pierwszych(i) for i in range (ile)]
plt.plot(tab,ile)