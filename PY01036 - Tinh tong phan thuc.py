def calc(n):
    total = 0.0
    if n % 2 == 1:
        for i in range(1, n+1, 2):
            total += 1/i
    else:
        for i in range(2, n+1, 2):
            total += 1/i
    return format(total, ".6f")
for _ in range(int(input())):
    n = int(input())
    print(calc(n))