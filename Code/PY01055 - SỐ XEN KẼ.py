def check(n):
    if len(n)%2==0: return False
    if a[0]==a[1]: return False
    for i in range(2,len(n),2):
        if a[i]!=a[0]: return False
    return True
t=int(input())
for test in range(t):
    a=list(map(int,input()))
    if check(a):
        print("YES")
    else:
        print("NO")