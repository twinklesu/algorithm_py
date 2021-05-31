from math import sqrt

def distance(a,b):
    return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)


def solution():
    points = list(map(int, input().split()))
    start = (points[:2])
    end = (points[2:])
    n = int(input())
    circles = []
    for _ in range(n):
        circles.append(list(map(int, input().split())))

    count = 0
    for c in circles:
        start_dist = distance(c[:2], start)
        end_dist = distance(c[:2], end)
        if start_dist <= c[2] and end_dist <= c[2]:
            pass
        elif start_dist <= c[2] or end_dist <= c[2]:
            count += 1
    print(count)


def main():
    t = int(input())
    for _ in range(t):
        solution()


main()