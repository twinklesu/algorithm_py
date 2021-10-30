from heapq import heappop, heappush

n, m = map(int, input().split())
byte = list(map(int, input().split()))
cost = list(map(int, input().split()))

item = []
heappush(item, [0,0])
for i in range(n):
    heappush(item, [cost[i],byte[i]])
knapsackList = []
while item:
    knapsackList.append(heappop(item))

costMatrix = [[0 for _ in range(m+1)] for _ in range(n+1)]

for row in range(1, n+1):
    for col in range(m+1):
        if knapsackList[row][1] <= col:
            leftByte = col - knapsackList[row][1]
            costMatrix[row][col] = max(costMatrix[row-1][col], costMatrix[row-1][leftByte]+knapsackList[row][0])
        else:
            costMatrix[row][col] = costMatrix[row-1][col]

print(costMatrix[-1][-1])