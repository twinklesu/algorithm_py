global white, blue


def dfs(matrix, n):
    global white, blue
    w, b = 0, 0
    for line in matrix:
        w += line.count(0)
        b += line.count(1)
    if w == 0:
        blue += 1
    elif b == 0:
        white += 1
    else:
        temp1 = []
        temp2 = []
        for i in range(n//2):
            temp1.append(matrix[i][:n//2])
            temp2.append(matrix[i][n//2:])
        dfs(temp1, n//2)
        dfs(temp2, n//2)
        temp1 = []
        temp2 = []
        for i in range(n//2, n):
            temp1.append(matrix[i][:n//2])
            temp2.append(matrix[i][n//2:])
        dfs(temp1, n//2)
        dfs(temp2, n//2)



def main():
    n = int(input())
    matrix = []
    for _ in range(n):
        line = list(map(int, input().split()))
        matrix.append(line)
    global white, blue
    white = 0
    blue = 0
    dfs(matrix, n)
    print(white)
    print(blue)


main()