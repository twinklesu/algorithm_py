import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().rstrip().split()))
ans = numbers[0]
dp = [ans for _ in range(n)]


for i in range(0, n):
    if dp[i] < numbers[i]:
        dp[i] = numbers[i]
        if dp[i] > ans:
            ans = dp[i]
        for j in range(i+1, n):
            dp[j] = dp[j-1] + numbers[j]
            if dp[j] > ans:
                ans = dp[j]

print(max(dp))
