from collections import deque


wheel =  [deque(map(int, input())) for _ in range(4)]
wheel = [None] + wheel
t = int(input())
for _ in range(t):
    startWheel, direction = map(int, input().split())
    moves = [0]*5
    moves[startWheel] = direction
    # 시작 부터 왼쪽 방향으로 확인
    beforeWheel = startWheel
    beforeDirection = direction
    for i in range(startWheel-1, 0, -1):
        if wheel[i][2] == wheel[beforeWheel][6]:
            break
        else:
            beforeWheel = i
            beforeDirection = 1 if beforeDirection == -1 else -1
            moves[i] = beforeDirection
    # 시작부터 오른쪽 방향으로 확인
    beforeWheel = startWheel
    beforeDirection = direction
    for i in range(startWheel+1, 5):
        if wheel[beforeWheel][2] == wheel[i][6]:
            break
        else:
            beforeWheel = i
            beforeDirection = 1 if beforeDirection == -1 else -1
            moves[i] = beforeDirection

    # 여기서부터 톱니 회전
    for i in range(1,5):
        wheel[i].rotate(moves[i])


# 점수
ans = 0
for i in range(1,5):
    if wheel[i][0] == 1:
        ans += 2**(i-1)

print(ans)
