a=int(input("wprowadz liczbe "))
b=a
odwrotnosc = 0
while (a>1):
    odwrotnosc+=a%10
    if (a>10):
        odwrotnosc=odwrotnosc * 10
    a=a//10
print("Liczba ",end="")
if (odwrotnosc != b): print("nie ",end="")
print("jest palindromiczna")