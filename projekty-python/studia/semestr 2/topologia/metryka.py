import math
import numbers

def przestrzen_dyskretna(x,y):
    if (x==y): return 0
    return 1


def przestrzen_euklidesowa(x,y):
    if(type(x) != type(y)):
        print("input error",x," ",y)
        return 0
    if(isinstance(x,numbers.Number) and isinstance(y,numbers.Number)):
        return math.fabs(x-y)
    temp = 0
    for i in range(len(x)):
        try:
            temp += (x[i] - y[i])**2
        except BaseException:
            temp += (x[i])**2
    temp = math.sqrt(temp)
    return temp

def metryka_rzeka_R2(x,y):
    if(type(x) != type(y)):
        print("input error",x," ",y)
        return 0
    if(isinstance(x,numbers.Number) and isinstance(y,numbers.Number)):
        return math.fabs(x-y)
    
    if(x[0] == y[0]):
        return przestrzen_euklidesowa(x,y)
    
    return math.fabs(x[1]) + math.fabs(y[1]) + math.fabs(x[0] - y[0])
    #TODO narysować trójkąt
    

def metryka_rzeka_RN(x,y,N):
    if(type(x) != type(y)):
        print("input error",x," ",y)
        return 0
    if(isinstance(x,numbers.Number) and isinstance(y,numbers.Number)):
        return math.fabs(x-y)
    
    if(x[0] == y[0]):
        return przestrzen_euklidesowa(x,y)
    # temp = 0
    # for i in range(N):
    #     temp =
    # math.fabs(x[1]) + math.fabs(y[1]) + math.fabs(x[0] - y[0])
    # # TODO narysować trójkąt
    # TODO odleglosc punktu od prostej w dowolnym wymiarze



#szablon
def metryka(x,y):
    if(type(x) != type(y)):
        print("input error",x," ",y)
        return 0
    if(isinstance(x,numbers.Number) and isinstance(y,numbers.Number)):
        return math.fabs(x-y)
    temp = 0
    for i in range(len(x)):
        temp += (x[i] - y[i])**2
    temp = math.sqrt(temp)
    return temp

def metryka(x,y):
    if(type(x) != type(y)):
        print("input error",x," ",y)
        return 0
    if(isinstance(x,numbers.Number) and isinstance(y,numbers.Number)):
        return math.fabs(x-y)
    temp = 0
    for i in range(len(x)):
        temp += (x[i] - y[i])**2
    temp = math.sqrt(temp)
    return temp

print(przestrzen_euklidesowa(10,92),
      przestrzen_euklidesowa((12,2),(121,22)),
      )