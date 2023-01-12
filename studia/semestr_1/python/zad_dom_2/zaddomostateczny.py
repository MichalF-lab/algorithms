import random
import math

def find_min(W,a,b,z,s):#  W - funkcja, a - początek przedziału, b - koniec przedziału z - złożoność (najlepiej > 3) - s - średnica podziału?(step)
    prawdopodobne_przedzialy = []
    miejsce = a
    wartosc_najmniejsza = W(a)
    temp_a = a
    while(temp_a <= b):
        if(W(temp_a) < wartosc_najmniejsza): 
            wartosc_najmniejsza = W(temp_a)
            miejsce = temp_a
        temp_a+=s

    temp_a = a

    nwm = 2 # tolerowany zakres?
    while(temp_a <= b):
        if(W(temp_a)-nwm <= wartosc_najmniejsza): prawdopodobne_przedzialy.append(temp_a)
        temp_a+=s
    
    for i in range(len(prawdopodobne_przedzialy)):
        for j in range(z):
            temp = random.uniform(prawdopodobne_przedzialy[i]-(s*0.5),prawdopodobne_przedzialy[i]+(s*0.5)) #0.5 jest optymalne imo
            if(temp < wartosc_najmniejsza): 
                wartosc_najmniejsza = temp
                miejsce = temp
    return (wartosc_najmniejsza, temp)

#----------------------------------------------Testy
def W1(x):
    return 10*(1+(x)**2/3-math.cos(3*math.pi*(x)))
def W2(x):
    return x*x*x-8*x+2
def W3(x):
    return x*x-8*x+2    
def W4(x):
    return x*x*x*x*x*x-62*x*x*x+13*x+1382.1333
def W5(x):
    return math.tan(x)

print(find_min(W1,-10,10,3,0.1))
print(find_min(W1,-10,10,10,0.05))

print(find_min(W2,-10,10,5,0.05))

print(find_min(W3,-10,10,5,0.05))

print(find_min(W4,-10,10,5,0.1))
print(find_min(W4,-10,10,50,0.05))

print(find_min(W5,-10,10,50,0.5))
print(find_min(W5,-10,10,50,0.05))
print(find_min(W5,-10,10,50,0.005))
print(find_min(W5,-10,10,50,0.0005))
print(find_min(W5,-10,10,500,0.0005))