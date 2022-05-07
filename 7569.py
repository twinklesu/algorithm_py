# from collections import deque
# import sys
# input = sys.stdin.readline
#
#
# n, m, h = map(int, input().split())
# box = [[[0 for _ in range(n)] for _ in range(m)] for _ in range(h)]
# newRipen = deque()
# for i in range(h):
#     for j in range(m):
#         line = list(map(int, input().split()))
#         for k, el in enumerate(line):
#             box[i][j][k] = el
#             if el == 1:
#                 newRipen.append([i, j, k])
#
# days = -1 # q에 남는게 없을 때 끝나니까 -1 로 시작
# ripen = deque()
# dx = [1, -1, 0, 0, 0, 0]
# dy = [0, 0, 1, -1, 0, 0]
# dz = [0, 0, 0, 0, -1, 1]
# while newRipen:
#     ripen = newRipen.copy()
#     newRipen.clear()
#     days += 1 # 첫날에 다 익었을 경우 여기서 0 됨
#     while ripen:
#         x, y, z = ripen.popleft()
#         for i in range(6):
#             newX = x + dx[i]
#             newY = y + dy[i]
#             newZ = z + dz[i]
#             if 0<=newX<h and 0<=newY<m and 0<=newZ<n and box[newX][newY][newZ] == 0:
#                 box[newX][newY][newZ] = 1  # 방문
#                 newRipen.append([newX, newY, newZ])
#
#
# flag = False
# for i in range(h):
#     for j in range(m):
#         if 0 in box[i][j]:
#             print(-1)
#             flag = True
#             break
#     if flag:
#         break
# else:
#     print(days)
#
# # 4 3 2
# # 1 1 1 1
# # 1 1 1 1
# # -1 -1 -1 1
# # 1 1 1 1
# # -1 -1 -1 -1
# # 0 0 0 -1


from collections import deque
from copy import deepcopy

m, n, h = map(int, input().split())
box = [[[0 for _ in range(m)] for _ in range(n)] for _ in range(h)]
newQ = deque()
tomato = 0
for z in range(h):
    for y in range(n):
        for x, el in enumerate(map(int, input().split())):
            if el == 1:
                newQ.append((z, y, x))
            if el == 0:
                tomato += 1
            box[z][y][x] = el
dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]
count = -1
while newQ:
    q = deepcopy(newQ)
    newQ.clear()
    count += 1
    while q:
        x, y, z = q.popleft()
        for i in range(6):
            newX = x + dx[i]
            newY = y + dy[i]
            newZ = z + dz[i]
            if 0 <= newX < h and 0 <= newY < n and 0 <= newZ < m and box[newX][newY][newZ] == 0:
                box[newX][newY][newZ] = 1
                tomato -= 1
                newQ.append((newX, newY, newZ))

if tomato == 0:
    print(count)
else:
    print(-1)

