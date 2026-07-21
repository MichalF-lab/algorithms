def wypisz_binarnie(liczba:int):
    if(liczba == 1):
        print(1, end=''),
        return 0
    wypisz_binarnie(liczba//2)
    print(liczba%2 , end='')

# wypisz_binarnie(173)