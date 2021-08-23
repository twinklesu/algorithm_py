from heapq import heappop, heappush
import sys
input = sys.stdin.readline


n, c = map(int, input().split())
houses = [0 for _ in range(n)]
for i in range(n):
    houses[i] = int(input())
maxi = max(houses)
numbers = [False for _ in range(maxi+1)]
