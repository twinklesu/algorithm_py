from collections import defaultdict, deque
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    times = [0] + list(map(int, input().split()))
    graph = defaultdict(list)
    preOrderGraph = defaultdict(list)
    state = [0 for _ in range(n+1)]
    for _ in range(k):
        u, v = map(int, input().split())
        graph[u].append(v) # 출발: [도착 노드 들]
        preOrderGraph[v].append(u) # 도착: [출발 노드들]
        state[v] += 1 # 위상 증가 시켜줌

    w = int(input()) # 지어야할 건물
    # 위상정렬
    q = deque()
    cnt = 0
    for i in range(1, n+1):
        if state[i] == 0:
            q.append(i)
    sortedQ = deque()
    while q:
        thisNode = q.popleft()
        sortedQ.append(thisNode)
        for nextNode in graph[thisNode]:
            state[nextNode] -= 1
            if state[nextNode] == 0:
                q.append(nextNode)

    dp = [0 for _ in range(n+1)]
    while sortedQ:
        thisNode = sortedQ.popleft()
        dp[thisNode] = times[thisNode]
        maxPreNodeTime = 0
        for preNode in preOrderGraph[thisNode]:
            maxPreNodeTime = max(dp[preNode], maxPreNodeTime)
        dp[thisNode] += maxPreNodeTime

    print(dp[w])




