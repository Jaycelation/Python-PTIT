def check(n):
    for i in range(0, len(n)-1):
        if n[i] > n[i+1]:
            return False
    return True
for _ in range(int(input())):
    n = input()
    print("YES" if check(n) else "NO")