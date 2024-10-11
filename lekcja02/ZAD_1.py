from pulp import *

problem = LpProblem("Zakup tokenow", LpMaximize)

pakiet_500 = pulp.LpVariable("Pakiet 500", lowBound=0, cat='Integer') # koszt 35
pakiet_250 = pulp.LpVariable("Pakiet 250", lowBound=0, cat='Integer') # koszt 18
pakiet_100 = pulp.LpVariable("Pakiet 100", lowBound=0, cat='Integer') # koszt 10

problem += 500 * pakiet_500 + 250 * pakiet_250 + 100 * pakiet_100
problem += 35 * pakiet_500 + 18 * pakiet_250 + 10 * pakiet_100 <= 200

problem.solve()

print(f"Pakiet 500: {pakiet_500.varValue}")
print(f"Pakiet 250: {pakiet_250.varValue}")
print(f"Pakiet 100: {pakiet_100.varValue}")

print(f"Ilosc kupionych tokenow: {pulp.value(problem.objective)}")
