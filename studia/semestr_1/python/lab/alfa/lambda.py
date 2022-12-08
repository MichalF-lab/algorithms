temp1 = lambda x: x+1
# print(temp1(8))

temp2 = lambda x,y: x*y
# print(temp2(12,11))

# funkcja wyższego rzędu
    
def funkcja(f,liczba):
    return f(liczba)

# print(funkcja(lambda x: x+1, 7))
# print(funkcja(lambda x: x*x, 7))

tab1 = [1,2,4,56,7,2334,6,8532,5,32135]

def sort1(tab):
    tab.sort()

tab2 = lambda tab: tab.sort1()

print(tab2(tab1))