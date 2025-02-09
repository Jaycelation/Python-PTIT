def checkP(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return n > 1
for _ in range(int(input())):
    n = input()
    val = 0
    for i in range(len(n)):
        val += int(n[i])
    print("YES" if checkP(val) else "NO")