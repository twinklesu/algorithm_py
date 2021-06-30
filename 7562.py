from collections import deque
import sys

input = sys.stdin.readline

dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [-1, 1, -1, 1, -2, 2, -2, 2]


def solution():
    i = int(input())
    start = list(map(int, input().rstrip().split()))
    end = list(map(int, input().rstrip().split()))
    visited = [[False for _ in range(i)] for _ in range(i)]

    # bfs
    q = deque()
    q.append(start + [0])
    while q:
        temp = q.popleft()
        x, y, count = map(int, temp)
        if [x,y] == end:
            return count
        visited[x][y] = True
        for ind in range(8):
            newX = x+dx[ind]
            newY = y+dy[ind]
            if 0<=newX<i and 0<=newY<i and not visited[newX][newY] and [newX, newY] not in q:
                q.append([newX, newY, count+1])



def main():
    t = int(input())
    for _ in range(t):
        print(solution())


main()
