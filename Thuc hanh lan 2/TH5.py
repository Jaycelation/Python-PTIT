MAXN = 200005
bit = [0] * MAXN
ans = 0

def getS(x):
    s = 0
    while x > 0:
        s += bit[x]
        x -= x & -x
    return s

def update(x, val):
    while x < MAXN:
        bit[x] += val
        x += x & -x

n = int(input())
a = [0] + list(map(int, input().split()))

for i in range(n, 0, -1):
    ans += getS(a[i] - 1)
    update(a[i], 1)

print(ans)