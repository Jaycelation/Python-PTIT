import math

def sieve(n):
    is_prime = [True] * (n+1)
    is_prime[0] = is_prime[1] = False

    primes = []
    for i in range(2, n+1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return primes

def check(n):
    limit = int(math.sqrt(n))
    primes = sieve(limit)
    count = 0

    #Dạng 1: p^8
    for p in primes:
        if p**8 > n:
            break
        count += 1
    
    #Dạng 2: p1^2 * p2^2
    num_primes = len(primes)
    for i in range(num_primes):
        for j in range(i+1, num_primes):
            if primes[i]**2 * primes[j]**2 > n:
                break
            count += 1

    return count

n = int(input())
print(check(n))