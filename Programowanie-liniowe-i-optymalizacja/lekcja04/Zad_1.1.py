#! Nie do oceny
from pulp import * 

problem = LpProblem("Handel ubraniami", LpMaximize)

Spodnie = pulp.LpVariable("Spodnie", lowBound=2, cat='Integer')
Koszulka = pulp.LpVariable("Koszulka", lowBound=4, cat='Integer')
Buty = pulp.LpVariable("Buty", lowBound=2, cat='Integer')
Bluza = pulp.LpVariable("Bluza", lowBound=2, cat='Integer')


problem += -(Spodnie * 80  + Koszulka * 35 + Buty * 70  + Bluza * 75)
problem += Spodnie + Koszulka + Buty + Bluza >= 15

problem.solve()

print("Optymalna liczba ubran w szafie:")
print("Spodnie:", Spodnie.varValue)
print("Koszulka:", Koszulka.varValue)
print("Buty:", Buty.varValue)
print("Bluza:", Bluza.varValue)
print(f"Ilosc wydanych pieniedzy: {pulp.value(problem.objective)}")