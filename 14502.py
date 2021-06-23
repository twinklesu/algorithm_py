from collections import deque
from copy import deepcopy

def count_free(mapp,m):
    count = 0
    for i in range(m):
        count += mapp[i].count(0)
    return count


def infect(mapp, n, m):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[False for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if mapp[i][j] == 2 and not visited[i][j]:
                q = deque()
                q.append([i,j])
                while q:
                    temp = q.popleft()
                    visited[temp[0]][temp[1]] = True
                    for k in range(4):
                        x = temp[0] + dx[k]
                        y = temp[1] + dy[k]
                        if 0<=x<m and 0<=y<n and mapp[x][y] != 1 and not visited[x][y] and [x,y] not in q:
                            q.append([x,y])
                            if mapp[x][y] == 0:
                                mapp[x][y] = 2
    return count_free(mapp, m)


def main():
    m, n = map(int, input().split())
    mapp = [[0 for _ in range(n)] for _ in range(m)]
    zeroIndex = []
    for i in range(m):
        line = list(map(int, input().split()))
        for j, el in enumerate(line):
            if el != 0:
                mapp[i][j] = el
            else:
                zeroIndex.append([i,j])

    max_free = 0
    lenZero = len(zeroIndex)
    for i in range(lenZero-2):
        for j in range(i+1, lenZero-1):
            for k in range(j+1, lenZero):
                new_mapp = deepcopy(mapp)
                new_mapp[zeroIndex[i][0]][zeroIndex[i][1]] = 1
                new_mapp[zeroIndex[j][0]][zeroIndex[j][1]] = 1
                new_mapp[zeroIndex[k][0]][zeroIndex[k][1]] = 1
                count = infect(new_mapp, n, m)
                if count > max_free:
                    max_free = count
    print(max_free)


main()
