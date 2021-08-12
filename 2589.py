from collections import deque
from copy import deepcopy
import sys
input = sys.stdin.readline


n, m = map(int, input().split())
mapp = set()
land = deque()
for i in range(n):
    line = input()
    for j, el in enumerate(line):
        if el == 'L':
            mapp.add((i,j))
            land.append([i,j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
# 모든 땅 좌표에 대해 bfs 시행
ans = 0
visited = set()
for x, y in land:
    visited.clear()
    visited.add((x,y)) # visited
    q = deque()
    q.append([x,y,0]) # x, y, depth
    thisCount = 0
    while q:
        xx, yy, depth = q.popleft()
        thisCount = max(thisCount, depth)
        for i in range(4):
            newX = xx + dx[i]
            newY = yy + dy[i]
            if (newX, newY) not in visited and (newX, newY) in mapp:
                visited.add((newX, newY))
                q.append([newX, newY, depth+1])

    ans = max(ans, thisCount)

print(ans)