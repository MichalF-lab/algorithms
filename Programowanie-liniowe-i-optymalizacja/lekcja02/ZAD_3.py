from pulp import *

# Utworzenie problemu
problem = LpProblem("Transfery_pieniedzy", LpMinimize)


# A - Anna, B - Bartek, C - Celina, D - Dominika
AB = LpVariable("Anna_Bartek", 0, None)
AC = LpVariable("Anna_Celina", 0, None)
AD = LpVariable("Anna_Dominika", 0, None) 

BA = LpVariable("Bartek_Anna", 0, None)
BC = LpVariable("Bartek_Celina", 0, None)
BD = LpVariable("Bartek_Dominika", 0, None)

CA = LpVariable("Celina_Anna", 0, None)
CB = LpVariable("Celina_Bartek", 0, None)
CD = LpVariable("Celina_Dominika", 0, None)

DA = LpVariable("Dominika_Anna", 0, None)
DB = LpVariable("Dominika_Bartek", 0, None)
DC = LpVariable("Dominika_Celina", 0, None)


problem += AB + AC + AD + BA + BC + BD + CA + CB + CD + DA + DB + DC

problem += (AB + AC + AD) - (BA + CA + DA) == (50 + 30 + 20) - (20 + 10 + 40)
problem += (BA + BC + BD) - (AB + CB + DB) == (20 + 40 + 10) - (50 + 60 + 20)
problem += (CA + CB + CD) - (AC + BC + DC) == (10 + 60 + 30) - (30 + 40 + 50)
problem += (DA + DB + DC) - (AD + BD + CD) == (40 + 20 + 50) - (20 + 10 + 30)

problem.solve()

# Wyświetlenie wyników
print("Optymalne transfery:")
for i in problem.variables():
    if value(i) > 0:
        print(i.name,": ",value(i)," zl")
