from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(picture: list, n: int, startX: int, startY: int):
    count = 1
    q = deque()
    q.append([startX, startY])
    color = picture[startX][startY]
    picture[startX][startY] = ''
    while q:
        x, y = q.popleft()
        for i in range(4):
            newX, newY = x + dx[i], y + dy[i]
            if 0 <= newX < n and 0 <= newY < n and picture[newX][newY] == color:
                picture[newX][newY] = ''
                q.append([newX, newY])
    return count


def main():
    n = int(input())
    original = [[] for _ in range(n)]
    changed = [[] for _ in range(n)]

    for i in range(n):
        line = input()
        original[i] = list(map(str, line))
        line = line.replace('R', 'G')
        changed[i] = list(map(str, line))

    originalCount = 0
    changedCount = 0
    for i in range(n):
        for j in range(n):
            if original[i][j] != '':
                bfs(original, n, i, j)
                originalCount += 1

            if changed[i][j] != '':
                bfs(changed, n, i, j)
                changedCount +=1

    print(originalCount, changedCount)

main()