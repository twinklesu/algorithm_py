n = int(input())
numbers = list(map(int, input().split()))
numSet = list(set(numbers))
numSet.sort()
numDict = dict()
for ind, el in enumerate(numSet):
    numDict[el] = ind

for num in numbers:
    print(numDict[num], end=' ')