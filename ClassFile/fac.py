from math import sqrt
def factor(a):
    s=[]
    for i in range(1,a//2+2):
        if a%i==0:
            s.append(i)
    if a>2:
        s.append(a)
    while True:
        try:
            print(eval(input('>>> ')))
        except:
            break

def prime(n):
    d={}
    while n % 2== 0:
        n = n / 2
        try:
            d[2]+=1
        except:
            d[2]=1
    for i in range(3,int(sqrt(n))+1,2):
        while n % i== 0:
            n = n / i
            try:
                d[i]+=1
            except:
                d[i]=1
    if n > 2:
        d[n]=1
    return d

def largestPrimeFactor(n):
    while n % 2== 0:
        n = n / 2
    for i in range(3,int(sqrt(n))+1,2):
        while n % i== 0:
            n = n / i
            x = i
    if n > 2:
        x = n
    return int(x)
