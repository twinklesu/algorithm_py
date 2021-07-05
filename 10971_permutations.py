import sys
input = sys.stdin.readline
from itertools import permutations


def main():
    global minCost
    n = int(input())
    costMatrix = [list(map(int, input().split())) for _ in range(n)]

    minCost = 10**7

    perm = permutations(range(n))
    for p in perm:
        cost = 0
        for i in range(n-1):
            movingCost = costMatrix[p[i]][p[i+1]]
            if movingCost != 0:
                cost += movingCost
            else:
                break
        else:
            movingCost = costMatrix[p[-1]][p[0]]
            if movingCost != 0:
                cost += movingCost
                minCost = min(minCost, cost)

    print(minCost)


main()
