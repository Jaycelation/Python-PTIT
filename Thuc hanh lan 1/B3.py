t = int(input())
for _ in range(t):
    n = int(input())
    arr = sorted([int(x) for x in input().split()])
    count = 0
    for i in range(0, n-2):
        left = i+1
        right = len(arr) - 1
        x = arr[i]
        while left < right:
            if x + arr[left] + arr[right] == 0:
                count += 1
                left += 1
            elif x + arr[left] + arr[right] < 0:
                left += 1
            else:
                right -= 1
    print(count)