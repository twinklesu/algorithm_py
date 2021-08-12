n, m = map(int, input().split())
dp = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    line = map(int, input())
    for j, el in enumerate(line):
        dp[i][j] = el

maxSquare = 0
for i in range(n):
    for j in range(m):
        if dp[i][j] == 1:
            if 0<i and 0<j:
                dp[i][j] = min([dp[i-1][j], dp[i-1][j-1], dp[i][j-1]]) + 1
            maxSquare = max(maxSquare, dp[i][j])

print(maxSquare**2)