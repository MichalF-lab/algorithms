lista1 = [22,331,321,42354,36,67,8,7869,2,33,3]
# # kopijuemy liste co kosztuje
# def minimum(lista):
#     if lista:
#         kandydat = lista[0]
#         for element in lista[1:]:
#             if element < kandydat:
#                 kandydat = element
#         return kandydat

# print(minimum(lista1))

# def minimum3(lista):
#     if lista:
#         lista = iter(lista)
#         kandydat = next(lista)
#         for element in lista:
#             if element > kandydat:
#                 kandydat = element
#         return kandydat


# def bisekcja(f,a,b,tol=1e-6):
#     c = (a+b)/2
#     pol_dlugosci = (b-a)/2
#     if pol_dlugosci < tol: return c
#     f_a=f(a)
#     while pol_dlugosci > tol:
#         f_c=f(c)
#         if (f_a*f_c < 0): b = c
#         elif(f_a*f_c > 0):
#             a = c
#             f_a = f_c
#         else: return c
#         pol_dlugosci/=2
#         c = (a+b)/2
#     return c

# def fun_kwadratowa(x):
#     return (x**x-10)

# print(bisekcja(fun_kwadratowa,0,10))

def tajemnicza_funkcja(lista):
	if lista:
		kandydat = lista[0]
		for element in lista:
			if element < kandydat:
				kandydat = element
		return kandydat

print(tajemnicza_funkcja(lista1))