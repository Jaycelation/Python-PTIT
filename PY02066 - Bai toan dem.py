from collections import Counter
n = int(input())
arr = []
sum = 0
while len(arr) != n:
    line = list(map(int, input().split()))
    for i in range(len(line)):
        arr.append(line[i])

A = Counter(arr)
c = 1
for i in range(1, max(arr)+1):
    if i not in A.keys():
        c = 0
        print(i)
if c:
    print("Excellent!")