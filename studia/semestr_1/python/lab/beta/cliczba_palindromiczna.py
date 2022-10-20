from operator import truediv


def cliczba_palindromiczna(a):
    #a=int(input("wprowadz liczbe "))
    b=a
    odwrotnosc = 0
    while (a>1):
        odwrotnosc+=a%10
        if (a>10):
            odwrotnosc=odwrotnosc * 10
        a=a//10
    # print("Liczba ",end="")
    # if (odwrotnosc != b): print("nie ",end="")
    # print("jest palindromiczna")
    if (odwrotnosc != b): return False
    return True

# print(cliczba_palindromiczna(7))
# print(cliczba_palindromiczna(134))