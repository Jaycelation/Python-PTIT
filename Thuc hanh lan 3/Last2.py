n = int(input())
sum1 = 0
sum2 = 0
arr = [[0] * n for _ in range(n)]
for i in range(n):
    lst = list(map(int, input().split()))
    for j in range(n):
        arr[i][j] = lst[j]

for i in range(n):
    for j in range(n):
        if j< n - i - 1:
            sum1 += arr[i][j]
        elif j > n - i - 1:
            sum2 += arr[i][j]
        else:
            continue
x = int(input())
print("YES" if abs(sum1-sum2) <= x else "NO")
print(abs(sum1-sum2))
