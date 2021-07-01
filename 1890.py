from collections import deque
import sys
input = sys.stdin.readline


# def dfs(board: list, n: int, x: int, y: int, path: list):
#     global count
#     move = board[x][y]
#     if move == 0:
#         count += 1
#         px, py = path[-1]
#         board[px][py] = 0
#         return
#     newX = x + move
#     newY = y + move
#     if 0<= newX < n:
#         dfs(board, n, newX, y, path+[[newX, y]])
#     if 0<= newY < n:
#         dfs(board, n, x, newY, path+[[x, newY]])


def dfs(board:list, n:int):
    global count
    stack = deque()
    stack.append([0,0])
    while stack:
        x, y = stack.popleft()
        move = board[x][y]
        newX = x + move
        newY = y + move
        if 0<= newX < n:
            if board[newX][y] != 0:
                if [newX,y] not in stack:
                    stack.append([newX,y])
        if 0<= newY < n:
            if board[x][newY] != 0:
                if [x,newY] not in stack:
                    stack.append([x,newY])


def main():
    global count
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]

    stack = deque()
    stack.append([0,0])

    # dfs
    count = 0
    # dfs(board, n, 0, 0, [])
    dfs(board, n)
    print(count)


main()