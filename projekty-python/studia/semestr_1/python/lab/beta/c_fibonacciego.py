
def c_fibonacciego(inputt,temp1 = 0,temp2 = 1):
    if(inputt == 0):
        return 0
    if(inputt == 1):
        return temp2
    temp3 = temp2 + temp1
    return c_fibonacciego(inputt - 1,temp2,temp3)

# print(c_fibonacciego(40))

# def tajemnicza_funkcja(x):
#     if x:
#         return x * tajemnicza_funkcja(x-1)
#     else:
#         return 1

# print(tajemnicza_funkcja(6))