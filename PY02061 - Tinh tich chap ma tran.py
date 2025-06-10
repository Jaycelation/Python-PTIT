for _ in range(int(input())):
    n, m = map(int, input().split())

    x = [list(map(int, input().split())) for _ in range(n)]
    h = [list(map(int, input().split())) for _ in range(3)]

    result = []
    total = 0

    for i in range(n - 2):
        row = []
        for j in range(m - 2):
            s = 0
            for k1 in range(3):
                for k2 in range(3):
                    s += h[k1][k2] * x[i + k1][j + k2]
            row.append(s)
            total += s
        result.append(row)
        
    print(total)
