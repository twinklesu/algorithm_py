from collections import deque
import sys
input = sys.stdin.readline


def bfs(graph, n, visited):
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


def stackDfs(graph, n, visited):
    count = 0
    for i in range(n):
        if not visited[i]:
            stack = deque([i])
            while stack:
                thisNode = stack.pop()
                if not visited[thisNode]:
                    visited[thisNode] = True
                    for nextNode in graph[thisNode]:
                        if not visited[nextNode] and nextNode not in stack:
                            stack.append(nextNode)
            count += 1
    print(count)


def main():
    n, m = map(int, input().rstrip().split())
    graph = [[] for _ in range(n)]
    visited = [False for _ in range(n)]
    for _ in range(m):
        u, v = map(int, input().rstrip().split())
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    # bfs(graph, n, visited)
    stackDfs(graph, n, visited)




main()
