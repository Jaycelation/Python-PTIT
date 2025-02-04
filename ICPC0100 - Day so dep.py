test = int(input())
while test:
    test -= 1
    n = int(input())
    arr = list(map(int, input().split()))
    result = [arr[0]]
    for i in range(n-1):
        a, b = arr[i], arr[i+1]
        if a > b:
            a, b = b, a
        while b > 2 * a:
            a *= 2
            result.append(a)
        result.append(arr[i+1])
    print(len(result) - n)