import random
import numpy
import time

# main_table = numpy.arange(random.randint(5,7))

# for item in main_table:
#     main_table[item] = float(random.randint(1,100))

def bucketsort(tab,count1 = 10):
    indextab = [[] for _ in range(count1)]
    distance = float(max(tab)) - float(min(tab))
    for item in tab:
        j = 0
        for i in numpy.arange(float(min(tab)),float(max(tab)),distance/count1):
            # print(i)
            if(item <= i):
                indextab[j].append(item)
                break
            j+=1
        # indextab[(int(item / (temp))) % count1].append(item)
    ext = []
    for bucket in indextab:
        #print(bucket)
        if (all(element == bucket[0] for element in bucket) and len(bucket) >= 2): 
            ext.extend(bucket)
        elif len(bucket) >= 2:
            ext.extend(bucketsort(bucket, count1))
        elif len(bucket) == 1:    
            ext.append(bucket[0])
    return ext


print(bucketsort([0.9,0.2,0.34,0.22,0.9,0.0011,0.2112,0.31111],10))

def radixsort(tab, base = 10):

    def countingsort(tab,step):
        nonlocal base
        indextab = [0 for _ in range(base)]
        for item in tab: indextab[int(str(item % step)[0])] += 1

        for i in range(1, base):
            indextab[i] += indextab[i - 1]
        #print(indextab)
        ext = tab[:]
        
        for item in tab[::-1]:
            index = int(str(item % (step))[0])
            #print(item," ",index," ",indextab[index])
            ext[indextab[index] - 1] = item
            indextab[index] -= 1

        return ext[:]
    
    sup = max(tab)
    i = 10
    temp = tab[:]
    while True:
        temp = countingsort(temp,i)
        if(i > sup): break
        i *= 10
    return temp


#print(radixsort([16,22,11,22,32,21,22,23,14,24],7))

if __name__ == 'main':

    def test_sortowania(algorytm, tablica, nazwa_algorytmu):
        start_time = time.time()
        algorytm(tablica)
        end_time = time.time()
        print(f"{nazwa_algorytmu}: {end_time - start_time:.6f} sekundy")

    def testy_sortowania():
        rozmiar_tablicy = 10000
        zakres_liczb = 100000

        tablica_do_posortowania = [random.randint(0, zakres_liczb) for _ in range(rozmiar_tablicy)]
        
        print("Testy dla bubblesort:")
        test_sortowania(bubblesort, tablica_do_posortowania.copy(), "Bubblesort")

        print("\nTesty dla mergesort:")
        test_sortowania(mergesort, tablica_do_posortowania.copy(), "Mergesort")

        print("\nTesty dla bucketsort:")
        test_sortowania(bucketsort, tablica_do_posortowania.copy(), "Bucketsort")

        print("\nTesty dla radixsort:")
        test_sortowania(radixsort, tablica_do_posortowania.copy(), "Radixsort")

    testy_sortowania()
