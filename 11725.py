from collections import defaultdict, deque
import sys
input = sys.stdin.readline

def dfs(n: int, tree: defaultdict):
    visited = [False for _ in range(n+1)]
    visited[0] = True # place holder
    visited[1] = True # 1은 방문하고 시작하니까
    ans = [0 for _ in range(n+1)] # 0 인덱스는 place holder

    stack = deque()
    stack.append(1)
    while stack:
        thisNode = stack.pop()
        nextNodes = tree[thisNode]
        for nextN in nextNodes:
            if not visited[nextN]:
                ans[nextN] = thisNode  # nextN의 부모는 thisNode
                visited[nextN] = True
                stack.append(nextN)
    return ans


def main():
    n = int(input())
    tree = defaultdict(list)
    for _ in range(n-1):
        u, v = map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)

    ans = dfs(n, tree)
    print(*ans[2:], sep='\n')

main()