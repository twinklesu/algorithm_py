from collections import deque
n, k = map(int, input().split())

INF = 10**5+1
visited = [[0,0] for _ in range(INF)] # 시간, 방문 횟수
q = deque()
visited[n][1] += 1
newQ = deque()
newQ.append(n)

count = 0
flag = True
while newQ and flag:
    q = newQ.copy()
    newQ.clear()
    count += 1
    while q:
        thisNode = q.popleft()
        if thisNode == k:
            flag = False
            break
        nextNodes = [thisNode-1, thisNode+1, thisNode*2]
        for nn in nextNodes:
            if 0 <= nn < INF and (visited[nn][1] == 0 or visited[nn][0] == count):
                if visited[nn][1] == 0:
                    # 이번턴에도 첫 방문 일 시
                    newQ.append(nn)
                visited[nn][1] += visited[thisNode][1]
                visited[nn][0] = count



print(*visited[k], sep='\n')