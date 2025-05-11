n = int(input())
arr = list(map(int, input().split()))

s = 10 ** 9

for i in arr:
    x = 0
    for j in arr:
        x += abs(i-j)
    if s > x:
        s = x
        p = i
print(s, p)