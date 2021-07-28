from collections import deque
import sys
input = sys.stdin.readline


n, l, r = map(int, input().split())
countries = [list(map(int, input().split())) for _ in range(n)]

lookingFor = deque()
for i in range(n):
    for j in range(n):
        lookingFor.append([i,j])

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

changes = True
days = 0
q = deque()
visited = [[False for _ in range(n)] for _ in range(n)]
while lookingFor and changes:
    newLookingFor = deque()
    changes = False
    # 구역 탐색
    for i, j in lookingFor:
        if not visited[i][j]:
            visited[i][j] = True
            q.append([i,j])
            thisUnion = []
            summ = 0
            lenUnion = 0
            while q:
                temp = q.popleft()
                thisUnion.append(temp)
                summ += countries[temp[0]][temp[1]]
                lenUnion += 1
                for k in range(4):
                    newX = temp[0] + dx[k]
                    newY = temp[1] + dy[k]
                    if 0<=newX<n and 0<=newY<n and not visited[newX][newY]:
                        subs = abs(countries[temp[0]][temp[1]] - countries[newX][newY])
                        if l <= subs <= r:
                            q.append([newX, newY])
                            visited[newX][newY] = True
            # 인구이동
            if lenUnion > 1:
                changes = True # 오늘 변화 있었음
                newPop = summ//lenUnion
                for x,y in thisUnion:
                    countries[x][y] = newPop
                    newLookingFor.append([x,y])# 값이 변한애들만 다음에 bfs 하면돼
    if changes:
        days += 1
        visited = [[False for _ in range(n)] for _ in range(n)]
        lookingFor = newLookingFor
    if not changes:
        print(days)
