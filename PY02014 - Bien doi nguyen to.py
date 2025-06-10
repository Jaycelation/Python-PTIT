from math import sqrt

def check_prime(n):
    for i in range(2, int(sqrt(n)+1)):
        if n % i == 0:
            return False
    return n > 1

def nearest_prime(n):
    if n < 2:
        return 2

    lower = n
    upper = n

    while True:
        if check_prime(lower):
            return lower
        if check_prime(upper):
            return upper
        lower -= 1
        upper += 1

n = int(input())
arr = list(map(int, input().split()))
cnt = 0
for i in range(n):
    if not check_prime(arr[i]):
        val = nearest_prime(arr[i])
        #print(f"[{arr[i]}] -> [{val}]")
        cnt = max(cnt, abs(arr[i]-val))

print(cnt)