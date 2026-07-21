a=int(input("wprowadz pierwsza liczba "))
b=int(input("wprowadz druga liczba "))
while (a != b):
    if (a>b):
        a-=b
    else:
        b-=a
print(a)