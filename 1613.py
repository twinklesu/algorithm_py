import sys
input = sys.stdin.readline


n, k = map(int, input().split())
matrix = [[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(k):
    pre, post = map(int,input().split())
    matrix[pre][post] = -1
    matrix[post][pre] = 1

# 플로이드워셜
for mid in range(1, n+1):
    for start in range(1, n+1):
        for end in range(1, n+1):
            if matrix[start][end] == 0 and matrix[start][mid] != 0:
                if matrix[start][mid] == matrix[mid][end]:
                    matrix[start][end] = matrix[start][mid]

s = int(input())
for _ in range(s):
    u, v = map(int, input().split())
    print(matrix[u][v])
