from collections import deque


def bfs(grid: list, node: list, n: int, m: int):
    q = deque()
    q.append(node)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while q:
        temp = q.popleft()
        grid[temp[0]][temp[1]] = 0
        for dxx, dyy in zip(dx, dy):
            newX = temp[0] + dxx
            newY = temp[1] + dyy
            if 0 <= newX < n and 0 <= newY < m and grid[newX][newY] == 1 and [newX, newY] not in q:
                q.append([newX, newY])


def solution():
    m, n, k = map(int, input().split())
    grid = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        grid[y][x] = 1

    count = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                bfs(grid, [i, j], n, m)
                count += 1
    print(count)


def main():
    t = int(input())
    for _ in range(t):
        solution()


main()
