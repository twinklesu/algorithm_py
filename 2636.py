from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0 for _ in range(m)] for _ in range(n)]
newQ = deque()
cheese = [0]
for i in range(m):
    inline = list(map(int, input().split()))
    for j, el in enumerate(inline):
        if el == 1:
            graph[i][j] = el
            cheese[0] += 1
dx = [1,-1,0,0]
dy = [0,0,1,-1]
q = deque()

hrCount = 0
while cheese[-1] > 0:
    hrCount += 1
    looseCheese = deque()
    q.append([0,0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[0][0] = True
    while q:
        x, y = q.popleft()
        for k in range(4):
            newX, newY = x+dx[k], y+dy[k]
            if 0<=newX<n and 0<=newY<m and not visited[newX][newY]:
                visited[newX][newY] = True
                if graph[newX][newY] == 0:
                    # 바깥쪽 계속 탐색
                    q.append([newX, newY])
                else:
                    # 가장 외곽의 치즈면
                    looseCheese.append([newX, newY])
    # 이 시간의 치즈 없애기
    countLoose = 0
    for x,y in looseCheese:
        countLoose += 1
        graph[x][y] = 0
    cheese.append(cheese[-1]-countLoose)


print(hrCount)
print(cheese[-2])