import sys
from collections import Counter

def prime_factorization(n):
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

def format_output(n):
    factor_counts = Counter(prime_factorization(n))
    result = "1"
    for factor, count in sorted(factor_counts.items()):
        result += f" * {factor}^{count}"
    return result

def main():
    t = int(sys.stdin.readline().strip())  # Đọc số bộ test
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        print(format_output(n))

if __name__ == "__main__":
    main()