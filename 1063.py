king, stone, n = map(str, input().split())
n = int(n)

row = 'ABCDEFGH'
king_xy = [row.find(king[0]), int(king[1])]
stone_xy = [row.find(stone[0]), int(stone[1])]

def moving(xy, move):
    for m in move:
        if m == 'R':
            xy[0] += 1
        elif m =='L':
            xy[0] -= 1
        elif m =='B':
            xy[1] -= 1
        elif m == 'T':
            xy[1] += 1
    return xy

for _ in range(n):
    move = input()
    king_new = moving([king_xy[0], king_xy[1]], move)
    if 0 <= king_new[0] < 8 and 0 < king_new[1] <= 8:
        if king_new == stone_xy:
            stone_new = moving([stone_xy[0], stone_xy[1]], move)
            if 0 <= stone_new[0] < 8 and 0 < stone_new[1] <= 8:
                stone_xy = stone_new
                king_xy = king_new
        else:
            king_xy = king_new

print(row[king_xy[0]] + str(king_xy[1]))
print(row[stone_xy[0]] + str(stone_xy[1]))