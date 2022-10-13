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
        suma += inputt + sumaRek(inputt - 1)
    return suma

print(sumaRek(5))