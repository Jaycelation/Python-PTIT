from math import *

test = int(input())
while test:
    test -= 1
    n = input()
    cnt = len(n) - 1
    n = int(n)
    i = 1
    while i <= cnt:
        n /= pow(10, i)
        if n - int(n) >= 0.5:
            n = ceil(n)
        else:
            n = int(n)
        n *= pow(10, i)
        i += 1
    print(int(n))
