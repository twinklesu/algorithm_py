a,b = map(int, input().split())

numList = []
start = 1
l = 0
while l < b:
    numList.extend([start]*start)
    l += start
    start += 1

print(sum(numList[a-1:b]))