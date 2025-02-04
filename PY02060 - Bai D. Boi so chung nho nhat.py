from math import lcm

mod = 10 ** 9 + 7

def product(a, b):
    result = 1
    for i in range(a, b+1):
        result = (result * i) % mod
    return result

test = int(input())
while test:
    test -= 1
    a, b = list(map(int, input().split()))
    target = product(a, b)
    count = 0
    for i in range(a, b+1):
        for j in range(i, b+1):
            if lcm(i, j) == target:
                count += 1
    print(count % mod)