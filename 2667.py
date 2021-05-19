import sys

input = sys.stdin.readline
from collections import deque


def bfs(waiting_q, mapp, visited, n):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    count = 1
    while waiting_q:
        temp = waiting_q.popleft()
        for i in range(4):
            x = temp[0] + dx[i]
            y = temp[1] + dy[i]
            if 0 <= x < n and 0 <= y < n and visited[x][y] == 0 and mapp[x][y] == 1:
                waiting_q.append((x, y))
                visited[x][y] = 1
                count += 1
    return count


n = int(input())
mapp = [[0 for _ in range(n)] for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    line = list(map(int, input().rstrip()))
    for ind, el in enumerate(line):
        mapp[i][ind] = el

group = []
waiting_q = deque()
for i in range(n):
    for j in range(n):
        if mapp[i][j] == 1 and visited[i][j] == 0:
            waiting_q.append([i, j])
            visited[i][j] = 1
            group.append(bfs(waiting_q, mapp, visited, n))

print(len(group))
group.sort()
for g in group:
    print(g)
