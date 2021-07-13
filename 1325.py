from collections import defaultdict,deque
import sys
input = sys.stdin.readline


def dfs(tree:dict, key:int, n:int):
    stack = deque()
    stack.append(key)
    count = 0
    visited = [0 for _ in range(n+1)]
    visited[key] = 1
    while stack:
        temp = stack.popleft()
        count += 1
        if temp in tree:
            nextNode = tree[temp]
            for node in nextNode:
                if visited[node] == 0:
                    visited[node] = 1
                    stack.append(node)
    return count


def main():
    n, m = map(int, input().split())
    tree = defaultdict(list)
    for _ in range(m):
        value, key = map(int, input().split())
        tree[key].append(value)

    maxCount = 0
    maxAns = []
    for key in range(1, n+1):
        count = dfs(tree, key, n)
        if maxCount < count:
            maxAns = [key]
            maxCount = count
        elif maxCount == count:
            maxAns.append(key)

    print(*maxAns)


main()