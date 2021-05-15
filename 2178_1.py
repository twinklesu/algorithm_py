n, m = map(int, input().split())

mapp = dict()

for i in range(n):
    line = list(map(int, input()))
    for ind, el in enumerate(line):
        mapp[(i, ind)] = el

def recursive(point):
    if mapp[point] == 0:
        return 10000
    row = point[0]
    col = point[1]
    next_move = []
    if row>0: # 상
        next_move.append((row-1, col))
    if row < n-1: # 하
        next_move.append((row+1, col))
    if col > 0: # 좌
        next_move.append((row, col-1))
    if col < m-1: #우
        next_move.append((row, col+1))
    result = []
    for move in next_move:
        result.append(recursive(move))
    return min(result)


print(recursive((0,0)))