def check(a, b):
    from math import gcd
    return gcd(a, b) == 1

arr = list(map(int, input().split()))
n, temp = arr[0], arr[1]
a = 10 ** (temp-1)
b = 10 ** temp
j = 0
for i in range(a, b):
    if check(n, i):
        print(i, end=" ")
        j += 1
        if j == 10:
            j = 0
            print()