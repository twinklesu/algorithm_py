from collections import deque

def setZeroes(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    nRow = len(matrix)
    nCol = len(matrix[0])
    # 0인 곳의 인덱스 찾기
    zeroIndices = []
    for row, li in enumerate(matrix):
        for col, el in enumerate(li):
            if el == 0:
                zeroIndices.append([row, col])
    # 인덱스 이용해서 행과 열의 값 변경
    for row, col in zeroIndices:
        # 행 값 변경
        for c in range(nCol):
            matrix[row][c] = 0
        # 열 값 변경
        for r in range(nRow):
            matrix[r][col] = 0



def heedo_review(matrix):
    # 희도 코드 리뷰
    nRow = len(matrix)
    nCol = len(matrix[0])
    xSet = set()
    ySet = set()
    for row, li in enumerate(matrix):
        for col, el in enumerate(li):
            if el == 0:
                xSet.add(row)
                ySet.add(col)
    for x in xSet:
        for c in range(nCol):
            matrix[x][c] = 0
    for y in ySet:
        for r in range(nRow):
            matrix[r][y]
