def check(n):
    for i in range(len(n)-1):
        if ord(n[i]) > ord(n[i+1]):
            return False
    return True
for _ in range(int(input())):
    n = input()
    print("YES" if check(n) else "NO")