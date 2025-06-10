for _ in range(int(input())):
    n, m = map(int, input().split())

    a = [list(map(int, input().split())) for _ in range(m)]
    INF = float('inf')
    dp = [[INF for _ in range(n+1)] for _ in range(m+1)]
    dp[0][0] = 0

    for i in range(1, n+1):
        for j in range(1, m+1):
            dp[i][j] = abs((min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) - a[i-1][j-1]))
    
    print(dp[n][m])