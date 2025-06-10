for _ in range(int(input())):
    n, m, l = list(map(int, input().split()))
    
    k = l // 2

    image = [list(map(int, input().split())) for _ in range(n)]

    result = []
    for i in range(k, n - k):
        row = []
        for j in range(k, m - k):
            total = 0
            for u in range(-k, k + 1):
                for v in range(-k, k + 1):
                    total += image[i + u][j + v]
            smoothed = total // (l * l)
            row.append(smoothed)
        print(*row)
