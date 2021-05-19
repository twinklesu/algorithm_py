n = int(input())

dp = [None, 0, 1, 1]

for i in range(4, n+1):
    temp = []
    if i % 3 == 0:
        temp.append(dp[i//3])
    if i % 2 == 0:
        temp.append(dp[i//2])
    temp.append(dp[i-1])
    dp.append(min(temp)+1)


print(dp[n])

