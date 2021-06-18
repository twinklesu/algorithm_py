n = int(input())
numbers = list(map(int, input().split()))

dp = [[0 for _ in range(n)] for _ in range(n-1)]

ans = 0
for row in range(n-1):
    for ind in range(n-1):
        if ind == row:
            dp[row][ind] = 1
        if numbers[ind] < numbers[ind+1]:
            dp[row][ind+1] = dp[row][ind] + 1
        else:
            dp[row][ind+1] = dp[row][ind]
    if dp[row][-1] > ans:
        ans = dp[row][-1]

if ans == 1:
    print(0)
else:
    print(ans)
