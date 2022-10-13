# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def sumaWhile(inputt):
     i = 0
     sumaa = 0
     while inputt >= i:
         sumaa += i
         i+=1
     return sumaa

print(sumaWhile(5))

def sumaFor(inputt):
     sumaa = 0
     for i in range(inputt + 1):
         sumaa += i
     return sumaa
     
print(sumaFor(5))

def sumaRek(inputt):
    suma = 0
    if(inputt != 0):
        suma = inputt + sumaRek(inputt - 1)
    return suma

print(sumaRek(5))

def cFibbonaci(inputt,temp1 = 0,temp2 = 1):
    if(inputt == 0):
        return 0
    if(inputt == 1):
        return temp2
    temp3 = temp2 + temp1
    return cFibbonaci(inputt - 1,temp2,temp3)

print(cFibbonaci(40))


suma = 0

print( suma)