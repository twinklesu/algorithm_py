from collections import defaultdict
from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

INF = 10**7
dist = [INF for _ in range(n+1)]
dist[x] = 0
q = []
heappush(q, [0, x])
while q:
    thisNode, thisDist = heappop(q)
    if thisNode in graph:
        nextNodes = graph.pop(thisNode)
        for nn in nextNodes:
            if dist[nn] > thisDist + 1:
                dist[nn] = thisDist + 1
                heappush(q, [dist[nn], nn])

flag = True
for ind, el in enumerate(dist):
    if el == k:
        print(ind)
        flag = False
if flag:
    print(-1)
