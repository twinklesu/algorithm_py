from collections import deque

def main():
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    r, c = map(int, input().split())
    s = deque()
    q = deque()  # waters
    d = []
    waterVisited = [[0 for _ in range(c)] for _ in range(r)]
    sVisited = [[0 for _ in range(c)] for _ in range(r)]
    for i in range(r):
        forest = input()
        for j in range(c):
            if forest[j] == 'S':  # 고슴도치면
                s.append([i, j, 0])  # 좌표, 시간
                sVisited[i][j] = 1
            elif forest[j] == 'D':  # 비버집이면
                sVisited[i][j] = 2
                waterVisited[i][j] = 1  # 물은 비버집 접근 못함
            elif forest[j] == '*':  # 물이면
                q.append((i, j))  # bfs 위한 큐
                waterVisited[i][j] = 1
                sVisited[i][j] = 1  # 어차피 고슴도치는 물 있는 곳 못가
            elif forest[j] == 'X':
                waterVisited[i][j] = 1  # 물 접근 못하니까 이미 방문한걸로
                sVisited[i][j] = 1  # 고슴도치도 돌에 접근 못함

    while s:
        newQ = deque()
        # 홍수 bfs
        for temp in q:
            for i in range(4):
                newX = temp[0] + dx[i]
                newY = temp[1] + dy[i]
                if 0 <= newX < r and 0 <= newY < c and waterVisited[newX][newY] == 0:
                    waterVisited[newX][newY] = 1
                    sVisited[newX][newY] = 1 # 물 퍼지면 고슴도치 못 가
                    newQ.append((newX, newY))
        q = newQ
        # 고슴도치 옮기기
        newS = []
        for ss in s:
            for i in range(4):
                newX = ss[0] + dx[i]
                newY = ss[1] + dy[i]
                if 0 <= newX < r and 0 <= newY < c:
                    if sVisited[newX][newY] == 2:  # d 를 2로 해뒀으니까
                        print(ss[2] + 1)
                        return
                    elif sVisited[newX][newY] == 0:
                        sVisited[newX][newY] = 1
                        newS.append([newX, newY, ss[2] + 1])
        s = newS
    else:
        print('KAKTUS')


main()