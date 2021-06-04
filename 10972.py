from itertools import permutations
n = int(input())
numbers = list(map(int, input().split()))

cursor = None
# 커지기 시작하는 마지막 위치 기록
for ind, el in enumerate(numbers[:-1]):
    if el < numbers[ind+1]:
        cursor = ind
# 한번도 안커지는,,
if cursor is None:
    print(-1)
else:
    newNumbers = numbers[cursor:]
    if newNumbers[-1] == min(newNumbers):
        newNumbers.sort()
        newNumbers = [newNumbers[-1]] + newNumbers[:-1]
    else:
        perm = list(permutations(newNumbers))
        perm.sort()
        for p in perm:
            if list(p) > newNumbers:
                newNumbers = list(p)
                break
    for num in numbers[:cursor]+newNumbers:
        print(num, end=' ')
