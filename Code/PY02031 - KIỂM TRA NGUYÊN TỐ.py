import math
def check(n):
    if n<2: return 0
    for i in range(2,math.isqrt(n)+1):
        if n%i==0:
            return 0
    return 1
n,m=map(int,input().split())
a=[]
for i in range(n):
    b=list(map(int,input().split()))
    b=[check(x) for x in b]
    a.append(b)
for i in range(n):
    for j in range(m):
        print(a[i][j],end=' ')
    print()