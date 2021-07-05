import sys
input = sys.stdin.readline


def dfs(costMatrix:list, cost: int, path: list, lenPath: int, n: int, fromCity: int):
    global minCost
    if lenPath == n:
        returnCost = costMatrix[fromCity][path[0]]
        if returnCost != 0:
            minCost = min(minCost, cost+returnCost)
        return

    lenPath += 1
    for i in range(n):
        if i not in path:
            movingCost = costMatrix[fromCity][i]
            if movingCost != 0:
                costMatrix[fromCity][i] = 0
                dfs(costMatrix, cost + movingCost, path+[i], lenPath, n, i)
                costMatrix[fromCity][i] = movingCost


def main():
    global minCost
    n = int(input())
    costMatrix = [list(map(int, input().split())) for _ in range(n)]

    minCost = 10**7
    for i in range(n):
        dfs(costMatrix, 0, [i], 1, n, i)
    print(minCost)


main()
