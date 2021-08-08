from collections import deque
import sys
input = sys.stdin.readline


n = int(input())
space = [[0 for _ in range(n)] for _ in range(n)]
rains = {1, 100} # 높이가 0이거나 100 초과일 수 있음
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(n):
        space[i][j] = line[j]
        if 1 < line[j] < 100:
            rains.add(line[j]) # 지역의 높이만큼 비가 내릴때 안전지대에 영향을 줌


safety = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for rain in rains:
    # 최대 높이 지역만큼 비가 오면 안전지대는 0개
    thisSafety = 0
    visited = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if space[i][j] >= rain and not visited[i][j]:
                # bfs
                q = deque()
                q.append([i,j])
                visited[i][j] = True
                thisSafety += 1
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        newX = x + dx[k]
                        newY = y + dy[k]
                        if 0<=newX<n and 0 <=newY<n and not visited[newX][newY] and space[newX][newY] >= rain:
                            visited[newX][newY] = True
                            q.append([newX, newY])
    safety = max(safety, thisSafety)

print(safety)