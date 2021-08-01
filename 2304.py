n = int(input())
poll = []
maxHeight = 0
maxHeightX = 0
for _ in range(n):
    x, y = map(int, input().split())
    if y > maxHeight:
        maxHeightX = x
        maxHeight = y
    poll.append([x,y])

poll.sort()

beforeMax = []
afterMax = []

beforeH = 0
for p in poll:
    if p[1] > beforeH:
        beforeMax.append(p)
        beforeH = p[1]
    if p[0] == maxHeightX:
        break

beforeH = 0
for p in poll[::-1]:
    if p[0] == maxHeightX:
        afterMax.append([p[0]+1, p[1]])
        break
    if p[1] > beforeH:
        afterMax.append(p)
        beforeH = p[1]

afterMax[0][0] += 1 # 기둥의 끝이 필요해서

ans = 0
for i in range(len(beforeMax)-1):
    ans += (beforeMax[i+1][0]- beforeMax[i][0]) * beforeMax[i][1]
ans += maxHeight
for i in range(len(afterMax)-1):
    print((afterMax[i][0]- afterMax[i+1][0]) * afterMax[i][1])
    ans += (afterMax[i][0]- afterMax[i+1][0]) * afterMax[i][1]
    print(ans)

print(ans)