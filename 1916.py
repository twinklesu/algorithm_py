from heapq import heappop, heappush
from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
cost = dict()
graph = defaultdict(list)
for _ in range(m):
    start, to, c = map(int, input().split())
    if (start, to) in cost:
        cost[(start, to)] = min(cost[(start, to)], c)
    else:
        cost[(start, to)] = c
        graph[start].append(to)
startNode, destNode = map(int, input().split())

# 다익스트라
heapq = []
INF = 10**10+1
dijkstra = [INF for _ in range(n + 1)] # 0은 place holder
dijkstra[startNode] = 0
heappush(heapq, [0, startNode])
while heapq:
    thisCost, thisNode= heappop(heapq)
    if thisNode in graph:
        nextNodes = graph[thisNode]
        for nn in nextNodes:
            newCost = thisCost + cost[(thisNode, nn)]
            if newCost < dijkstra[nn]:
                dijkstra[nn] = newCost
                heappush(heapq, [newCost, nn])

print(dijkstra[destNode])
