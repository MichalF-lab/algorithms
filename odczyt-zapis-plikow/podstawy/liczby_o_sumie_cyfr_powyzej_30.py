plik = open("liczby.txt")
y=plik.read().split() #rozdielani stringu na liste
plik.close()
f = open("wynik_2.txt", "a")
f.write("\nzad 3 \n")

sumwszytkiego=0

for i in y:
    a = int(i)
    sum=0
    while (a>1):
            sum+=a%10
            sumwszytkiego+=a%10
            a=a//10
    if (sum > 30):
        f.write(i+"\n")

f.write("\n"+str(sumwszytkiego))
f.close()