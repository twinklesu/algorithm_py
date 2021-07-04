import sys

input = sys.stdin.readline

tetromino = [[] for _ in range(19)]
tetromino[0] = [[0, 0, 0, 0], [0, 1, 2, 3]]
tetromino[1] = [[0, 1, 2, 3], [0, 0, 0, 0]]

tetromino[2] = [[0, 1, 0, 1], [0, 0, 1, 1]]

tetromino[3] = [[0, 0, 0, 1], [0, 1, 2, 2]]
tetromino[4] = [[0, 1, 1, 1], [2, 0, 1, 2]]
tetromino[5] = [[0, 1, 2, 2], [1, 1, 1, 0]]
tetromino[6] = [[0, 1, 2, 2], [0, 0, 0, 1]]
tetromino[7] = [[0, 1, 1, 1], [0, 0, 1, 2]]
tetromino[8] = [[0, 0, 0, 1], [2, 1, 0, 0]]
tetromino[9] = [[0, 0, 1, 2], [1, 0, 0, 0]]
tetromino[10] = [[0, 0, 1, 2], [0, 1, 1, 1]]

tetromino[11] = [[0, 0, 1, 1], [0, 1, 1, 2]]
tetromino[12] = [[0, 1, 1, 2], [1, 1, 0, 0]]
tetromino[13] = [[0, 0, 1, 1], [2, 1, 1, 0]]
tetromino[14] = [[0, 1, 1, 2], [0, 0, 1, 1]]

tetromino[15] = [[0, 1, 2, 1], [0, 0, 0, 1]]
tetromino[16] = [[0, 1, 2, 1], [1, 1, 1, 0]]
tetromino[17] = [[0, 0, 0, 1], [0, 1, 2, 1]]
tetromino[18] = [[1, 0, 0, 0], [0, 1, 2, 1]]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

maxi = 0
for i in range(n):
    for j in range(m):
        for tet in tetromino:
            count = 0
            for t in range(4):
                newX, newY = i + tet[0][t], j + tet[1][t]
                if 0 <= newX < n and 0 <= newY < m:
                    count += board[newX][newY]
                else:
                    break
            else:
                maxi = max(maxi, count)

print(maxi)
