from collections import deque

n = int(input())
m = 0
numList = []
for _ in range(n):
    num = int(input())
    m += num
    numList.append(num)

dasom = numList[0]
numList = deque(numList[1:])
count = 0

while any(dasom <= x for x in numList):
    temp = numList.popleft()
    if all(temp >= x for x in numList):
        numList.append(temp-1)
        count += 1
        dasom += 1
    else:
        numList.append(temp)

print(count)