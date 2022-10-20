

# def suma_liczb_while(inputt):
#      i = 0
#      sumaa = 0
#      while inputt >= i:
#          sumaa += i
#          i+=1
#      return sumaa

# print(suma_liczb(5))

def suma_liczb(inputt):
     sumaa = 0
     for i in range(inputt + 1):
         sumaa += i
     return sumaa
     
# print(suma_liczb(5))

# def suma_liczb_rekurencyjnie(inputt):
#     suma = 0
#     if(inputt != 0):
#         suma = inputt + suma_liczb_rekurencyjnie(inputt - 1)
#     return suma

# print(suma_liczb_rekurencyjnie(5))
