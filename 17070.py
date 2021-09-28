import sys
input = sys.stdin.readline

n = int(input())
room = [[0 for _ in range(n+1)] for _ in range(n+1)]
dp = [[[0,0,0] for _ in range(n+1)] for _ in range(n+1)]
for i in range(1,n+1):
    inline = list(map(int, input().split()))
    for j, el in enumerate(inline):
        room[i][j+1] = el
moving = {0: (0,1), 1: (1,1), 2:(1,0)}
dx = [0, 1, 1]
dy = [1, 0, 1]


dp[1][2][0] += 1
for i in range(1,n+1):
    for j in range(1,n+1):
        if room[i][j] == 1:
            continue
        else:
            # 0도
            dp[i][j][0] += sum(dp[i][j-1][:2])
            # 90도
            dp[i][j][2] += sum(dp[i-1][j][1:])
            # 45도
            if room[i-1][j] == 0 and room[i][j-1] == 0:
                dp[i][j][1] += sum(dp[i-1][j-1])
print(sum(dp[-1][-1]))