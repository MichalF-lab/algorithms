from pulp import *

problem = LpProblem("ile jakich ciastek", LpMaximize)

Przepis1 = LpVariable("przepis1", lowBound=0, cat='Integer')
Przepis2 = LpVariable("przepis2", lowBound=0, cat='Integer')

problem += Przepis1 * 30 + Przepis2 * 35
problem += Przepis1 * 250 + Przepis2 * 200 <= 2000
problem += Przepis1 * 200 + Przepis2 * 150 <= 1000
problem += Przepis1 * 100 + Przepis2 * 250 <= 1000

problem.solve()

print("Status:", LpStatus[problem.status])
print("Optymalna liczba paczek ciastek typu 1:", Przepis1.varValue)
print("Optymalna liczba paczek ciastek typu 2:", Przepis2.varValue)

print("Maksymalna wartość funkcji celu:", value(problem.objective))