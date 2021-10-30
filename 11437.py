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
parentList = dict()
visited = [False for _ in range(n+1)] # 0 place holder


def findParents(thisNode, parents: list):
    parentList[thisNode] = parents + [thisNode]
    for nextNode in tree[thisNode]:
        if not visited[nextNode]:
            visited[nextNode] = True
            findParents(nextNode, parents+[thisNode])


visited[1] = True
findParents(1, [])

m = int(input())
for _ in range(m):
    u, v = map(int, input().split())
    uParentNum = len(parentList[u])
    vParentNum = len(parentList[v])
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