from collections import defaultdict
import sys
input = sys.stdin.readline

tc = int(input())
for _ in range(tc):
    n, m, w = map(int, input().split())
    road = defaultdict(list)
    for _ in range(m):
        # 도로
        s, e, t = map(int, input().split())
        road[s].append([e,t])
        road[e].append([s,t])
    for _ in range(w):
        # 웜홀
        s, e, t = map(int, input().split())
        road[s].append([e, -t])

    flag = False
    INF = 10**9
    dist = [INF for _ in range(n+1)]
    dist[1] = 0
    # 1에서 출발해 j로가는 최소 비용 구해 dist에 저장
    # n-1번까지만 반복 (이후로는 음수 사이클 존재)
    for turn in range(n):
        for node in range(1, n+1):
            for nextNode, nextCost in road[node]:
                if dist[nextNode] > dist[node] + nextCost:
                    dist[nextNode] = dist[node] + nextCost
                    if turn == n-1:
                        # n-1 에도 변화가 일어나서 여기까지 왔다? 사이클을 돌지 않고도 감소되는 부분이 존재??
                        flag = True

    if flag:
        print("YES")
    else:
        print("NO")

