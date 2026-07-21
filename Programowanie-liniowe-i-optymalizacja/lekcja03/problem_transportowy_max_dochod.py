from pulp import *

problem = LpProblem("Maxincome", LpMaximize)

Al = pulp.LpVariable(" Al", lowBound=0, cat='Integer') # koszt 35
Go = pulp.LpVariable(" Go", lowBound=0, cat='Integer') # koszt 18
Kl = pulp.LpVariable(" Kl", lowBound=0, cat='Integer') # koszt 18
AG = pulp.LpVariable(" AG", lowBound=0, cat='Integer') # koszt 10
AK = pulp.LpVariable(" AK", lowBound=0, cat='Integer') # koszt 10
GK = pulp.LpVariable(" GK", lowBound=0, cat='Integer') # koszt 10

problem += Al * 50 + Go * 75 + Kl * 100 + AG * 80 + AK * 125 + GK * 150
problem += Al + Go + Kl + AG + AK + GK <= 20
problem += Al + AG + AK == 10
problem += Go + AG + GK == 8
problem += Kl + AK + GK == 15


problem.solve()

print(f" Al: {Al.varValue}")
print(f" Go: {Go.varValue}")
print(f" Kl: {Kl.varValue}")
print(f" AG: {AG.varValue}")
print(f" AK: {AK.varValue}")
print(f" GK: {GK.varValue}")

print(f"Ilosc kupionych tokenow: {pulp.value(problem.objective)}")
