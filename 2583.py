from collections import deque


m, n, k = map(int, input().split())
paper = [[0 for _ in range(n)] for _ in range(m)]
for _ in range(k):
    # 사각형 마킹
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            paper[i][j] = 1

# bfs
count = 0
size = []
dx = [1, -1, 0, 0]
dy = [0,0,1,-1]
for i in range(m):
    for j in range(n):
        if paper[i][j] == 0:
            q = deque()
            q.append([i,j])
            paper[i][j] = 1
            thisSize = 1
            count += 1
            while q:
                x, y = q.popleft()
                for k in range(4):
                    newX = x+dx[k]
                    newY = y+dy[k]
                    if 0<=newX<m and 0<=newY<n and paper[newX][newY] == 0:
                        q.append([newX, newY])
                        thisSize += 1
                        paper[newX][newY] = 1
            size.append(thisSize)

size.sort()
print(count)
print(*size)
