n, k = map(int, input().split())

dp = [[1 for _ in range(n+1)] for _ in range(k)]

for i in range(1, k):
    for j in range(n+1):
        if j == 0:
            dp[i][j] = 1
        else:
            dp[i][j] = (dp[i][j-1] + dp[i-1][j])%10**9

print(dp[-1][-1])