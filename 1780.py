import sys
input = sys.stdin.readline


def solution(paper: list, row: int, col: int, n: int):
    global globalCount
    count = [0,0,0]
    numberSet = set()
    for i in range(n):
        numberSet.update(paper[row+i][col:col+n])

    if len(numberSet) == 1:
        num = numberSet.pop()
        globalCount[num+1] += 1
        return
    n//=3
    for i in range(3):
        for j in range(3):
            solution(paper, row+n*i, col+n*j, n)


def main():
    global globalCount
    n = int(input())
    paper = [list(map(int, input().split())) for _ in range(n)]
    globalCount = [0,0,0]
    solution(paper, 0, 0, n)
    print(*globalCount, sep='\n')


main()