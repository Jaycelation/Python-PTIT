def check(n):
    for i in range(1000):
        if n%7==0:
            return n
        m=int(str(n)[::-1])
        n+=m
    return -1
t=int(input())
for test in range(t):
    n=int(input())
    print(check(n))