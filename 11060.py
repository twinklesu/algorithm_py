n = int(input())
numbers = list(map(int, input().split()))
dp = [n for _ in range(n)]
dp[0] = 0

for i in range(n):
    for j in range(1, numbers[i]+1):
        if i+j < n:
            dp[i+j] = min(dp[i+j], dp[i]+1)

if dp[-1] == n:
    print(-1)
else:
    print(dp[-1])