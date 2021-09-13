import sys
input = sys.stdin.readline


def distance(a, b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])


def solution(store, end, here):
    global ans
    if distance(here, end) <= 1000:
        ans = "happy"
        return
    for s in store:
        if store[s] == 0:
            if distance(here, s) <= 1000:
                store[s] = 1
                solution(store, end, s)
                store[s] = 0


t = int(input())
for _ in range(t):
    n = int(input())
    start = tuple(map(int, input().split()))
    store = dict()
    for _ in range(n):
        store[(tuple(map(int, input().split())))] = 0
    end = tuple(map(int, input().split()))

    ans = "sad"
    solution(store, end, start)

    print(ans)

