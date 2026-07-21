def ctrójkąt_istnieje(a,b,c):
#     a = int(input("Podaj pierwsza wartosc "))
#     b = int(input("Podaj druga wartosc "))
#     c = int(input("Podaj trzecia wartosc "))
    if(a + b > c):
        if(c + b > a):
            if(a + c > b):
                # print("Istnieje taki trojkat")
                return True
    else:
        # print("Nie istnieje taki trojkat")
        return False
