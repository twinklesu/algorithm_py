import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
for i in range(1, n+1):
    line = [0] + list(map(int, input().split()))
    rowAcc = 0
    for j in range(1, n+1):
        rowAcc += line[j]
        dp[i][j] = dp[i-1][j] + rowAcc

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    x1 -= 1
    y1 -= 1
    print(dp[x2][y2]-dp[x1][y2]-dp[x2][y1]+dp[x1][y1])

