import time
import random
import matplotlib.pyplot as plt
from functools import partial

# Funkcje sortujące

def heapsort(arr):
    comparisons, assignments = 0, 0

    def heapify(arr, n, i):
        nonlocal comparisons, assignments
        largest = i
        left = 3 * i + 1
        middle = 3 * i + 2
        right = 3 * i + 3

        if left < n and arr[i] < arr[left]:
            comparisons += 1
            largest = left

        if middle < n and arr[largest] < arr[middle]:
            comparisons += 1
            largest = middle

        if right < n and arr[largest] < arr[right]:
            comparisons += 1
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            assignments += 3  # swap requires 3 assignments
            heapify(arr, n, largest)

    n = len(arr)
    for i in range(n // 3 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        assignments += 3  # swap requires 3 assignments
        heapify(arr, i, 0)

    return comparisons, assignments

# Funkcje pomocnicze

def generate_random_data(size):
    return [random.randint(1, 1000) for _ in range(size)]

def measure_time(func, data):
    start_time = time.time()
    func(data)
    end_time = time.time()
    return end_time - start_time

def measure_algorithm(algorithm, sizes):
    times = []
    comparisons = []
    assignments = []

    for size in sizes:
        data = generate_random_data(size)

        time_taken = measure_time(algorithm, data.copy())
        times.append(time_taken)

        comp, assign = algorithm(data)
        comparisons.append(comp)
        assignments.append(assign)

    return times, comparisons, assignments

# Testy i generowanie wykresów

sizes = [100, 500, 1000, 2000, 5000]
heapsort_times, heapsort_comparisons, heapsort_assignments = measure_algorithm(heapsort, sizes)

# Wykresy

plt.figure(figsize=(12, 4))

plt.subplot(1, 3, 1)
plt.plot(sizes, heapsort_times, marker='o')
plt.title('Heapsort - Czas wykonania')
plt.xlabel('Rozmiar danych')
plt.ylabel('Czas (s)')

plt.subplot(1, 3, 2)
plt.plot(sizes, heapsort_comparisons, marker='o', label='Porównania')
plt.plot(sizes, heapsort_assignments, marker='o', label='Przypisania')
plt.title('Heapsort - Porównania i przypisania')
plt.xlabel('Rozmiar danych')
plt.ylabel('Liczba operacji')
plt.legend()

plt.tight_layout()
plt.savefig('heapsort_analysis.pdf')
plt.show()
