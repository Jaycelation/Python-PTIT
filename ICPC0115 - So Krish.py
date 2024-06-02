def digit(n):
    ans = 1
    for i in range (1, n+1):
        ans *= i
    return ans

def check(n):
    sum = 0
    for i in str(n):
        res = int(i)
        sum += digit(res)
    return sum == n

T = int(input())
while T != 0:
    T -= 1
    n = int(input())
    if check(n):
        print("Yes")
    else:
        print("No")