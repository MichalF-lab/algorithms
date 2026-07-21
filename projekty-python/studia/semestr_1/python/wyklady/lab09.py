list = ["aaaaaaaa","l","kkkkk"]
list.remove("l")
#print(list)
#list.remove("aa")
print(list)

def naprzemian(x):
    while(True):
        yield -x+5
        yield x

f = naprzemian(10)
# print(f)

g = (x+2 for x in f)
for i in range(10):
    print(next(g))