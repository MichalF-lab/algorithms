
def fi():
    a=[]
    b=int(input())
    a.append(0)
    a.append(1)
    for i in range (b):
        a.append(a[i+1]+a[i])
    a.reverse()
    print(a[1])


fi()