n = int(input())
arr = list(map(float, input().split()))

dmax = max(arr)
dmin = min(arr)

filtered_arr = [x for x in arr if x != dmax and x != dmin]

avg = sum(filtered_arr) / len(filtered_arr)
print(f"{avg:.2f}")
