def solution(video: list, n: int, startX, startY):
    checkUniqueSet = set()
    for i in range(startX, startX+n):
        for j in range(startY, startY+n):
            checkUniqueSet.add(video[i][j])
    if len(checkUniqueSet) == 1:
        return str(checkUniqueSet.pop())
    n//=2
    return "(" + solution(video, n, startX, startY) + solution(video, n, startX, startY+n) + solution(video, n, startX+n, startY) + solution(video, n, startX+n, startY+n) + ")"


n = int(input())
video = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    line = list(map(int, input()))
    for j, el in enumerate(line):
        video[i][j] = el

print(solution(video, n, 0, 0))
