import matplotlib.pyplot as plt
import numpy as np
import time

# Funkcje sortujące
import random
import numpy
import time

# Przygotowanie tablic do testów

main_table = numpy.arange(random.randint(5,7))

for item in main_table:
    main_table[item] = float(random.randint(1,100))

#main_table = [37,18,45,50,28,80]


def quicksort(tab):

    if (len(tab) <= 1 ): return tab
    
    a = tab[-1]
    ltab, rtab = [], []

    for item in tab[:-1]:
        if (item <= a): ltab.append(item)
        if (item > a): rtab.append(item)

    ltab = quicksort(ltab)
    rtab = quicksort(rtab)

    ext = []
    if ltab:
        ext.extend(ltab)
    ext.append(a)
    if rtab:
        ext.extend(rtab)
        
    return ext

def quicksort_plus(tab):
    
    count_e, count_p = 0,0

    def quicksortp(tab):

        nonlocal count_e, count_p

        if (len(tab) <= 1 ): return tab

        a = tab[-1]
        count_p += 1
        ltab, rtab = [], []

        for item in tab[:-1]:
            if (item <= a): ltab.append(item)
            if (item > a): rtab.append(item)
            count_e += 1
            count_p += 1

        ltab = quicksort(ltab)
        rtab = quicksort(rtab)

        ext = []
        if ltab:
            ext.extend(ltab)
            count_p += 1
        ext.append(a)
        count_p += 1
        if rtab:
            ext.extend(rtab)
            count_p += 1
            
        return ext

    quicksortp(tab)
    return count_e, count_p

#---------------------------------------------------------------------------------


def quicksort3(tab):

    if (len(tab) <= 1 ): return tab
    if (len(tab) == 2 ):
        if (tab[0] < tab[1]): return tab
        return [tab[1],tab[0]]
    
    a = tab[-1]
    b = tab[-2]
    if (a > b): a,b = b,a

    ltab,mtab, rtab = [], [], []

    for item in tab[:-2]:
        if (item <= a): ltab.append(item)
        elif (item > b): rtab.append(item)
        else: mtab.append(item)

    ltab = quicksort3(ltab)
    mtab = quicksort3(mtab)
    rtab = quicksort3(rtab)

    ext = []
    if ltab:
        ext.extend(ltab)
    ext.append(a)
    if mtab:
        ext.extend(mtab)
    ext.append(b)
    if rtab:
        ext.extend(rtab)
        
    return ext


def quicksort3_plus(tab):
    
    count_e, count_p = 0,0

    def quicksort3p(tab):

        nonlocal count_e, count_p

        if (len(tab) <= 1 ): 
            return tab
        if (len(tab) == 2 ):
            count_e += 1
            if (tab[0] < tab[1]): return tab
            return [tab[1],tab[0]]
        
        a = tab[-1]
        b = tab[-2]
        count_p += 2

        if (a > b):
            a,b = b,a
            count_e +=2

        ltab,mtab, rtab = [], [], []

        for item in tab[:-2]:
            count_e += 1
            if (item <= a): 
                ltab.append(item)
            elif (item > b):
                rtab.append(item)
                count_e +=1
            else: mtab.append(item)
            count_p += 1

        ltab = quicksort3p(ltab)
        mtab = quicksort3p(mtab)
        rtab = quicksort3p(rtab)

        ext = []
        if ltab:
            ext.extend(ltab)
            count_p += 1
        ext.append(a)
        count_p += 1
        if mtab:
            ext.extend(mtab)
            count_p += 1
        ext.append(b)
        count_p += 1
        if rtab:
            ext.extend(rtab)
            count_p += 1
            
        return ext
    
    quicksort3p(tab)
    return count_e, count_p

#--------------------------------------------------------------------------------
def heapsort(tab):

    if (len(tab) <= 1 ): return tab

    def sort_the_heap(heap,root,lenght):
        left = 2 * root + 1
        if left > lenght : return heap
        right = 2 * root + 2

        if heap[left] > heap[root]:
            heap[left], heap[root] = heap[root], heap[left]
        
        if right > lenght : return heap

        if heap[right] > heap[root] and heap[right] > heap[left]:
            heap[right], heap[root] = heap[root], heap[right] 



    def sort_whole_heap(tab,N):
        for i in range(N, -1, -1):
            sort_the_heap(tab, i, N)

    for i in range(len(tab)-1, 0, -1):
        sort_whole_heap(tab, i)
        tab[i], tab[0] = tab[0], tab[i]

    return tab



def heapsort_plus(tab):
    count_e, count_p = 0,0

    def heapsortp(tab):
        nonlocal count_e, count_p
        if (len(tab) <= 1 ): return tab

        def sort_the_heap(heap,root,lenght):
            nonlocal count_e, count_p

            left = 2 * root + 1
            if left > lenght : return heap
            count_e += 1
            if heap[left] > heap[root]:
                heap[left], heap[root] = heap[root], heap[left]
                count_p += 2

            right = 2 * root + 2
            if right > lenght : return heap
            count_e += 1
            if heap[right] > heap[root] and heap[right] > heap[left]:
                heap[right], heap[root] = heap[root], heap[right]
                count_p += 2



        def sort_whole_heap(tab,N):
            for i in range(N, -1, -1):
                sort_the_heap(tab, i, N)

        for i in range(len(tab)-1, 0, -1):
            sort_whole_heap(tab, i)
            tab[i], tab[0] = tab[0], tab[i]
            count_p += 2

        return tab

    heapsortp(tab)
    return count_e, count_p

#---------------------------------------------------------------------------------
def heapsort3(tab):

    if (len(tab) <= 1 ): return tab

    def sort_the_heap3(heap,root,lenght):
        left = 3 * root + 1
        if left > lenght : return heap

        if heap[left] > heap[root]:
            heap[left], heap[root] = heap[root], heap[left]
        
        mid = 3 * root + 2
        if mid > lenght : return heap

        if heap[mid] > heap[root] and heap[mid] > heap[left]:
            heap[mid], heap[root] = heap[root], heap[mid] 

        right = 3 * root + 3
        if right > lenght : return heap

        if heap[right] > heap[root] and heap[right] > heap[left]:
            heap[right], heap[root] = heap[root], heap[right] 

    def sort_whole_heap3(tab,N):
        for i in range(N, -1, -1):
            sort_the_heap3(tab, i, N)

    for i in range(len(tab)-1, 0, -1):
        sort_whole_heap3(tab, i)
        tab[i], tab[0] = tab[0], tab[i]

    return tab

def heapsort3_plus(tab):
    count_e, count_p = 0,0

    def heapsort3(tab):
        nonlocal count_e, count_p
        if (len(tab) <= 1 ): return tab

        def sort_the_heap3(heap,root,lenght):
            nonlocal count_e, count_p

            left = 3 * root + 1
            if left > lenght : return heap

            count_p += 1
            if heap[left] > heap[root]:
                heap[left], heap[root] = heap[root], heap[left]
                count_e += 2
            
            mid = 3 * root + 2
            if mid > lenght : return heap

            count_p += 1
            if heap[mid] > heap[root] and heap[mid] > heap[left]:
                heap[mid], heap[root] = heap[root], heap[mid]
                count_e += 2

            right = 3 * root + 3
            if right > lenght : return heap

            count_p += 1
            if heap[right] > heap[root] and heap[right] > heap[left]:
                heap[right], heap[root] = heap[root], heap[right] 
                count_e += 2

        def sort_whole_heap3(tab,N):
            for i in range(N, -1, -1):
                sort_the_heap3(tab, i, N)

        for i in range(len(tab)-1, 0, -1):
            sort_whole_heap3(tab, i)
            tab[i], tab[0] = tab[0], tab[i]
            count_e += 2

        return tab

    heapsort3(tab)
    return count_e, count_p
#-------------------------------------------------------------------------

# if __name__ == '__main__':
#     a = 10
#     # print(main_table)
#     print(quicksort3_plus(main_table))
#     print(main_table)
#     print(heapsort3_plus(main_table))
#     print(heapsort_plus(main_table))
#     print(quicksort3(main_table) == heapsort3(main_table))

def generate_random_data(size):
    return [float(random.randint(1, 100)) for _ in range(size)]

def measure_algorithm(algorithm, sizes):
    times = []
    comparisons = []
    assignments = []

    for size in sizes:
        data = generate_random_data(size)

        start_time = time.time()
        algorithm(data.copy())
        end_time = time.time()
        times.append(end_time - start_time)

        comp, assign = algorithm(data)
        comparisons.append(comp)
        assignments.append(assign)

    return times, comparisons, assignments

# Testy

sizes = [100, 500, 1000, 2000, 5000]

heapsort3_times, heapsort3_comparisons, heapsort3_assignments = measure_algorithm(heapsort3, sizes)
heapsort3_plus_times, heapsort3_plus_comparisons, heapsort3_plus_assignments = measure_algorithm(heapsort3_plus, sizes)
heapsort_plus_times, heapsort_plus_comparisons, heapsort_plus_assignments = measure_algorithm(heapsort_plus, sizes)
quicksort3_plus_times, quicksort3_plus_comparisons, quicksort3_plus_assignments = measure_algorithm(quicksort3_plus, sizes)

# Wykresy

plt.figure(figsize=(15, 10))

# Czas wykonania
plt.subplot(3, 1, 1)
plt.plot(sizes, heapsort3_times, marker='o', label='heapsort3')
plt.plot(sizes, heapsort3_plus_times, marker='o', label='heapsort3_plus')
plt.plot(sizes, heapsort_plus_times, marker='o', label='heapsort_plus')
plt.plot(sizes, quicksort3_plus_times, marker='o', label='quicksort3_plus')
plt.title('Czas wykonania')
plt.xlabel('Rozmiar danych')
plt.ylabel('Czas (s)')
plt.legend()

# Liczba porównań
plt.subplot(3, 1, 2)
plt.plot(sizes, heapsort3_comparisons, marker='o', label='heapsort3')
plt.plot(sizes, heapsort3_plus_comparisons, marker='o', label='heapsort3_plus')
plt.plot(sizes, heapsort_plus_comparisons, marker='o', label='heapsort_plus')
plt.plot(sizes, quicksort3_plus_comparisons, marker='o', label='quicksort3_plus')
plt.title('Liczba porównań')
plt.xlabel('Rozmiar danych')
plt.ylabel('Liczba porównań')
plt.legend()

# Liczba przypisań
plt.subplot(3, 1, 3)
plt.plot(sizes, heapsort3_assignments, marker='o', label='heapsort3')
plt.plot(sizes, heapsort3_plus_assignments, marker='o', label='heapsort3_plus')
plt.plot(sizes, heapsort_plus_assignments, marker='o', label='heapsort_plus')
plt.plot(sizes, quicksort3_plus_assignments, marker='o', label='quicksort3_plus')
plt.title('Liczba przypisań')
plt.xlabel('Rozmiar danych')
plt.ylabel('Liczba przypisań')
plt.legend()

plt.tight_layout()
plt.savefig('sorting_algorithms_analysis.pdf')
plt.show()
