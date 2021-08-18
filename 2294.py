import sys
input = sys.stdin.readline

n, k = map(int, input().split())
INF = k+1
prices = [INF for _ in range(k+1)]
for _ in range(n):
    num = int(input())
    if num <= k: #. 인덱스 에러 방지
        prices[num] = 1

for i in range(1, k+1):
    for j in range(i):
        if prices[j]+prices[i-j] < prices[i]:
            prices[i] = prices[j] + prices[i-j]


if prices[-1] == INF:
    print(-1)
else:
    print(prices[-1])

