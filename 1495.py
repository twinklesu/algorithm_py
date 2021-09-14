n, s, m = map(int, input().split())
v = list(map(int, input().split()))

dp = [0 for _ in range(m+1)]
dp[s] = 1
for song in range(n):
    new_dp = [0 for _ in range(m+1)]
    for i in range(m+1):
        if dp[i]:
                if 0 <= i + v[song] <= m:
                    new_dp[i+v[song]] = 1
                if 0 <= i - v[song] <= m:
                    new_dp[i-v[song]] = 1
    dp = new_dp


for i in range(m, -1, -1):
    if dp[i]:
        print(i)
        break
else:
    print(-1)