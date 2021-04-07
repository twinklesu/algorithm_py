ax, ay, bx, by, cx, cy = map(int, input().split())
points = [[ax,ay], [bx,by], [cx,cy]]

def dist(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**(1/2)

# 평행사변형 안될때

if points[0]==points[1] or points[1]==points[2] or points[0]==points[2]:
    print(-1)
elif ax-bx != 0 and cx-bx!=0 and (ay-by)/(ax-bx) == (cy-by)/(cx-bx):
    print(-1)
elif ax==bx and bx==cx:
    print(-1)
else:
    lenList = [dist(ax, ay, bx, by), dist(ax,ay,cx,cy), dist(bx,by,cx,cy)]
    lenList.sort()
    min_ = 2*(lenList[0] + lenList[1])
    max_ = 2*(lenList[1] + lenList[2])

    print(max_ - min_)