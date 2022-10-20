a=int(input("wprowadz szerokosc "))
b=int(input("wprowadz wysokosc "))
for i in range (b):
    if (i == 0 or i == b-2):
        for g in range (a):
            print ("X",end="")
        print("")
    if (i == b-2): break
    print("X",end="")
    for g in range (a-2):
        print(" ",end="")
    print("X")    