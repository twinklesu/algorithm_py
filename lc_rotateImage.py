from collections import deque

def rotate(matrix) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)
    q = deque()
    for i in range(n):
        for j in range(n):
            q.append(matrix[i][j])

    for col in range(n - 1, -1, -1):
        for row in range(n):
            matrix[row][col] = q.popleft()


def rotate2(matrix) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    for ind, el in enumerate(zip(*matrix[::-1])):
        matrix[ind] = list(el)