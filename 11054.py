n = int(input())
numbers = list(map(int, input().split()))
increasingDp = [1 for _ in range(n)]
decreasingDp = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if numbers[i] > numbers[j]:
            increasingDp[i] = max(increasingDp[i], increasingDp[j]+1)

for i in range(n-1, -1, -1):
    for j in range(i+1, n):
        if numbers[i] > numbers[j]:
            decreasingDp[i] = max(decreasingDp[i], decreasingDp[j]+1)

dp = [0 for _ in range(n)]
for i in range(n):
    dp[i] = increasingDp[i] + decreasingDp[i]

print(max(dp)-1)
