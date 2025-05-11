arr = list(map(int, input().split()))
a, k, n = arr[0], arr[1], arr[2]

first = ((a // k) + 1) * k

if first > n:
    print("-1")
else:
    lst = list(range(first - a, n - a + 1, k))  
    print(" ".join(map(str, lst)))