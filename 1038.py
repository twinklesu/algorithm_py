def backTrack(targetLen, numLen, num, k, n):
    if numLen == targetLen and k == n:
        return num
    for i in range(num%10):


n = int(input())

dp = [[0 for _ in range(10)] for _ in range(11)]
for j in range(10):
    dp[0][j] = 1
for i in range(1,11):
    for j in range(10):
        dp[i][j] = sum(dp[i-1][j+1:])

dp_count = 0
length = -1
for i in range(11):
    dp_count += sum(dp[i])
    if dp_count >= n:
        length = i +1
        break

if length == -1:
    print(-1)
else:
