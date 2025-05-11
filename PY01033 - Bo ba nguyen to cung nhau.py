import math
def check(a, b):
    return math.gcd(a, b) == 1

arr = list(map(int, input().split()))
a, b = arr[0], arr[1]
for i in range(a, b+1):
    for j in range(i+1, b+1):
        for k in range(j+1, b+1):
            if check(i, j) and check(j, k) and check(i, k):
                print(f'({i}, {j}, {k})')