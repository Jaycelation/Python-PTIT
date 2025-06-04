for _ in range(int(input())):
    n, m = map(int, input().split())
    x = []

    for i in range(n):
        temp = list(map(int, input().split()))
        x.append(temp)
    y = [[0 for _ in range(n)] for _ in range(m)]
    for i in range(n):
        for j in range(m):
            y[j][i] = x[i][j]
    
    z = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(m):
                z[i][j] += x[i][k] * y[k][j]
    
    for i in range(n):  
        for j in range(n):
            print(z[i][j], end=' ')
        print()