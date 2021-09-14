def dynamic(n, m):
    dp = [[0 for _ in range(m)] for _ in range(n)]
    dp[0] = [1 for _ in range(m)]
    for i in range(n):
        dp[i][0] = 1
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[-1][-1]


n, m, k = map(int, input().split())

if k == 0:
    print(dynamic(n,m))
else:
    k -=1
    x, y = k//m, k%m
    print(dynamic(x+1, y+1) * dynamic(n-x, m-y))
