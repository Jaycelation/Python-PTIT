import math
def prime(n):
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return n > 1

test = int(input())
while test:
    test -= 1
    n = input()
    s = n[:3]
    w = n[-3:]
    print("YES" if prime(int(s)) and prime(int(w)) else "NO")