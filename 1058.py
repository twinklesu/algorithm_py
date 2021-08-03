n = int(input())
INF = 100
cost = [[INF for _ in range(n)] for _ in range(n)]
for i in range(n):
    line = input()
    for j in range(i+1, n):
        if line[j] == 'Y':
            cost[i][j] = 1
            cost[j][i] = 1
    cost[i][i] = 0

for mid in range(n):
    for start in range(n):
        for end in range(n):
            cost[start][end] = min(cost[start][end], cost[start][mid] + cost[mid][end])

ans = 0
for i in range(n):
    count = 0
    for j in range(n):
        if 0 < cost[i][j] <= 2:
            count += 1
    ans = max(ans, count)

print(ans)