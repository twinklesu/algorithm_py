n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]

dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            break
        if dp[i][j] > 0:
            move = board[i][j]
            if 0 <= i + move < n:
                dp[i + move][j] += dp[i][j]
            if 0 <= j + move < n:
                dp[i][j + move] += dp[i][j]


print(dp[-1][-1])