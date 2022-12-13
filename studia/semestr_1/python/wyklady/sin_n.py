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
    print(ile)

def czy_liczba_jest_pierwsza(a):
    for i in range(1,(a+1)//2+1): 
        if (a%i == 0): return False
        return True

ile_iczb_pierwszych(100)