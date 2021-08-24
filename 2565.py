import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    count = 1
    n = int(input())
    candidates = [0 for _ in range(n+1)]
    for _ in range(n):
        ind, el = map(int, input().split())
        candidates[ind] = el
    cutLine = candidates[1]
    for i in range(2, n+1):
        if candidates[i] < cutLine:
            count += 1
            cutLine = candidates[i]

    print(count)


