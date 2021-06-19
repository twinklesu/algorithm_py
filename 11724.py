from collections import deque
import sys
input = sys.stdin.readline


def main():
    n, m = map(int, input().rstrip().split())
    graph = [[] for _ in range(n)]
    visited = [False for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().rstrip().split())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    count = 0
    for i in range(n):
        if not visited[i]:
            count += 1
            q = deque(graph[i])
            while q:
                temp = q.popleft()
                visited[temp] = True
                for newNode in graph[temp]:
                    if not visited[newNode] and newNode not in q:
                        q.append(newNode)

    print(count)


main()
