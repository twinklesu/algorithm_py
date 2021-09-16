from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def markingIsland(mapp, n):
    q = deque()
    mark = 1
    for i in range(n):
        for j in range(n):
            if mapp[i][j] == 1:
                mark += 1
                q.append([i, j])
                mapp[i][j] = mark
                while q:
                    x, y = q.popleft() # bfs
                    for k in range(4):
                        newX = x + dx[k]
                        newY = y + dy[k]
                        if 0<=newX<n and 0<=newY<n and mapp[newX][newY] == 1:
                            q.append([newX, newY])
                            mapp[newX][newY] = mark
    return mapp


def findNearest(mapp, n):
    q = deque()
    ans = n*3
    for i in range(n):
        for j in range(n):
            if mapp[i][j] != 0:
                visited = [[False for _ in range(n)] for _ in range(n)]
                island = mapp[i][j]
                q.append([i,j, 0])
                visited[i][j] = True
                while q:
                    x, y, cost = q.popleft()
                    for k in range(4):
                        newX = x + dx[k]
                        newY = y + dy[k]
                        if 0<=newX<n and 0<=newY<n and not visited[newX][newY]:
                            # 같은섬
                            if mapp[newX][newY] == island:
                                visited[newX][newY] = True
                            # 바다
                            elif mapp[newX][newY] == 0:
                                q.append([newX, newY, cost+1])
                                visited[newX][newY] = True
                            # 가장 가까운 다른섬
                            else:
                                ans = min(ans, cost)
                                q.clear()
                                break
    return ans


def solution():
    n = int(input())
    mapp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        inline = list(map(int, input().split()))
        for j, el in enumerate(inline):
            mapp[i][j] = el

    mapp = markingIsland(mapp, n)
    print(findNearest(mapp, n))





solution()