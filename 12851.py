from collections import deque
n, k = map(int, input().split())

INF = 10**5+1
visited = [0 for _ in range(INF)] # 방문한 횟수
q = deque()
q.append([n,0])
visited[n] += 1
time = INF

while q:
    thisNode, thisTime = q.popleft()
    nextNodes = [thisNode-1, thisNode+1, thisNode*2]
    for nn in nextNodes:
        if nn == k:
            newTime = thisTime + 1
            if newTime <= time:
                visited[nn] += 1
                time = newTime
        elif 0 <= nn < INF and visited[nn] == 0:
            q.append([nn, thisTime+1])
            visited[nn] += 1

print(time)
print(visited[k])