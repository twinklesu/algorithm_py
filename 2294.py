import sys
input = sys.stdin.readline

INF = 10**4+1
n, k = map(int, input().split())
dp = [INF for _ in range(k+1)]
for _ in range(n):
    dp[int(input())] = 1

for i in range(2, k+1):
    for j in range(1, i):
        if dp[j] != 0 and dp[i-j] != 0:
            dp[i] = min(dp[i], dp[j] + dp[i-j])

if dp[-1] == INF:
    print(-1)
else:
    print(dp[-1])