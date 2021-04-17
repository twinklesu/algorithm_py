from collections import deque
n = int(input())
move = list(map(str, input()))

directions = deque(['S', 'E', 'N', 'W'])
x = 0
y = 0
beenTo = set()
beenTo.add((x, y))
xSet = set()
ySet = set()
xSet.add(x)
ySet.add(y)
for m in move:
    if m == 'R':
        directions.rotate(-1)
    elif m =='L':
        directions.rotate(1)
    else:
        moveTo = directions[0]
        if moveTo == 'S':
            y -= 1
        elif moveTo == 'N':
            y += 1
        elif moveTo == 'E':
            x -= 1
        else:
            x += 1
        beenTo.add((x, y))
        xSet.add(x)
        ySet.add(y)


xLen = len(xSet)
yLen = len(ySet)
xMin = -min(xSet)
yMin = -min(ySet)

map_ = []
for _ in range(yLen):
    temp = []
    for _ in range(xLen):
        temp.append('#')
    map_.append(temp)


for point in beenTo:
    xPoint = point[1]+yMin
    yPoint = point[0] + xMin
    map_[xPoint][yPoint] = '.'

for i in range(len(map_)-1, -1, -1):
    for m in map_[i]:
        print(m, end='')
    print()
