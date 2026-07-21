import math

def f1(x):
    return x**2

def calka_prostokatami(f, start, end, sample=20):
    #T = 0
    T = [[0]*(sample) for _ in range(sample)]
    distans = (end-start)
    for i in range(0, sample):
        pom_2_do_i = 2**i
        jump = distans/(pom_2_do_i)
        for z in range(pom_2_do_i):
            T[i][0] += (jump*1/2 * (f(start+((z)*jump)) + f(start+((z+1)*jump))))
    
    return (T[sample-1][0])

print(calka_prostokatami(f1, 0, 1, 6))


def miejca_zerowe_funkcji(f1,f2=lambda x:0,start = -100,end = 100,sample = 1/4):
    T = []
    distance = (end-start)
    for i in range(int(distance/sample)):
        step = start+(i*sample)
        #print(f1(step+sample)," ",f2(step))
        if (f1(step) > f2(step) and f1(step+sample) < f2(step+sample)):
            T.append(step+(1/2*sample))
        elif (f1(step) < f2(step) and f1(step+sample) > f2(step+sample)):            
            T.append(step+(1/2*sample))
        
    return T


def pole_pomiedzy_funkcjami(f1,f2,start = -100,end = 100,sample=1/4):
    field = 0
    tab = miejca_zerowe_funkcji(f1,f2,sample=sample)
    for i in range(len(tab)-1):
        field += calka_prostokatami(f1,tab[i],tab[i+1]) - calka_prostokatami(f2,tab[i],tab[i+1])
    return field

def f2(x):
    return x**2-3


def f3(x):
    return -x**2 +2


print(miejca_zerowe_funkcji(f2))

print(pole_pomiedzy_funkcjami(f3,f2,sample=1/32))



def fmcos(x):
    return x**2

def fpcos(x):
    return math.cos(x)

print(pole_pomiedzy_funkcjami(fpcos,fmcos,sample=1/36,start=-1,end=1))


def pochodna(f,x,sample=1/1000):
    start = f(x)
    end = f(x+sample)
    slope = (end-start)/sample
    return slope

print(pochodna(fmcos,8))

def dlugosc_luku(f,start = -10, end = 0-10):
    try:
        length = calka_prostokatami(math.sqrt(1+pochodna(f)**2))
        return length
    except BaseException:
        print("nie da sie policzyc")

print(dlugosc_luku(fmcos))