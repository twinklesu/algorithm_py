from itertools import combinations
from math import sqrt


def solution():
    points = []
    for i in range(4):
        points.append(tuple(map(int, input().split())))
    comb = list(combinations(points, 2))
    dist_comb = []
    for c in comb:
        dist_comb.append([dist(c[0], c[1]), c])
    dist_comb.sort()
    dist_comb = dist_comb[:4]
    # 같은 길이의 모서리가 4개가 아닐 때
    distance = set([x[0] for x in dist_comb])
    if len(distance) != 1:
        print(0)
        return
    vectorLi = []
    for c in dist_comb:
        temp = c[1]
        vectorLi.append(vector(temp[0], temp[1]))
    vectorComb = list(combinations(vectorLi, 2))
    productLi = []
    for c in vectorComb:
        productLi.append(product(c[0], c[1]))
    count = 0
    for p in productLi:
        if p == 0:
            count += 1
    if count >= 4:
        print(1)
    else:
        print(0)


def dist(a, b):
    return sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def vector(a, b):
    return tuple([a[0] - b[0], a[1] - b[1]])


def product(a, b):
    return a[0] * b[0] + a[1] * b[1]


def main():
    n = int(input())

    for _ in range(n):
        solution()


main()