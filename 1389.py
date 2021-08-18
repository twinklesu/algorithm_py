from collections import defaultdict

n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

INF = 101 # n명이 한줄로 있어도, 최대 비용 n
cost = [[INF for _ in range(n+1)] for _ in range(n+1)]
for i in range(n+1):
    if i in graph:
        for j in graph[i]:
            cost[i][j] = 1
    cost[i][i] = 0


for mid in range(1, n+1):
    for start in range(1, n+1):
        for end in range(1, n+1):
            if cost[start][end] > cost[start][mid] + cost[mid][end]:
                cost[start][end] = cost[start][mid] + cost[mid][end]

minCost = INF
minInd = -1
for i in range(1, n+1):
    if minCost > sum(cost[i][1:]):
        minCost = sum(cost[i][1:])
        minInd = i

print(minInd)
