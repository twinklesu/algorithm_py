from collections import deque


n = int(input())
k = int(input())
apples = []
for _ in range(k):
    a, b = map(int, input().split())
    apples.append((a-1, b-1))
l = int(input())
turn = dict()
for _ in range(l):
    line = input().split()
    turn[int(line[0])] = line[1]

seconds = 0
movingDirection = [[0,1], [-1,0], [0,-1], [1,0]] # e, n, w, s
direction = 0
snake = deque()
snake.append((0,0))
while True:
    seconds += 1
    head = snake[0]
    newHead = (head[0]+movingDirection[direction][0], head[1]+movingDirection[direction][1])

    if newHead in snake or not 0<=newHead[0]<n or not 0<=newHead[1]<n:
        # 종료 조건
        break

    snake.appendleft(newHead)
    if newHead in apples:
        apples.remove(newHead)
    else:
        snake.pop()

    if seconds in turn:
        turning = turn.pop(seconds)
        if turning == 'D':
            direction = (direction-1)%4
        else:
            direction = (direction+1)%4

print(seconds)