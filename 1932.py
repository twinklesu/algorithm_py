import sys
input = sys.stdin.readline

n = int(input())

triangle = []

for _ in range(n):
    line = list(map(int, input().rstrip().split()))
    triangle.append(line)

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            triangle[i][j] += triangle[i-1][j]
        elif j == i:
            triangle[i][j] += triangle[i-1][j-1]
        else:
            triangle[i][j] += max([triangle[i-1][j], triangle[i-1][j-1]])

print(max(triangle[-1]))