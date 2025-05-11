def to(a, b, s: str):
    return int(s.replace(str(a), str(b)))

for _ in range(int(input())):
    a, b = map(int, input().split())
    x1 = input().split()
    x2 = x1[1] if len(x1) > 1 else input()
    x1 = x1[0]
    print(to(max(a, b), min(a, b), x1) + to(max(a, b), min(a, b), x2),
          to(min(a, b), max(a, b), x1) + to(min(a, b), max(a, b), x2))
