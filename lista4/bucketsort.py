def bucketsort(tab, count1=10, __deep=-1):
    __deep += 1
    indextab = [[] for _ in range(count1)]
    temp = max(tab)

    for item in tab:
        index = int(item / (1 / temp)) % count1
        indextab[index].append(item)

    ext = []

    for bucket in indextab:
        if len(bucket) >= 2:
            # Sortuj kubełek wewnętrznie
            bucket.sort()
            ext.extend(bucketsort([x for x in bucket], count1, __deep))
        elif len(bucket) == 1:
            ext.append(bucket[0] / 10**__deep)

    return ext

# Przykład użycia
tablica = [0.12, 0.84, 0.45, 0.23, 0.67, 0.92, 0.34, 0.78, 0.56, 0.01]
wynik = bucketsort(tablica, count1=5)
print(wynik)
