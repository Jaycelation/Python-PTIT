n = int(input())

arr = list(map(int, input().split()))

temp = 0
res = []
for i in range(n):
    val = arr[i]
    for j in range(n):
        if i != j:
            temp += abs(arr[i] - arr[j])
    res.append(temp)
    temp = 0

j = 0
for i in range(n):
    if min(res) == res[i]:
        j = i
        break
print(min(res), arr[j])