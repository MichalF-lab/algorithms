class A1():
    def __init__(self):
        pass

class B1(A1):
    def __init__(self):
        pass

class C1(B1):
    def __init__(self):
        pass


# class C1(B1,A1):
#     def __init__(self):
#         pass
# class C1(A1,B1):
#     def __init__(self):
#         pass
# tu sa błedy

class F: pass
class E: pass
class D: pass
class C(D, F): pass
class B(D, E): pass
class A(B, C): pass

# to działa

class sup1:
    def __init__(self):
        print("1")


class sup2:
    def __init__(self):
        print("2")

class sup3(sup2):
    def __init__(self):
        print("3")
        super().__init__()


class sup4(sup1,sup3):
    def __init__(self):
        super().__init__()
        print("4")

# a = sup4()
# wypisze 1 4

class sup5(sup3,sup1):
    def __init__(self):
        super().__init__()
        print("5")

b = sup5()
# wypisze 3 1 2 5

print(b.__str__())