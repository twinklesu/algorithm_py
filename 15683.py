from copy import deepcopy
from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
room = [[0 for _ in range(m)] for _ in range(n)]
cameras = []
for i in range(n):
    line = list(map(int, input().split()))
    for j, el in enumerate(line):
        if 1<= el < 6:
            cameras.append((i,j,el))
            room[i][j] = 1
        if el == 6:
            room[i][j] = 6

one = [[0], [1], [2], [3]] # 동 서 남 북
two = [[0,1], [2,3]]
three = [[0,2], [1,2], [1,3], [0,3]]
four = [[0,1,2], [1,2,3], [0,1,3], [0,2,3]]
five = [[0,1,2,3]]
cams = [None, one, two, three, four, five]


combinations = []
def comb(cameras, combination, k):
    if k == len(cameras):
        combinations.append(combination)
        return
    cam = cameras[k][2]
    for direction in cams[cam]:
        comb(cameras, combination + [direction], k+1)


comb(cameras, [], 0)

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
minCount = 100
for c in combinations:
    copiedRoom = deepcopy(room)
    for camera, direction in zip(cameras, c):
            for d in direction:
                q = deque()
                q.append([camera[0],camera[1]])
                while q:
                    temp = q.popleft()
                    newX = temp[0] + dx[d]
                    newY = temp[1] + dy[d]
                    if 0 <= newX < n and 0<=newY<m and 0<=copiedRoom[newX][newY]<=1:
                        copiedRoom[newX][newY] = 1
                        q.append([newX, newY])
    # 사각지대 갯수 세기
    count = 0
    for i in range(n):
        for j in range(m):
            if copiedRoom[i][j] == 0:
                count += 1
    minCount = min(minCount, count)


print(minCount)

