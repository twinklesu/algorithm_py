n = int(input())

numList = []
numList = list(map(int, input().split()))

min_ = min(numList)
max_ = max(numList)

print(min_*max_)