import math

def sieve(n, prime):
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            i = p * 2
            while (i <= n):
                prime[i] = False
                i = i + p
        p = p + 1

for _ in range(int(input())):
    n = int(input())
    prime = [True] * (n+1)
    sieve(n, prime)
    count = 0
    for i in range(2, n-6+1):
        if (prime[i] and prime[i+2] and prime[i+6]):
            count += 1
        elif (prime[i] and prime[i+4] and prime[i+6]):
            count += 1

    print(count)