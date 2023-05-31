import math

# Funkcje pomocnicze

def NWW(a,b):
    if(a==b): return a
    if(a<=b): return NWW(a+temp1,b)
    if(a>=b): return NWW(a,b+temp2)

def random_prime_numbers():
    return 0

#Przespiane z nnotatek wylicznia

# p,q,e liczby pierwsze
p = 101
q = 3
e = 17
N = p*q

temp1 = (math.fabs((q-1)*(p-1)))
temp2 = e
temp3 = NWW(temp1,temp2)

c = temp3/temp1
d = temp3/temp2

klucz_prywatny = (d,p,q)
klucz_publiczny = (N,e)



#szyfrowanie wiadomoości !TODO Nie działa XD
# m - wiadmosć
m = 70

# Zaszyfrowana wiadomość
hash_meesage = math.pow(m,e) * math.fabs(N)

# Odszyfrowana wiadomość
un_hash_meesage = math.pow(c,d)*math.fabs(p*q)

print(un_hash_meesage)


