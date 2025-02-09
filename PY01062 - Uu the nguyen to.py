import math

def prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return n > 1

def check(s):
    s = str(s)
    n = len(s)
    countP = sum(1 for i in s if prime(int(i)))
    return prime(n) and countP > (n - countP)

test = int(input())
while test > 0:
    test -= 1
    n = input()
    print("YES" if check(n) else "NO")
