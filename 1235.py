n = int(input())
numList = []

for _ in range(n):
    numList.append(input())

length = len(numList[0])
for k in range(1, length+1):
    numSet = set()
    for num in numList:
        numSet.add(num[length-k:])
    if len(numSet) == n:
        print(k)
        break