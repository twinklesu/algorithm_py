n = int(input())
numbers = list(map(int, input().split()))
dp = [0 for _ in range(n)]

for i in range(n):
    dp[i] = numbers[i]
    for j in range(i):
        if numbers[i] > numbers[j]:
            if dp[i] < dp[j] + numbers[i]:
                dp[i] = dp[j] + numbers[i]

print(max(dp))