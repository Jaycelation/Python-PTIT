def check(n):
    for i in range(0,len(n)-2):
        if n[i]!=n[i+2] or n[i]==n[i+1]:
            return False
    return True
t=int(input())
for test in range(t):
    n=list(map(int,input()))
    if check(n):
        print("YES")
    else:
        print("NO")