def calc(n):
    val = str(n)
    return sum(int(c) for c in val if c.isdigit())
def check(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return n > 1
for _ in range(int(input())):
    arr = list(map(int, input().split()))
    a, b = arr[0], arr[1]
    import math
    c = math.gcd(a, b)
    print("YES" if check(calc(c)) else "NO")