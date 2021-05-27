import sys
input = sys.stdin.readline

# 이분탐색
# 높이가 0 <= h <= 1,000,000,000 / 높이를 이분탐색


def sumOfTrees(h, trees):
    totalTree = 0
    for tree in trees:
        if tree-h > 0:
            totalTree += (tree-h)
    return totalTree


def recursion(front, tail, m, trees):
    mid = (front + tail)//2

    if mid == front:
        return mid # 수렴

    if sumOfTrees(mid, trees) >= m:
        return recursion(mid, tail, m, trees)
    else:
        return recursion(front, mid, m, trees)


def main():
    n, m = map(int, input().rstrip().split())
    trees = list(map(int, input().rstrip().split()))
    print(recursion(0, 10**9, m, trees))

main()