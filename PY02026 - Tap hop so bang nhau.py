x, y = list(map(int, input().split()))

arr = list(map(int, input().split()))
brr = list(map(int, input().split()))

A, B = set(arr), set(brr)
print("YES" if A == B else "NO")