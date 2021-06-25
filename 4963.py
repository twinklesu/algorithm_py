from collections import deque


def stackDfs(mapp: list, n: int, m: int):
    count = 0
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    for i in range(m):
        for j in range(n):
            if mapp[i][j] == 1:
                stack = deque()
                stack.append([i,j])
                while stack:
                    top = stack.pop()
                    mapp[top[0]][top[1]] = 0
                    for k in range(8):
                        x = top[0] + dx[k]
                        y = top[1] + dy[k]
                        if 0<=x<m and 0<=y<n and mapp[x][y] == 1 and [x,y] not in stack:
                            stack.append([x,y])
                count += 1
    return count


def main():
    while True:
        n, m = map(int, input().split())
        if n == 0 or m == 0:
            break
        mapp = [list(map(int, input().split())) for _ in range(m)]
        print(stackDfs(mapp, n, m))


main()