plik = open('liczby5.txt')
y=plik.read().split() 
plik.close()
f = open("wynik_5.txt", "a")
f.write("\nzad 3 \n")
for k in y:
    if int(k)>=4000:
        if int(k)<=5000:
            g=2
            while( g<=int(k)):
                if (int(k)%g==0):
                    break
            f.write(str(k) + "\n")
f.close()
