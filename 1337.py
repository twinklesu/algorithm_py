n = int(input())
li = []
for _ in range(n):
    li.append(int(input()))

li.sort()
minDiff = 0
for i in range(0, n):
    if i+5 <= n:
        numSet = set(li[i:i+5])
    else:
        numSet = set(li[i:])
    compare = set(range(li[i], li[i] + 5))
    diff = len(compare.difference(numSet))
    if diff < minDiff or i == 0:
        minDiff = diff
print(minDiff)