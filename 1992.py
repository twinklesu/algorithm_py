# def solution(video: list, n: int, startX, startY):
#     checkUniqueSet = set()
#     for i in range(startX, startX+n):
#         for j in range(startY, startY+n):
#             checkUniqueSet.add(video[i][j])
#     if len(checkUniqueSet) == 1:
#         return str(checkUniqueSet.pop())
#     n//=2
#     return "(" + solution(video, n, startX, startY) + solution(video, n, startX, startY+n) + solution(video, n, startX+n, startY) + solution(video, n, startX+n, startY+n) + ")"
#
#
# n = int(input())
# video = [[0 for _ in range(n)] for _ in range(n)]
# for i in range(n):
#     line = list(map(int, input()))
#     for j, el in enumerate(line):
#         video[i][j] = el
#
# print(solution(video, n, 0, 0))

n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input())))

def recursion(n, startX, startY):
    isAllSame = True
    color = matrix[startX][startY]
    for i in range(n):
        for j in range(n):
            if matrix[startX + i][startY + j] != color:
                isAllSame = False
    if isAllSame:
        return str(color)
    else:
        return "(" + recursion(n//2, startX, startY) + recursion(n//2, startX, startY+n//2) + recursion(n//2, startX+n//2, startY) + recursion(n//2, startX+n//2, startY+n//2) + ")"

print(recursion(n, 0,0))