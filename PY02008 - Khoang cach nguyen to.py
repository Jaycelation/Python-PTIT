import math
def sieve(n):
    if n < 2:
        return []
    primes = [True] * (n+1)
    primes[0] = primes[1] = False
    for i in range(2, int(math.sqrt(n)+1)):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
    return [i for i, is_prime in enumerate(primes) if is_prime]

primes = sieve(8000)
arr = list(map(int, input().split()))
n, x = arr[0], arr[1]
ans = []
ans.append(x)
for i in range(n):
    x = primes[i] + x
    ans.append(x)

for i in ans:
    print(i, end=" ")