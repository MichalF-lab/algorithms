# para = (3,5,44,"cos")
# print(para * 3) # 3,5,44,"cos" 3,5,44,"cos" 3,5,44,"cos"
# print(len(para)) # 4

# x = 2021
# y = 2021
# z = x is y
# print(z) # teoretycznie false

# () # to jest pusta ktotka
# (1) # to nie jest krotka
# (1,) # to jest krotka jednoelementowa

import sys
x = 2021
y = 2021
print(sys.getrefcount(x)-1) # 1 teoretycznie bo w praktyce 4
print(sys.getrefcount(y)-1) # 1 teoretycznie bo w praktyce 4

xx = 2021
yy = 20213
print(sys.getrefcount(xx)-1) # 2 teoretycznie bo w praktyce 5
print(sys.getrefcount(yy)-1) # 1 teoretycznie bo w praktyce 3
