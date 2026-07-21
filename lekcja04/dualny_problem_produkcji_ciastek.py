from pulp import *

problem = LpProblem("problem_dualny", LpMinimize)

Maka = LpVariable("Maka", lowBound=0)
Maslo = LpVariable("Maslo", lowBound=0)
Cukier = LpVariable("Cukier", lowBound=0)


problem += 2000 * Maka + 1000 * Maslo + 1000 * Cukier

problem += (250 * Maka + 200 * Maslo + 100 * Cukier) >= 30 
problem += (200 * Maka + 150 * Maslo + 250 * Cukier) >= 35 

problem.solve()

print("Status:", LpStatus[problem.status])
print("Minimalna wartość funkcji celu:", value(problem.objective))