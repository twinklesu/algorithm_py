from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    inline = list(map(int, input().split()))
    for j, el in enumerate(inline):
        board[i][j] = el

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

count = 0
maxSize = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            # bfs
            q = deque()
            q.append([i,j])
            board[i][j] = 0 # visited
            thisSize = 0
            count += 1
            while q:
                x, y = q.popleft()
                thisSize += 1
                for k in range(4):
                    newX = x + dx[k]
                    newY = y + dy[k]
                    if 0<=newX<n and 0<=newY<m and board[newX][newY] == 1:
                        board[newX][newY] = 0
                        q.append([newX, newY])
            maxSize = max(maxSize, thisSize)

print(count)
print(maxSize)