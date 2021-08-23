from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    x = int(input())
    if x == 0:
        if heap:
            pri, num = heappop(heap)
            print(num)
        else:
            print(0)
    else:
        heappush(heap, [abs(x), x])