import pulp

problem = pulp.LpProblem("Maksymalizacja_tekenow", pulp.LpMaximize)

pakiet_500 = pulp.LpVariable("Pakiet 500", lowBound=0, cat='Integer')
pakiet_100 = pulp.LpVariable("Pakiet 100", lowBound=0, cat='Integer')

problem += 500 * pakiet_500 + 100 * pakiet_100
problem += 35 * pakiet_500 + 10 * pakiet_100 <= 100
problem.solve()

print(f"Status: {pulp.LpStatus[problem.status]}")

print(f"Pakiet 500: {pakiet_500.varValue}")
print(f"Pakiet 100: {pakiet_100.varValue}")

print(f"Ilosc kupionych tokenow: {pulp.value(problem.objective)}")