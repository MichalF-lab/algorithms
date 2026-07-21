# suma 1/n!

def funkcja(n):
    tab_wynik = [1]
    suma = 0
    for i in range (1,n):
        tab_wynik.append((tab_wynik[i-1]*(1/i)))
        suma+=tab_wynik[i]
    return suma
print(funkcja(100))

