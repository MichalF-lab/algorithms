class jakas:
    atrybut = 0

a = jakas()
a.atrybut = 10

b = jakas()
print(b.atrybut)

jakas.atrybut = 10

print(b.atrybut)

class jakas2:
    atrybut = 0

    def __init__(self,x):
        print(x)
        print(self.atrybut)
        self.atrytybut = 50
        print(self.atrytybut)

    @classmethod
    def anonim(cls):
        cls.atrybut += 100
        return cls("nwm co to")

c = jakas2.anonim()
print(c.atrybut)
d = jakas2(10)
print(d.atrybut)


# class ccc:

#     def promien(self):
#         pass
#     @promien.setter
#     def promien(self,r):
#         pass

# obiekt = ccc()
# obiekt.promien = 10

# class A:
#     @classmethod
#     def nazwa():
#         print("Hello World")

# A.nazwa()
# a = A()

# class A:
#     def __init__(self, x):
#         self.x = 2*x

#     @property
#     def x(self):
#         return self._x

#     @x.setter
#     def x(self, x):
#         self._x = 3*x

# a = A(10)
# print(a.x)

class A:
    def __init__(self):
        self.x = 42

a = A()
a.x = 7
print(A.x)