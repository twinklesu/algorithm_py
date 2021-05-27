import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
lans = []
for _ in range(n):
    lans.append(int(input().rstrip()))


def getSumOfLens(lans, h):
    cut = [x//h for x in lans if x//h > 0]
    return sum(cut)


def binarySearch(front, tail, lans):
    mid = (front+tail)//2

    if front == mid:
        return mid
    elif getSumOfLens(lans, mid) >= m:
        return binarySearch(mid, tail, lans)
    else:
        return binarySearch(front, mid, lans)


print(binarySearch(1, 2**31, lans))