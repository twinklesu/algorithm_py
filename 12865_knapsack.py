n, k = map(int, input().split())
item = [[0,0]] + [list(map(int, input().split())) for _ in range(n)]
knapsack = [[0 for _ in range(k+1)] for _ in range(n+1)]

for i in range(1, n+1):
    w, v = item[i]
    for j in range(1, k+1):
        if w <= j: # 얘를 가방에 넣을 수 있다
            leftW = j-w
            knapsack[i][j] = max(knapsack[i-1][j], knapsack[i-1][leftW] + v) # 안넣었을 때 최대, 넣었을 때 최대
        else:
            knapsack[i][j] = knapsack[i - 1][j]

print(knapsack[-1][-1])

