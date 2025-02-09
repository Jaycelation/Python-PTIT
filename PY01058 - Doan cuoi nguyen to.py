def checkPrime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return n > 1

for test in range(int(input())):
    n = input()
    s = n[-4:]
    print("YES" if checkPrime(int(s)) else "NO")