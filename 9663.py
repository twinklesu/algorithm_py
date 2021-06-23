def dfs(n, k, board):
    global count
    if k == n:
        count += 1
        return
    for i in range(n): # 열
        for j in range(k): # 이전의 행에 접근하기 위한
            if i == board[j] or abs(k-j) == abs(i-board[j]):
                break
        else:
            board[k] = i
            dfs(n, k+1, board)


def main():
    global count
    n = int(input())
    board = [-1 for _ in range(n)]

    count = 0
    dfs(n, 0, board)

    print(count)


main()