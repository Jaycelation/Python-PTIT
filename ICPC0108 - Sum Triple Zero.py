for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    count = 0
    arr.sort()
    for i in range(0, n - 2):
        left = i + 1
        right = n - 1
        while left < right:
            val = arr[i] + arr[left] + arr[right]
            if val == 0:
                count += 1
            elif val < 0:
                left += 1
            else:
                right -= 1
    print(count)