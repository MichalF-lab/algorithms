plik = open("liczby.txt")
y=plik.read().split() #rozdielani stringu na liste
plik.close()

max=0
for i in y:
    i = int(i)
    if i%2==0:
        if i > max:
            max = i
f = open("wynik_2.txt", "a")
wynik = str(max)
f.write("\nzad 1 \n"+str(wynik)+"\n")
f.close()