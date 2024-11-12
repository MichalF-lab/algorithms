from pulp import *

# Inicjalizacja problemu - maksymalizacja zysku
prob = LpProblem("Optymalizacja_Garderoby", LpMaximize)

# Definicja danych
items = ["Spodnie", "Koszulka", "Buty", "Bluza"]
current_state = {"Spodnie": 4, "Koszulka": 2, "Buty": 6, "Bluza": 5}
min_state = {"Spodnie": 2, "Koszulka": 4, "Buty": 2, "Bluza": 2}
buy_price = {"Spodnie": 80, "Koszulka": 35, "Buty": 70, "Bluza": 75}
sell_price = {"Spodnie": 60, "Koszulka": 30, "Buty": 60, "Bluza": 60}

#LpVariable.dicts(name, sequence, lowBound=None, upBound=None, cat='Continuous')
sell = LpVariable.dicts("sprzedaz", items, 0, None, LpInteger)
buy = LpVariable.dicts("zakup", items, 0, None, LpInteger)


prob += lpSum([sell[item] * sell_price[item] for item in items]) - lpSum([buy[item] * buy_price[item] for item in items])

for item in items:
    prob += current_state[item] - sell[item] + buy[item] >= min_state[item]

for item in items:
    prob += sell[item] <= current_state[item]

prob += lpSum([current_state[item] - sell[item] + buy[item] for item in items]) >= 15
prob.solve()



print(f"Status: {LpStatus[prob.status]}")
print(f"Optymalny zysk: {value(prob.objective):.2f} zł\n")

print("Wyniki:")
print("\nSprzedaż:")
for item in items:
    if value(sell[item]) > 0:
        print(f"{item}: {value(sell[item])} szt.")

print("\nZakup:")
for item in items:
    if value(buy[item]) > 0:
        print(f"{item}: {value(buy[item])} szt.")

print("\nStan końcowy:")
for item in items:
    final_state = current_state[item] - value(sell[item]) + value(buy[item])
    print(f"{item}: {final_state} szt.")

print(f"\nŁączna liczba elementów po transakcjach: {sum(current_state[item] - value(sell[item]) + value(buy[item]) for item in items)}")