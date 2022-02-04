def spiralOrder(matrix):
    m = len(matrix)
    n = len(matrix[0])

    x, y = 0, 0
    answer = []

    while n > 1 and m > 1:
        # top row
        for dy in range(y, y + n - 1):
            answer.append(matrix[x][dy])
        # right col
        for dx in range(x, x + m - 1):
            answer.append(matrix[dx][y + n - 1])
        # bottom row
        for dy in range(y + n - 1, y, -1):
            answer.append(matrix[x + m - 1][dy])
        # left col
        for dx in range(x + m - 1, x, -1):
            answer.append(matrix[dx][y])
        n -= 2
        m -= 2
        x += 1
        y += 1

    if n == 1:
        if m == 1:
            # 1*1
            answer.append(matrix[x][y])
        else:
            # 1*m (col)
            for dx in range(x, x + m):
                answer.append(matrix[dx][y])
    else:
        if m == 1:
            # n*1 (row)
            for dy in range(y, y + n):
                answer.append(matrix[x][dy])

    return answer


matrix = []
count = 1
for i in range(10):
    temp = []
    for j in range(2):
        temp.append(count)
        count += 1
    matrix.append(temp)
    temp = []
print(spiralOrder(matrix))
