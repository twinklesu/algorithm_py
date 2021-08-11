n, m = map(int, input().split())
miro = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(m)] for _ in range(n)]
dp[0][0] = miro[0][0]

dx = [-1, -1, 0]
dy = [0, -1, -1]
for i in range(n):
    for j in range(m):
        for k in range(3):
            newX = i+dx[k]
            newY = j+dy[k]
            if 0<=newX and 0<=newY:
                dp[i][j] = max(dp[i][j], miro[i][j]+dp[newX][newY])

print(dp[-1][-1])
