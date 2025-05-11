def func(n):
    return n + int(str(n)[::-1])

for _ in range(int(input())):
    n = int(input())
    i = 0
    while n % 7 != 0 and i < 1000:
        n = func(n)
        i += 1
    print(n)