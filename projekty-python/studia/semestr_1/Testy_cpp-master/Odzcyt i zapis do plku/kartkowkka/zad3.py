plik = open("liczby5.txt")
y=plik.read().split() #
plik.close()
f = open("wynik_5.txt", "a")
f.write("\nzad 3 \n")

for k in y:
    pom=1
    if int(k)>=4000:
        if int(k)<=5000:
            pom=0
            g=2
            while( g<=int(k)):
                if (int(k)%g==0):
                    pom=1
                    
            if pom==0:
                f.write(str(k) + "\n")
plik.close()