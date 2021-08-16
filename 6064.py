import sys
# from math import gcd
input = sys.stdin.readline


def gcd(a: int, b: int):
    while b != 0:
        a, b = b, a%b
    return a


t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())
    gc = gcd(m, n)
    lcm = m * n//gc
    xSet = set(range(x, lcm+1, m))
    ySet = set(range(y, lcm+1, n))
    ans = xSet.intersection(ySet)
    if ans:
        print(*ans)
    else:
        print(-1)
