from collections import defaultdict, deque


n, m, k, x = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)

INF = 10**6
dist = [INF for _ in range(n+1)] # 0은 place holder
dist[x] = 0

q = deque()
q.append([x,0])
while q:
    node, distance = q.popleft()

    if dist[node] < distance:
        continue

    if node in graph:
        for nn in graph[node]:
            new_dist = dist[node] + 1
            if dist[nn] > new_dist:
                dist[nn] = new_dist
                q.append([nn, dist[nn]])

flag = True
for ind, el in enumerate(dist):
    if el == k:
        flag = False
        print(ind)
if flag:
    print(-1)
