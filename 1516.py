from collections import deque, defaultdict
import sys
input = sys.stdin.readline

n = int(input())
preToPost = defaultdict(list) # 선행 노드: 후행 노드
postToPre = defaultdict(list) # 후행 노드: 선행 노드
timeList = [0 for _ in range(n+1)] # 시간 얼마나 걸리는지
state = [0 for _ in range(n+1)] # 위상정렬 위해서, 이 노드 이전에 몇개의 노드 지나야 하는지 마킹
for u in range(1, n+1):
    inline = list(map(int, input().split()))[:-1]
    timeList[u] = inline[0]
    for v in inline[1:]:
        preToPost[v].append(u)
        postToPre[u].append(v)
        state[u] += 1


# 위상정렬
q = deque()
for i in range(1, n+1):
    if state[i] == 0:
        q.append(i)

sortedQ = deque()
while q:
    thisNode = q.popleft()
    sortedQ.append(thisNode)
    for nextNode in preToPost[thisNode]:
        state[nextNode] -= 1
        if state[nextNode] == 0:
            q.append(nextNode)

# 순서 정하면서 시간 계산
dp = [0 for _ in range(n+1)]
for node in sortedQ:
    dp[node] = timeList[node]
    # 이 노드 이전에 해야할 노드들의 max를 구해 더해줌
    preMax = 0
    for preNode in postToPre[node]:
        preMax = max(preMax, dp[preNode])
    dp[node] += preMax

print(*dp[1:], sep='\n')