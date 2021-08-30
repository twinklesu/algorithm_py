from collections import deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    choices = [0] + list(map(int, input().split()))
    graph = dict()
    visited = [False for _ in range(n+1)]
    for ind, el in enumerate(choices):
        if ind == el:
            visited[ind] = True
        else:
            graph[ind] = el
    for i in range(n+1):
        if not visited[i]:
            # dfs
            q = deque()
            q.append(i)
            thisVisitied = set()
            thisVisitied.add(i)
            while q:
                thisNode = q.pop()
                if thisNode in graph:
                    if graph[thisNode] not in thisVisitied:
                        q.append(graph[thisNode])
                        thisVisitied.add(graph[thisNode])
                    elif graph[thisNode] == i:
                        # 사이클이 잘 돈거니까
                        for v in thisVisitied:
                            visited[v] = True
                        break
    print(visited.count(False))
