from math import *
t=int(input())
for i in range(t):
    n=input()
    cnt=len(n)-1
    n=int(n)
    l=1
    while l<=cnt:
        n/=pow(10,l)
        if n-int(n)>=0.5:
            n=ceil(n)
        else: n=int(n)
        n*=pow(10,l)
        l+=1
    print(int(n))