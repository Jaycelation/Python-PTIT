from collections import Counter

def findcheck(arr, n):
    mapcount = Counter(arr)
    check = n // 2

    res = [val for val, count in mapcount.items() if count > check]

    if res:
        print(min(res))
    else:
        print("NO")

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    
    findcheck(arr, n)