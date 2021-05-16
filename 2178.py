from collections import deque

mapp = dict()
shortest_path = dict()
waiting_q = deque()


def solution(point):
    # 들어온 point의 상하좌우의 shortest_path 확인하고, +1 해준다
    x, y = map(int, point)
    points = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)] # mapp 에 있는 좌표만 접근하기 때문에 경계고려 안함
    path = []
    for p in points:
        if p in mapp and mapp[p] == 1:
            if p in shortest_path:
                path.append(shortest_path[p])
            else:
                if p not in waiting_q:
                    waiting_q.append(p)
    shortest_path[point] = 1 + min(path)


def main():
    n, m = map(int, input().split())

    for i in range(n):
        temp = list(map(int, input()))
        for ind, el in enumerate(temp):
            mapp[(i, ind)] = el

    shortest_path[(0,0)] = 1
    if mapp[(0,1)] == 1:
        waiting_q.append((0,1))
    if mapp[(1,0)] == 1:
        waiting_q.append((1,0))


    while waiting_q:
        temp = waiting_q.popleft()
        solution(temp)
    print(shortest_path[(n-1, m-1)])

main()
