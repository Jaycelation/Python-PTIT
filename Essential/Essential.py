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

def normalize_name(name):
    words  = name.strip().split()
    result = " ".join(word.capitalize() for word in words)
    return result

def base_conversion(a, b):
    if a == 0:
        return "0"
    s = ""
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    while a:
        c = a % b
        a //= b
        s = digits[c] + s
    return s

def off8():
    offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    return offsets
    # for dx, dy in offsets:
    #     x = i + dx
    #     y = j + dy
    # OR
    # dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    # dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    # for k in range(8):
    #     x = i + dx[k]
    #     y = j + dy[k]