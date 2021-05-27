from collections import deque

n, k = map(int, input().split())
q = deque([n])
visited = [None for _ in range(100001)]
visited[n] = 0

while q:
    node = q.popleft()
    if node == k:
        print(visited[node])
        break
    else:
        next_node = [node-1, node+1, node*2]
        for next_ in next_node:
            if 0<=next_<=100000 and visited[next_] is None:
                visited[next_] = visited[node] + 1
                q.append(next_)
