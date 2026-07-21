import math

# a = float(input('Podaj a: '))
# b = float(input('Podaj b: '))
# c = float(input('Podaj c: '))

def miejsca_zerowe_funkcji_kwadratowej(a = 0,b = 0, c = 0):
    delta = b*b-(4*a*c)
    if (delta < 0):
        print('Brak miejsc zerowych ')
    elif (delta == 0):
        x = -b/(2*a)
        print (x)
    else:
        x1 = ((-b-math.sqrt(delta))/2*a)
        x2 = ((-b+math.sqrt(delta))/2*a)
        print (x1,x2)