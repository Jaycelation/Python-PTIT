class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.bit = [0] * (size + 1)

    def get_sum(self, x):
        s = 0
        while x <= self.size:
            s += self.bit[x]
            x += x & -x
        return s

    def update(self, x, val):
        while x > 0:
            self.bit[x] += val
            x -= x & -x

n = int(input())
a = list(map(int, input().split()))

MAXN = 200005
bit = FenwickTree(MAXN)
ans = 0

for i in range(n):
    bit.update(a[i], 1)
    ans += bit.get_sum(a[i] + 1)

print(ans)