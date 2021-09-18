import sys
input = sys.stdin.readline
from collections import deque


def distance(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])


t = int(input())
for _ in range(t):
    n = int(input())
    start = tuple(map(int, input().split()))
    store = []
    for _ in range(n):
        store.append((tuple(map(int, input().split()))))
    end = tuple(map(int, input().split()))
    store = [start] + store + [end]


    # 플로이드 워셜
    INF = 1001
    costMatrix = [[INF for _ in range(n+2)] for _ in range(n+2)]
    for i in range(n+2):
        for j in range(n+2):
            if distance(store[i], store[j]) <= 1000:
                costMatrix[i][j] = 0

    for mid in range(n+2):
        for start in range(n+2):
            for end in range(n+2):
                newD = costMatrix[start][mid] + costMatrix[mid][end]
                if newD <= 1000:
                    costMatrix[start][end] = 0

    if costMatrix[0][-1] != 0:
        print("sad")
    else:
        print("happy")

