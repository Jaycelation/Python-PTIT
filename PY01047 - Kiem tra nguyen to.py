def checkP(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def check(n):
    s = int(n[-4:])  
    return checkP(s)

for _ in range(int(input().strip())):
    n = input()
    print("YES" if check(n) else "NO")