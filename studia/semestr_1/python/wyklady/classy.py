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
