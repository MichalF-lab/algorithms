import math

def fibonaci(n):
    return math.ceil(1/math.sqrt(5)*((2/(math.sqrt(5)-1))**n)-1/math.sqrt(5)*((2/(-math.sqrt(5)-1))**n))

for i in range (15):
    print(fibonaci(i))

def fib_wzór(n):
    return int(((math.sqrt(5)+1)/2)**n/math.sqrt(5) + 0.5)

for i in range (73):
    if(fib_wzór(i) == fibonaci(i)): print("zgadza_sie")
    else: print("n")
