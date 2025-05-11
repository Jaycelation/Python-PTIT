def check(s, w):
    a, b = int(s), int(w)
    import math
    return math.gcd(a, b) == 1

for _ in range(int(input())):
    s = input()
    w = s[::-1]
    print("YES" if check(s, w) else "NO")
