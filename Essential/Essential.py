import math

def prime(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return n > 1

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

def is_palindrome(n):
    return str(n) == str(n)[::-1]
