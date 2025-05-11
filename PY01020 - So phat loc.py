def check(n):
    x = str(n)
    y = x[-2:]
    return True if y == "86" else False
for _ in range(int(input())):
    n = int(input())
    print("YES" if check(n) else "NO")