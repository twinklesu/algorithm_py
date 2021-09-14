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
    ans = "sad"
    # 플로이드 워셜
    INF = 1001
    costMatrix = [[INF for _ in range(n+2)] for _ in range(n+2)]
    for fromm in range(n+2):
        for dest in range(n+2):
            # costMatrix[fromm][dest] = min(costMatrix[fromm][dest], distance(store[fromm], store[dest]))
            if distance(store[fromm], store[dest]) <= 1000:
                costMatrix[fromm][dest] = 0

    for fromm in range(n+2):
        for dest in range(n+2):
            for mid in range(n+2):
                # costMatrix[fromm][dest] = min(costMatrix[fromm][dest], costMatrix[fromm][mid]+costMatrix[mid][dest])
                if costMatrix[fromm][mid] + costMatrix[mid][dest] <= 1000:
                    costMatrix[fromm][dest] = 0
    if costMatrix[0][-1] <= 1000:
        print("happy")
    else:
        print("sad")

