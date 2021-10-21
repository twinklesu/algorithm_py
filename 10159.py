n = int(input())
m = int(input())

costMatrix = [[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    costMatrix[u][v] = 2
    costMatrix[v][u] = 1

# 플로이드 워셜
for mid in range(1, n+1):
    for start in range(1, n+1):
        for end in range(1, n+1):
            if costMatrix[start][end] == 0 and costMatrix[start][mid] == costMatrix[mid][end]:
                costMatrix[start][end] = costMatrix[start][mid]

for i in range(1,n+1):
    print(costMatrix[i][1:].count(0)-1) # 자기 자신 빼고

