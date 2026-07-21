from pulp import *

problem = LpProblem("Najtansze zakupy", LpMinimize)

# Kupujacy
Student1A = LpVariable("Student1A", lowBound=0, cat='Integer')
Student2A = LpVariable("Student2A", lowBound=0, cat='Integer')
Student3A = LpVariable("Student3A", lowBound=0, cat='Integer')
Student4A = LpVariable("Student4A", lowBound=0, cat='Integer')

Student1B = LpVariable("Student1B", lowBound=0, cat='Integer')
Student2B = LpVariable("Student2B", lowBound=0, cat='Integer')
Student3B = LpVariable("Student3B", lowBound=0, cat='Integer')
Student4B = LpVariable("Student4B", lowBound=0, cat='Integer')

Student1C = LpVariable("Student1C", lowBound=0, cat='Integer')
Student2C = LpVariable("Student2C", lowBound=0, cat='Integer')
Student3C = LpVariable("Student3C", lowBound=0, cat='Integer')
Student4C = LpVariable("Student4C", lowBound=0, cat='Integer')

Student1D = LpVariable("Student1D", lowBound=0, cat='Integer')
Student2D = LpVariable("Student2D", lowBound=0, cat='Integer')
Student3D = LpVariable("Student3D", lowBound=0, cat='Integer')
Student4D = LpVariable("Student4D", lowBound=0, cat='Integer')

problem += (Student1A * 15 + Student1B * 10 + Student1C * 10 + Student1D * 15) 
+ (Student2A * 15 + Student2B * 20 + Student2C * 15 + Student2D * 10)
+ (Student3A * 20 + Student3B * 15 + Student3C * 15 + Student3D * 10)
+ (Student4A * 10 + Student4B * 15 + Student4C * 20 + Student4D * 15)

problem += Student1A + Student1B + Student1C + Student1D == 6
problem += Student2A + Student2B + Student2C + Student2D == 6
problem += Student3A + Student3B + Student3C + Student3D == 6
problem += Student4A + Student4B + Student4C + Student4D == 6

problem += Student1A + Student2A + Student3A + Student4A == 5
problem += Student1B + Student2B + Student3B + Student4B == 6
problem += Student1C + Student2C + Student3C + Student4C == 8
problem += Student1D + Student2D + Student3D + Student4D == 5

problem.solve()



# Zdefiniuj zmienne decyzyjne dla każdego studenta i sklepu
studenci = ['Student1', 'Student2', 'Student3', 'Student4']
przedmioty = ['A', 'B', 'C', 'D']

# Macierz cen
ceny = {
    'Student1': {'A': 15, 'B': 10, 'C': 10, 'D': 15},
    'Student2': {'A': 15, 'B': 20, 'C': 15, 'D': 10},
    'Student3': {'A': 20, 'B': 15, 'C': 15, 'D': 10},
    'Student4': {'A': 10, 'B': 15, 'C': 20, 'D': 15}
}

# Słownik zmiennych
zmienne = {}
for student in studenci:
    for przedmiot in przedmioty:
        zmienna = LpVariable(f"{student}_{przedmiot}", lowBound=0, cat='Integer')
        zmienne[(student, przedmiot)] = zmienna

# Funkcja celu - minimalizacja całkowitego kosztu
problem += lpSum([
    zmienne[(student, sklep)] * ceny[student][sklep] 
    for student in studenci 
    for sklep in przedmioty
])

# Ograniczenia - każdy student kupuje dokładnie 6 produktów
for student in studenci:
    problem += lpSum([zmienne[(student, sklep)] for sklep in przedmioty]) == 6

# Rozwiązanie problemu
problem.solve()

print("Minimalna wartość funkcji celu:", value(problem.objective))
print("Student1",Student1A.varValue,Student1B.varValue,Student1C.varValue,Student1D.varValue)
print("Student1",Student2A.varValue,Student2B.varValue,Student2C.varValue,Student2D.varValue)
print("Student1",Student3A.varValue,Student3B.varValue,Student3C.varValue,Student3D.varValue)
print("Student1",Student4A.varValue,Student4B.varValue,Student4C.varValue,Student4D.varValue)