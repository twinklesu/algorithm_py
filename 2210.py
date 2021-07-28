board = [list(map(int, input().split())) for _ in range(5)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

ans = set()


def recursion(numbers: str, length: int, x: int, y: int):
    if length == 6:
        ans.add(numbers)
        return
    
    for i in range(4):
        newX = x + dx[i]
        newY = y + dy[i]
        if 0 <= newX < 5 and 0 <= newY < 5:
            recursion(numbers + str(board[newX][newY]), length + 1, newX, newY)


for i in range(5):
    for j in range(5):
        recursion(str(board[i][j]), 1, i, j)

print(len(ans))
