from collections import Counter
from math import sqrt

def check_prime(n):
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return False
    return n > 1

n = int(input())
arr = list(map(int, input().split()))

A = Counter(arr)
B = [val for val in A.keys()]

pre = [0] * len(B)
pre[0] = B[0]
for i in range(1, len(B)):
    pre[i] = pre[i-1] + B[i]

total = pre[-1]
val = -1

for i in range(len(B)):
    sum_pre = pre[i]
    sum_suf = total - sum_pre
    if check_prime(sum_pre) and check_prime(sum_suf):
        val = i
        break

print("NOT FOUND" if val == -1 else val)
