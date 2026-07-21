def platon1():
    ext = []
    for i in range(1, 100):
        for j in range(i, 100):
            ext.append((i*j, i, j))
    return [item for item in ext if [x[0] for x in ext].count(item[0]) != 1]


def sokrates1(tab):
    ext = []
    for i in range(1, 100):
        for j in range(i, 100):
            ext.append((i+j, i, j))
    temp = (x[0] for x in ext)
    temp = [item for item in temp if [x for x in temp].count(item) > 1]
    for item in tab:
        if item[0] in temp:
            ext.remove(item)
    return ext


def platon2(tab):
    ext = []
    for i in range(1, 100):
        for j in range(i, 100):
            ext.append((i*j, i, j))

    ext2 = []
    for ij in range(1, 100*100):
        ext2.append(sum(1 for _, i, j in tab if ij in (_, i, j)))
    print((ext2))


    tab_coppy = [(i, j) for _, i, j in tab]
    ext3 = [(i, j) for _, i, j in ext]
    for i in range(1, 100*100):
        suma = 0
        for j  in ext:
            if j[0] == i:
                suma += 1
        try:    
            if suma == ext2[i]:
                for j  in ext3:
                    if j in tab_coppy:
                        return j
        except:
            continue



ext = []
for i in range(1, 100):
    for j in range(i, 100):
        ext.append((i, j))

pairs1 = platon1()
#print(pairs1) # opcje dla platona
pairs2 = sokrates1(pairs1)
#print(pairs2) # opcje dla sokratesa
pairs3 = platon2(pairs2)
print(pairs3)
