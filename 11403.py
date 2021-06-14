import sys
input = sys.stdin.readline
from collections import deque


def main():
    n = int(input())
    table = [[0 for _ in range(n)] for _ in range(n)]
    lookingForQ = deque()

    for i in range(n):
        line = list(map(int, input().rstrip().split()))
        for j, el in enumerate(line):
            table[i][j] = el
            if el == 0:
                lookingForQ.append((i,j))

    doingUpdate = True
    while doingUpdate and lookingForQ:
        doingUpdate = False
        thisTurnQ = lookingForQ.copy()
        lookingForQ.clear()
        while thisTurnQ:
            node = thisTurnQ.popleft()
            possiblePath = []
            for ind, el in enumerate(table[node[0]]):
                if el == 1:
                    possiblePath.append(ind)
            for pp in possiblePath:
                if table[pp][node[1]] == 1:
                    table[node[0]][node[1]] = 1
                    doingUpdate = True
                    break
            else:
                lookingForQ.append(node)
    for t in table:
        print(*t)




main()
