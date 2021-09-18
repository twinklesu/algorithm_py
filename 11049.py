n = int(input())
size = dict()
for i in range(n):
    size[i] = list(map(int, input().split()))
dp = [[0 for _ in range(n)] for _ in range(n)]
INF = 2**31-1

for diagonal in range(1, n):
    for row in range(n-diagonal):
        col = row+diagonal
        if diagonal == 1:
            dp[row][col] = size[row][0] * size[row][1] * size[col][1]
        else:
            dp[row][col] = INF
            for calculated in range(row, col):
                dp[row][col] = min(dp[row][col], dp[row][calculated]+dp[calculated+1][col]+size[row][0]*size[calculated][1]*size[col][1])


print(dp[0][-1])

