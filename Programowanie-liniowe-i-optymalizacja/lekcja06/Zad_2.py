a = 2
b = 7
c = 5
d = 9
e = 5
f = 1

AB = a
AC = b
AD = c
AE = d
BC = f 
BD = a 
BE = c
CD = e
DE = b
DF = f
EF = b

def stanF():
    return 0

def stanE():
    return EF + stanF()

def stanD():
    return min(
        DF + stanF(), 
        DE + stanE()
    )

def stanC():
    return CD + stanD()

def stanB():
    return min(
        BC + stanC(),
        BD + stanD(),
        BE + stanE()
    )

def StanA():
    return min(
        AB + stanB(),
        AC + stanC(),
        AD + stanD(),
        AE + stanE()
    )

print(StanA())