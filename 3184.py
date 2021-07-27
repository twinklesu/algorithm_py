from collections import deque

n, m = map(int, input().split())
field = [list(map(str, input())) for _ in range(n)]

sheep = set()
wolves = set()
space = []
dx = [0,0,-1,1]
dy = [1,-1,0,0]
for i in range(1, n-1):
    for j in range(1, m-1): # 어차피 맨 끝은 범위로 생각 안함
        if field[i][j] == 'o':
            sheep.add((i,j))
        elif field[i][j] == 'v':
            wolves.add((i,j))
        if field[i][j] != '#':
            # bfs
            temp = set()
            q = deque()
            q.append([i,j])
            field[i][j] = '#' # 방문했으니 울타리로 마킹
            flag = True
            while q and flag:
                x, y = map(int, q.popleft())
                temp.add((x,y))
                for k in range(4):
                    newX = x+dx[k]
                    newY = y+dy[k]
                    if field[newX][newY] != '#': # 늑대랑 양도 영역으로 세야하니까
                        if 1<=newX<n-1 and 1<=newY<m-1:
                            if field[newX][newY] == 'o':
                                sheep.add((newX, newY))
                            elif field[newX][newY] == 'v':
                                wolves.add((newX, newY))
                            field[newX][newY] = '#'
                            q.append([newX, newY])
                        else:
                            flag = False
                            break
            else:
                space.append(temp)


totalS = 0
totalW = 0
for oneSpace in space:
    sCount = len(oneSpace.intersection(sheep))
    wCount = len(oneSpace.intersection(wolves))
    if sCount > wCount:
        totalS += sCount
    else:
        totalW += wCount

print(totalS, totalW)