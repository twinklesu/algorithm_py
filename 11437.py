from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())
tree = defaultdict(list)
for _ in range(n-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)

# 모든 노드에 대하여, parent 찾기
parentList = [[0 for _ in range(16)] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
depthList = [0 for _ in range(n+1)]


def dfs(node, depth):
    visited[node] = True
    depthList[node] = depth
    for nextNode in tree[node]:
        if not visited[nextNode]:
            parentList[nextNode][0] = node
            dfs(nextNode, depth + 1)


dfs(1, 0)
for depth in range(1, 17):
    for node in range(1, n+1):
        parent = parentList[node][depth-1]
        parentList[node][depth] = parentList[parent][depth-1]

m = int(input())
for _ in range(m):
    u, v = map(int, input().split())
    uParentNum = depthList[u]
    vParentNum = depthList[v]
    uPointer, vPointer = -1, -1
    while uParentNum > vParentNum:
        uPointer -= 1
        uParentNum -= 1
    while vParentNum > uParentNum:
        vPointer -= 1
        vParentNum -= 1
    uParent = parentList[u][uPointer]
    vParent = parentList[v][vPointer]
    while uParent != vParent:
        uPointer -= 1
        vPointer -= 1
        uParent = parentList[u][uPointer]
        vParent = parentList[v][vPointer]

    print(uParent)