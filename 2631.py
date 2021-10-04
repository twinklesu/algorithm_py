n = int(input())
numbers = list()
for _ in range(n):
    numbers.append(int(input()))

dp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if numbers[j] < numbers[i] and dp[j] >= dp[i]:
            dp[i]  = dp[j] + 1

maxi = max(dp)
print(n - maxi)