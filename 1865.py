from collections import defaultdict

tc = int(input())
for _ in range(tc):
    n, m, w = map(int, input().split())
    road = defaultdict(list)
    nodes = set()
    for _ in range(m):
        # 도로
        s, e, t = map(int, input().split())
        road[s].append([e,t])
        road[e].append([s,t])
        nodes.add(s)
        nodes.add(e)
    for _ in range(w):
        # 웜홀
        s, e, t = map(int, input().split())
        road[s].append([e, -t])
        nodes.add(s)
        nodes.add(e)

    INF = 10**9
    flag = False
    v = len(nodes)
    for start in range(1, n+1):
        dist = [INF for _ in range(n+1)]
        dist[start] = 0

        # node에서 출발해 j로가는 최소 비용 구해 dist에 저장
        # n-1번까지만 반복 (이후로는 음수 사이클 존재)
        for _ in range(v-1):
            for node in nodes:
                for nextNode, nextCost in road[node]:
                    if dist[nextNode] > dist[node] + nextCost:
                        dist[nextNode] = dist[node] + nextCost
        if dist[start] < 0:
            flag = True
            break

    if flag:
        print("YES")
    else:
        print("NO")

