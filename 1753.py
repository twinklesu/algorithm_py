import sys
from collections import defaultdict
from heapq import heappush, heappop
input = sys.stdin.readline

nNode, nEdge = map(int, input().rstrip().split())
start = int(input())
graph = defaultdict(list)
for _ in range(nEdge):
    u, v, w = map(int, input().rstrip().split())
    graph[u].append([v, w]) # 끝 노드, 가중치

INF = 10**6
shortestPath = [INF for _ in range(nNode+1)]
shortestPath[start] = 0
waitingQ = []
heappush(waitingQ, [0, start])

while waitingQ:
    thisWeight, thisNode = map(int, heappop(waitingQ))

    # 큐에 있던 동안 더 짧은 경로 생겼을 수 있어서, 얘가 최단일 때만 계산한다.
    if thisWeight <= shortestPath[thisNode]:
        for nextNode, nextWeight in graph[thisNode]:
            newWeight = thisWeight + nextWeight
            if newWeight < shortestPath[nextNode]:
                shortestPath[nextNode] = newWeight
                heappush(waitingQ, [newWeight, nextNode])

for path in shortestPath[1:]:
    print(path if path != INF else 'INF')