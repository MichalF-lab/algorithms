def NWD(a = 1, b = 1):
    # a=int(input("wprowadz pierwsza liczba "))
    # b=int(input("wprowadz druga liczba "))
    while (a != b):
        if (a>b):
            a-=b
        else:
            b-=a
    return a

# print(NWD(50,24))