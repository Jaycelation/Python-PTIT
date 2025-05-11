from collections import Counter
import math
def prime(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return n > 1

n = int(input())
arr = list(map(int, input().split()))
maparr = Counter(arr)

for x, y in maparr.items():
    if prime(x):
        print(x, y)
