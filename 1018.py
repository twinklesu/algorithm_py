white = ['W', 'B']*4
black = ['B', 'W']*4
w_board = [white, black]*4
b_board = [black, white]*4
board = []

n, m = map(int, input().split(' '))

for _ in range(n):
    board.append(list(map(str, input())))

minList = []

for i in range(n-7):
    for j in range(m-7):
        needFix1 = 0
        needFix2 = 0
        for s in range(8):
            for t in range(8):
                if board[i+s][j+t] != w_board[s][t]:
                    needFix1 += 1
                if board[i+s][j+t] != b_board[s][t]:
                    needFix2 += 1
        minList.append(needFix1)
        minList.append(needFix2)

print(min(minList))
