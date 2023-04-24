import random

class ciagi:
    def __init__(self,f) -> None:
        self.f = f
    
    def zbieznosc(self):
        try:
            temp = []
            sample = random.randint(300,500)
            # n z definicji
            n = random.randint(1000,2000)
            for i in range(sample):
                temp.append(f(n+i))
            # epsilon
            # n nalezace do N
            return temp
        except BaseException:
            print("rozbiezna")
class szeregi(ciagi):
    pass
def f(x):
    return x
a = ciagi(f)
print(a.zbieznosc())