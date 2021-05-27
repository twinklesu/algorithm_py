import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().rstrip().split())
box = [list(map(int, input().rstrip().split())) for _ in range(m)]

q = deque()
for i in range(m):
    for j in range(n):
        if box[i][j] == 1:
            q.append([i,j,0])

dx = [-1,1,0,0]
dy = [0,0,-1,1]
days = 0
while q:
    tomato = q.popleft()
    for ddx, ddy in zip(dx, dy):
        newX = tomato[0] + ddx
        newY = tomato[1] + ddy
        if 0<=newX<m and 0<=newY<n and box[newX][newY]==0:
            q.append([newX, newY, tomato[2]+1])
            box[newX][newY] = 1
    days = max(days, tomato[2])

for row in box:
    if 0 in row:
        print(-1)
        break
else:
    print(days)

