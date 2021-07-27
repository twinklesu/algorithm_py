import sys
input = sys.stdin.readline
n, l = map(int, input().split())


x = n/l - (l-1)/2
while int(x) != x and int(x) >= 0 and l < 101:
    l += 1
    x = n/l - (l-1)/2


x = int(x)
if x >= 0 and l < 101:
    print(*range(x, x+l))
else:
    print(-1)