import math
def nto(n):
    for i in range(2,math.isqrt(n)+1):
        if n%i==0:
            return False
    return n>1
def check(n):
    for i in range(len(n)):
        if nto(i):
            if not nto(n[i]): return False
        else:
            if nto(n[i]): return False
    return True
t=int(input())
for test in range(t):
    n=list(map(int,input()))
    if check(n):
        print("YES")
    else:
        print("NO")