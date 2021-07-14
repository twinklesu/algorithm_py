def transform(matrix: list, x: int, y:int):
    newMatrix = matrix.copy()
    for i in range(3):
        for j in range(3):
            newMatrix[x+i][y+j] = 0 if matrix[x+i][y+j] == 1 else 1
    return newMatrix


n, m = map(int, input().split())
a = [list(map(int, input())) for _ in range(n)]
b = [list(map(int, input())) for _ in range(n)]
count = 0
for i in range(n-2):
    for j in range(m-2):
        if a[i][j] != b[i][j]:
            count += 1
            a = transform(a, i, j)

for aa, bb in zip(a, b):
    if aa != bb:
        print(-1)
        break
else:
    print(count)





