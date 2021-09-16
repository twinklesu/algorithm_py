from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def dfs(start, v, graph, cost):
    q = deque()
    q.append([start, 0])
    distance = [None for _ in range(v+1)]
    distance[start] = 0
    maxIndex = 0
    maxi = 0
    while q:
        thisNode, thisCost = q.pop()
        for nextNode in graph[thisNode]:
            if distance[nextNode] is None:
                distance[nextNode] = distance[thisNode] + cost[(thisNode, nextNode)]
                q.append([nextNode, distance[nextNode]])
                if distance[nextNode] > maxi:
                    maxIndex = nextNode
                    maxi = distance[nextNode]
    return maxIndex, maxi

v = int(input())
graph = defaultdict(list)
cost = dict()
for _ in range(v):
    inline = list(map(int, input().split()))
    u = inline[0]
    pointer = 1
    while inline[pointer] != -1:
        w = inline[pointer]
        pointer += 1
        c = inline[pointer]
        graph[u].append(w)
        cost[(u,w)] = c
        pointer += 1

# 첫번째 dfs
farFromOne, value = dfs(1, v, graph, cost)
# 두번째 dfs
node, ans = dfs(farFromOne, v, graph, cost)
print(ans)
