def checkPossible(road: list, n: int, l: int):
    visited = [0 for _ in range(n)] # 경사로가 놓여지면 거긴 1됨
    flag = True
    pointer = 0
    while flag and pointer < n-1:
        # 내려가는 방향으로
        if road[pointer] == road[pointer +1] + 1:
            pointer += 1
            for j in range(l):
                if pointer+j < n and road[pointer+j] == road[pointer] and visited[pointer+j] == 0:
                    pass
                else:
                    flag = False
                    break
            else:
                visited[pointer:pointer+l] = [1]*l
                pointer += l-1
        # 높이 같아
        elif road[pointer] == road[pointer+1]:
            pointer += 1
        # 올라가는 경사로
        elif road[pointer] == road[pointer+1] - 1:
            for j in range(l):
                if pointer - j >= 0 and road[pointer-j] == road[pointer] and visited[pointer-j] == 0:
                    pass
                else:
                    flag = False
                    break
            else:
                visited[pointer-l+1:pointer+1] = [1]*l
                pointer += 1
        else:
            flag = False

    if flag:
        return 1
    else:
        return 0

n, l = map(int, input().split())
board = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    line = list(map(int, input().split()))
    for j, el in enumerate(line):
        board[i][j] = el

ans = 0
for i in range(n):
    ans += checkPossible(board[i], n, l)
for i in range(n):
    temp = [0 for _ in range(n)]
    for j in range(n):
        temp[j] = board[j][i]
    ans += checkPossible(temp, n, l)
print(ans)