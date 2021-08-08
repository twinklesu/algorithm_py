n = int(input())
polls = []
maxHeight = 0
maxHeightLastX = 0
for _ in range(n):
    x, y = map(int, input().split())
    if y >= maxHeight:
        maxHeight = y
        maxHeightLastX = x
    polls.append([x, y])

polls.sort()

pollsUntilMax = []
pollsAfterMax = []
beforeHeight = 0
for p in polls:
    if maxHeightLastX < p[0]:
        break
    if p[1] >= beforeHeight:
        pollsUntilMax.append(p)
        beforeHeight = p[1]
beforeHeight = 0
for p in polls[::-1]:
    if p[0] <= maxHeightLastX:
        break
    if p[1] >= beforeHeight:
        pollsAfterMax.append([p[0]+1, p[1]])
        beforeHeight = p[1]

pollsAfterMax.append([maxHeightLastX+1, maxHeight])
ans = 0
for i in range(len(pollsUntilMax)-1):
    ans += (pollsUntilMax[i+1][0] - pollsUntilMax[i][0]) * pollsUntilMax[i][1]
ans += maxHeight # 너비 1 짜리
for i in range(len(pollsAfterMax)-1):
    ans += (pollsAfterMax[i][0] - pollsAfterMax[i+1][0]) * pollsAfterMax[i][1]

print(ans)
