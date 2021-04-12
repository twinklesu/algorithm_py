from math import sqrt

t = int(input())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    a = [x1,y1]
    b = [x2,y2]
    ab = sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)
    r = [ab, r1, r2]
    r.sort()
    if ab == 0 and r1 == r2:
        print(-1)
    elif r[-1] > sum(r[:-1]):
        print(0)
    elif ab == r1+r2 or ab == max(r1,r2)-min(r1,r2):
        print(1)
    else:
        print(2)