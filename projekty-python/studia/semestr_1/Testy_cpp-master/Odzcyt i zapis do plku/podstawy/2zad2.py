plik = open("liczby.txt")
y=plik.read().split() #rozdielani stringu na liste
plik.close()
f = open("wynik_2.txt", "a")
f.write("\nzad 2 \n")

for i in y:
    a = int(i)
    b=a
    odwrotnosc = 0
    while (a>1):
        odwrotnosc+=a%10
        if (a>10):
            odwrotnosc=odwrotnosc * 10
        a=a//10
    if (odwrotnosc == b):
        f.write(str(b)+"\n")

f.close()