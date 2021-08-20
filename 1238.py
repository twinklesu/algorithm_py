from collections import defaultdict
from heapq import heappop, heappush


n, m, x = map(int, input().split())
INF = 10**6 # 시간의 최댓값이 100이고, 최대 1000개 도시를 다 거쳐간다면 + 왕복
costDict = {}
for _ in range(m):
    u, v, t = map(int, input().split())
    costDict[(u,v)] = t

# x로 가는 다익스트라
toX = [INF for _ in range(n+1)]
toX[x] = 0
heap = []
for c in costDict:
    if c[1] == x:
        heappush(heap, [costDict[c], c[0]])
        toX[c[0]] = costDict[c]
while heap:
    thisT, start = heappop(heap)
    for i in range(1, n+1):
        if (i, start) in costDict:
            newT = costDict[(i,start)]+thisT
            if newT < toX[i]:
                toX[i] = newT
                heappush(heap, [newT, i])

# x에서 오는 다익스트라
fromX = [INF for _ in range(n+1)]
fromX[x] = 0
heap = []
for c in costDict:
    if c[0] == x:
        heappush(heap, [costDict[c], c[1]])
        fromX[c[1]] = costDict[c]
while heap:
    thisT, start = heappop(heap)
    for i in range(1, n+1):
        if (start, i) in costDict:
            newT = costDict[(start, i)] + thisT
            if newT < fromX[i]:
                fromX[i] = newT
                heappush(heap, [newT, i])
# 왕복 시간
maxTime = 0
for i in range(1, n+1):
    totalTime = fromX[i] + toX[i]
    maxTime = max(maxTime, totalTime)

print(maxTime)