from pulp import *

problem = LpProblem("Najmniej wydanych pieniedzy", LpMinimize)

Miesiace = ['1','2','3','4','5','6,','7','8','9','10','11','12']
Zuzycie = {
    '1': 200,'2': 200, '3': 180, '4': 150, '5': 130, '6': 100,
    '7': 80, '8': 110, '9': 130, '10': 140, '11': 150, '12': 210
}

Koszt_produkcji_tabelka = {
    '1': 60,'2': 40, '3': 40, '4': 40, '5': 40, '6': 20,
    '7': 20, '8': 20, '9': 40, '10': 40, '11': 60, '12': 60
}
# Słownik zmiennych
koszt_produkcji = LpVariable.dicts("koszt_produkcji", Miesiace, 0, None, LpInteger)
ilosc_przechowywanej_energi = LpVariable.dicts("ilosc_przechowywanej_energi", Miesiace, 0, None, LpInteger)

problem += ((ilosc_przechowywanej_energi[miesiac] * 0,1) + (koszt_produkcji[miesiac] * Koszt_produkcji_tabelka[miesiac]) for miesiac in Miesiace)

for i in len(Miesiace):
    ilosc_przechowywanej_energi[i] >= 0

problem.solve()

print("Minimalna wartość funkcji celu:", value(problem.objective))
