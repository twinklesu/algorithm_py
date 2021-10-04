from collections import deque
import sys
input = sys.stdin.readline

game = [["." for _ in range(6)] for _ in range(12)]
for i in range(12):
    inline = list(map(str, input().rstrip()))
    for j, el in enumerate(inline):
        game[i][j] = el

ans = -1
dx = [-1,1,0,0]
dy = [0,0,-1,1]
flag = True
while flag:
    # 영역 파악 bfs
    visited = [[False for _ in range(6)] for _ in range(12)]
    thisTurnRemove = []
    flag = False
    for i in range(12):
        for j in range(6):
            if not visited[i][j]:
                visited[i][j] = True
                if game[i][j] != ".":
                    # bfs
                    q = deque()
                    q.append([i,j])
                    color = game[i][j]
                    thisSpace = [[i,j]]
                    while q:
                        x, y = q.popleft()
                        for k in range(4):
                            newX, newY = x+dx[k], y+dy[k]
                            if 0<=newX<12 and 0<=newY<6 and not visited[newX][newY] and game[newX][newY] == color:
                                q.append([newX, newY])
                                visited[newX][newY] = True
                                thisSpace.append([newX, newY])
                    if len(thisSpace) >= 4:
                        flag = True
                        for x,y in thisSpace:
                            game[x][y] = "."
    # 아래부터 값 땅기기
    for j in range(6):
        for i in range(11, -1, -1):
            if game[i][j] == ".":
                k = 0
                while i-k>=0 and game[i-k][j] == ".":
                    k += 1
                if i-k >= 0:
                    game[i][j], game[i-k][j] = game[i-k][j], game[i][j]
                else:
                    break
    ans += 1

print(ans)