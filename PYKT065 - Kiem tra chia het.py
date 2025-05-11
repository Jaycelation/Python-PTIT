import itertools

def count(L, R, K):
    return (R // K) - ((L - 1) // K)

def sieve(n):
    is_prime = [True] * (n + 1)
    primes = []
    for i in range(2, n + 1):
        if is_prime[i]:
            primes.append(i)
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return primes

def inclusion_exclusion(L, R, primes):
    m = len(primes)
    res = 0
    
    def dfs(index, product, sign):
        nonlocal res
        if index == m or product > R:
            return
        
        new_product = product * primes[index]
        if new_product <= R:
            res += sign * count(L, R, new_product)
            dfs(index + 1, new_product, -sign)
        
        dfs(index + 1, product, sign)
    
    dfs(0, 1, 1)
    return res

while True:
    try:
        line = input().strip()
        if line == "-1":
            break
        
        L, R = map(int, line.split())
        N = int(input())
        primes = sieve(N)
        total = R - L + 1
        bad = inclusion_exclusion(L, R, primes)

        print(total - bad)
        

    except EOFError:
        break