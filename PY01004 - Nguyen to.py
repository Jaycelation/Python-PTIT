import math

def prime(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return n > 1

test = int(input())
while test:
    test -= 1
    n = int(input())
    count = 1
    for i in range(2, n):
        if math.gcd(i, n) == 1:
            count += 1
    if prime(count):
        print("YES")
    else:
        print("NO")