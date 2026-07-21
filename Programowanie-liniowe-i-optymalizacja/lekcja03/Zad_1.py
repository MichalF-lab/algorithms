from pulp import *


problem = LpProblem("Zakup pudelek", LpMaximize)

pudelko_1 = pulp.LpVariable("pudelko 1", lowBound=0, cat='Integer')
pudelko_2 = pulp.LpVariable("pudelko 2", lowBound=0, cat='Integer')
pudelko_3 = pulp.LpVariable("pudelko 3", lowBound=0, cat='Integer')

problem += 22 * pudelko_1 + 13 * pudelko_2 + 17 * pudelko_3
problem += 22 * pudelko_1 + 13 * pudelko_2 + 17 * pudelko_3 <= 80

problem.solve()

print(f"pudelko 1: {pudelko_1.varValue}")
print(f"pudelko 2: {pudelko_2.varValue * 2}")
print(f"pudelko 3: {pudelko_3.varValue * 3}")


problem1 = LpProblem("Zakup pudelek", LpMaximize)

pudelko_1 = pulp.LpVariable("pudelko 1", lowBound=0, cat='Integer')
pudelko_2 = pulp.LpVariable("pudelko 2", lowBound=0, cat='Integer')
pudelko_3 = pulp.LpVariable("pudelko 3", lowBound=0, cat='Integer')

problem1 += 22 * pudelko_1 + 13 * pudelko_2 + 17 * pudelko_3
problem1 += 22 * pudelko_1 + 13 * pudelko_2 + 17 * pudelko_3 <= 60

problem1.solve()

print(f"pudelko 1: {pudelko_1.varValue}")
print(f"pudelko 2: {pudelko_2.varValue * 2}")
print(f"pudelko 3: {pudelko_3.varValue * 3}")

