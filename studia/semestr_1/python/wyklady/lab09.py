list = ["aaaaaaaa","l","kkkkk"]
list.remove("l")
#print(list)
list.remove("aa")
print(list)

def naprzemian(x):
    while(True):
        yield -x
        yield x

f = naprzemian(10)

g = (x+1 for x in f)
print(g)
print(next(g))