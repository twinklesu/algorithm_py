from collections import deque

s = int(input())
INF = 1000*2+1
q = deque()
visited = dict()
visited[(1,0)] = 0
q.append((1,0)) # 개수, 클립보드

while q:
    thisCount, thisClip = q.popleft()
    if thisCount == s:
        print(visited[(s, thisClip)])
        break
    if thisClip != 0 and (thisCount+thisClip, thisClip) not in visited:
        visited[(thisCount+thisClip, thisClip)] = visited[(thisCount, thisClip)] +1
        q.append((thisCount+thisClip, thisClip))
    if 0<thisCount-1 and (thisCount-1, thisClip) not in visited:
        visited[(thisCount-1, thisClip)] = visited[(thisCount, thisClip)] +1
        q.append((thisCount-1, thisClip))
    if (thisCount, thisCount) not in visited:
        q.append((thisCount, thisCount))
        visited[(thisCount, thisCount)] = visited[(thisCount, thisClip)] + 1

