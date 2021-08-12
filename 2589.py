from collections import deque
from copy import deepcopy


n, m = map(int, input().split())
mapp = [[1 for _ in range(m)] for _ in range(n)] # 1이면 땅, 0이면 바다
land = deque()
for i in range(n):
    line = input()
    for j, el in enumerate(line):
        if el == 'L':
            mapp[i][j] = 0
            land.append([i,j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 모든 땅 좌표에 대해 bfs 시행
ans = 0
for x, y in land:
    thisMap = deepcopy(mapp)
    thisMap[x][y] = 1 # visited
    q = deque()
    q.append([x,y,0]) # x, y, depth
    thisCount = 0
    while q:
        xx, yy, depth = q.popleft()
        thisCount = max(thisCount, depth)
        for i in range(4):
            newX = xx + dx[i]
            newY = yy + dy[i]
            if 0<=newX<n and 0<=newY<m and thisMap[newX][newY] == 0:
                thisMap[newX][newY] = 1
                q.append([newX, newY, depth+1])

    ans = max(ans, thisCount)

print(ans)