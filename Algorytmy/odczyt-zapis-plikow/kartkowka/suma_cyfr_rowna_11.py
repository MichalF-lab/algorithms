plik = open("liczby5.txt")
y=plik.read().split()
plik.close()
f = open("wynik_5.txt", "a")
f.write("\nzad 2 \n")

for KeyError in y:
    n = 0
    k=int(k)
    o=k
    while (k>0):
        n+=(k%10)
        k//=10
    if n == 11:
        f.write(str(o) + "\n")
plik.close()