def check(n):
    if len(set(n)) != 2:
        return False
    c = n[0]
    for i in range(2, len(n)):
        if n[i] != n[i-2]:
            return False
    return True

for _ in range(int(input())):
    n = input()
    print("YES" if check(n) else "NO")