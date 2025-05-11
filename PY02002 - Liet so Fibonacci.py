fib = [0] * 94
def init():
    fib[0] = 0
    fib[1] = 1
    fib[2] = 1
    for i in range(3, 94):
        fib[i] = fib[i-1] + fib[i-2]
    return fib
init()
for _ in range(int(input())):
    inp = list(map(int, input().split()))
    a, b = inp[0], inp[1]
    for i in range(a, b+1):
        print(fib[i], end=' ')
    print()