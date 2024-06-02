T = int(input())
while T != 0:
    T -= 1
    n, x, m = map(float, input().split())
    ans = 0
    while n < m:
        n = n + n*x/100
        ans += 1
    print(ans)