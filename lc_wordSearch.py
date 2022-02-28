from collections import deque
from copy import copy

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def exist( board, word: str) -> bool:
    global isExist
    rowN = len(board)
    colN = len(board[0])
    wordLen = len(word)

    possibleStart = []
    for row, li in enumerate(board):
        for col, el in enumerate(li):
            if el == word[0]:
                possibleStart.append([row, col])

    for startR, startC in possibleStart:
        visited = set()
        visited.add((startR, startC))
        if wordLen == 1:
            return True
        else:
            isExist = False
            dfs(board, word, 0, startR, startC, visited, rowN, colN, wordLen)
        if isExist:
            return True
    return False


def dfs(board, word, count, r, c, visited, rowN, colN, wordLen):
    global isExist
    count += 1
    if count < wordLen:
        for k in range(4):
            newR = r + dx[k]
            newC = c + dy[k]
            if 0<=newR<rowN and 0<=newC<colN and (newR, newC) not in visited and board[newR][newC] == word[count]:
                if count+1 == wordLen:
                    isExist = True # flag
                    return
                newV = copy(visited)
                newV.add((newR,newC))
                dfs(board, word, count, newR, newC, newV, rowN, colN, wordLen)



board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
print(exist(board, word))