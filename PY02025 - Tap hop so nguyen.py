n, m = map(int, input().split())
arr = list(map(int, input().split()))
brr = list(map(int, input().split()))

A = set(arr)
B = set(brr)

# Giao: A ∩ B
print(*sorted(A & B))

# Hiệu: A - B
print(*sorted(A - B))

# Hiệu: B - A
print(*sorted(B - A))