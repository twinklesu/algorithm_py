from heapq import heappop, heappush
from collections import defaultdict

n = int(input())
m = int(input())
graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

INF = 1000
cost = [INF for _ in range(n+1)] # place holder 0 index
cost[1] = 0 #상근이 자기 자신
heapq = []
for g in graph[1]:
    cost[g] = 1
    heapq.append([1, g])

# 다익스트라
while heapq:
    priority, thisNode = heappop(heapq)
    if thisNode in graph:
        nextNodes = graph[thisNode]
        for nn in nextNodes:
            if cost[thisNode] + 1 < cost[nn]:
                cost[nn] = cost[thisNode] + 1
                heappush(heapq, [cost[nn], nn])

cnt = -1 # 상근이 늘 빼고 세야해서
for c in cost:
    if c <= 2:
        cnt += 1
print(cnt)