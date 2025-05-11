def check(x, y):
    i, j = len(x), 0
    while j < i:
        if x[j] > y[j]:
            return False
        j += 1
    return True

for _ in range(int(input())):
    n = int(input())
    a = map(int, input().split())  
    b = map(int, input().split())
    x, y = sorted(a), sorted(b)
    print("YES" if check(x, y) else "NO")
    