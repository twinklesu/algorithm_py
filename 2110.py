from heapq import heappop, heappush
import sys
input = sys.stdin.readline


n, c = map(int, input().split())
houses = [0 for _ in range(n)]
for i in range(n):
    houses[i] = int(input())

houses.sort()
distances = []
for i in range(n-1):
    distances.append(houses[i+1]-houses[i])

k = c-1
while k < len(distances):
    heapLi = []
    for i in range(len(distances)-1):
        heappush(heapLi, [distances[i]+distances[i+1], i]) #합, 인덱스
    minDist, ind = heappop(heapLi)
    distances[ind] = minDist
    del distances[ind+1]

print(min(distances))