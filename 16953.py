from collections import deque
a, b = map(int, input().split())

possible = deque()
possible.append([a,1])

while possible:
    thisNode, cnt = possible.popleft()
    if thisNode == b:
        print(cnt)
        break
    if thisNode*2 < b+1:
        possible.append([thisNode*2, cnt+1])
    if thisNode*10+1 < b+1:
        possible.append([thisNode*10+1, cnt+1])
else:
    print(-1)
