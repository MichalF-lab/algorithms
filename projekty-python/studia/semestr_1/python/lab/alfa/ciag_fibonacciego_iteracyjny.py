def fi():
    a=1
    b=1
    k = int(input("Wprowaz numer większy od zera "))
    
    if k == 0:
        print(0)
    else:
        for i in range (k):
            print(a, end=' ')
            b+=a
            a=b-a 


g=fi()