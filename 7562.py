from collections import deque
import sys

input = sys.stdin.readline

dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [-1, 1, -1, 1, -2, 2, -2, 2]


def solution():
    i = int(input())
    start = list(map(int, input().rstrip().split()))
    end = list(map(int, input().rstrip().split()))
    visited = [[0 for _ in range(i)] for _ in range(i)]

    # bfs
    q = deque()
    q.append(start)
    while q:
        temp = q.popleft()
        x, y = map(int, temp)
        if [x,y] == end:
            return visited[x][y]
        count = visited[x][y]
        for ind in range(8):
            newX = x+dx[ind]
            newY = y+dy[ind]
            if 0<=newX<i and 0<=newY<i and visited[newX][newY] == 0:
                visited[newX][newY] = count + 1 # 여기서 visited 계산하는게 더 빠름
                q.append([newX, newY])



def main():
    t = int(input())
    for _ in range(t):
        print(solution())


main()
