import math
def check(a,b):
    for i in range(1,len(a)):
        if abs(ord(a[i])-ord(a[i-1]))!=abs(ord(b[i])-ord(b[i-1])):
            return False
    return True
t=int(input())
for test in range(t):
    n=input()
    m=n[::-1]
    if check(n,m):
        print("YES")
    else:
        print("NO")