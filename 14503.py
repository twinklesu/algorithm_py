n, m = map(int, input().split())
nowX, nowY, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]


def findingNextMove(x, y, d):
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]
    return x + dx[d], y + dy[d]


count = 0

while True:
    if room[nowX][nowY] == 0:
        count += 1
        room[nowX][nowY] = 2
    newD = (d + 3) % 4
    newX, newY = findingNextMove(nowX, nowY, newD)
    newSpace = room[newX][newY]
    nowX, nowY, d = newX, newY, newD
    if newSpace != 0:
        for _ in range(3):
            newD = (newD + 3) % 4
            newX, newY = findingNextMove(nowX, nowY, newD)
            newSpace = room[newX][newY]
            if newSpace == 0:
                nowX, nowY, d = newX, newY, newD
                break
        else:
            newD = (newD + 2) % 4
            newX, newY = findingNextMove(nowX, nowY, newD)
            newSpace = room[newX][newY]
            if newSpace == 1:
                break
            else:
                nowX, nowY, d = newX, newY, newD

print(count)
