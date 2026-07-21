from pulp import *

problem = LpProblem("Maxincome", LpMaximize)

To = pulp.LpVariable(" Al", lowBound=0, cat='Integer') # koszt 35
Ku = pulp.LpVariable(" Go", lowBound=0, cat='Integer') # koszt 18
Po = pulp.LpVariable(" Kl", lowBound=0, cat='Integer') # koszt 18
Mo = pulp.LpVariable(" AG", lowBound=0, cat='Integer') # koszt 10

problem1 = 1 * To + Ku * (1/5) + Po
problem2 = 1 * To + Ku * (1/4) + Mo * (1 * 4) 
problem3 = Ku * (1/8) + Po + Mo * (1 * 4)
problem4 = 1 * To + Po + Mo * (1 * 4) 

#problem += 4 *To * 6.99 + 1 * Ku * 19.99 + 5 * Po * (5 * 3.5) + 0.5 * Mo * (3.99 * 4)
problem += problem1 + problem2 + problem3 + problem4
problem += Ku <= 1
problem += To <= 4
problem += Po <= 5
problem += Mo <= 4


problem.solve()

print(f" Tortille wykrzystane: {To.varValue}")
print(f" Kurczak wykrzystane: {Ku.varValue} kg")
print(f" Pomidor wykrzystane: {Po.varValue}")
print(f" Mozzarela wykrzystane: {Mo.varValue*0.125}")

print(f"Ilosc wydanych pieniedzy: {pulp.value(problem.objective)}")
