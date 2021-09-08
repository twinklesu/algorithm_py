from heapq import heappush, heappop
n = int(input())
li = []
for _ in range(n):
    u, v = map(int, input().split())
    heappush(li, [u, v])

line = []
while li:
    pri, value = heappop(li)
    line.append(value)

# 가장 긴 증가하는 수열 dp 로 찾으면 됨
dp = [1 for _ in range(n)]
for i in range(n):
    for j in range(0,i):
        if line[i] > line[j] and dp[j]+1 > dp[i]:
            dp[i] = dp[j] + 1

print(n-max(dp))