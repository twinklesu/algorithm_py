n, m, x, y, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
moves = list(map(int, input().split()))
dice = [0 for _ in range(6)]
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

def roll(move: int , dice: list):
    if move == 1:
        return [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
    elif move == 2:
        return [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
    elif move == 3:
        return [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
    else:
        return [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]

if board[x][y] != 0:
    dice[5] = board[x][y]

for move in moves:
    newX = x+dx[move]
    newY = y+dy[move]
    if 0<=newX<n and 0<=newY<m:
        x, y = newX, newY
        dice = roll(move, dice)
        if board[x][y] == 0:
            board[x][y] = dice[5]
        else:
            dice[5] = board[x][y]
            board[x][y] = 0
        print(dice[0])
