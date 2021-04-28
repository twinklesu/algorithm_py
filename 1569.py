n = int(input())

points = []
xSet = set()
ySet = set()
for _ in range(n):
    inputLine = tuple(map(int, input().split()))
    points.append(inputLine)
    xSet.add(inputLine[0])
    ySet.add(inputLine[1])

maxX = max(xSet)
minX = min(xSet)
maxY = max(ySet)
minY = min(ySet)
lenX = maxX - minX
lenY = maxY - minY
length = 0
vertex = []

if lenX > lenY:
    length = lenX
    xVertex = [maxX, minX]
    yVertex = [minY, minY+length]
else:
    length = lenY
    xVertex = [minX, minX+length]
    yVertex = [minY, maxY]

for p in points:
    if p[0] in xVertex or p[1] in yVertex:
        pass
    else:
        print(-1)
        break
else:
    print(length)
