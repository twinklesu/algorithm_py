from heapq import heappop, heappush
import sys
input = sys.stdin.readline

n = int(input())
q = []
for _ in range(n):
    x = int(input())
    if x == 0 and q:
        print(heappop(q))
    elif x == 0 and not q:
        print(0)
    else:
        heappush(q, x)
