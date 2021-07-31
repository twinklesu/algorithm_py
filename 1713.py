from collections import deque, defaultdict


n = int(input())
t = int(input())
choice = list(map(int, input().split()))

studentsNum = max(choice)
photoZone = deque() # 번호, 시간
recommendation = defaultdict(int)

for c in choice:
    if c in photoZone:
        recommendation[c] += 1
    elif len(photoZone) < n:
        photoZone.append(c)
        recommendation[c] += 1
    else:
        minList = []
        minRec = min(recommendation.values())
        for k in recommendation:
            if recommendation[k] == minRec:
                minList.append(k)
        for p in photoZone:
            if p in minList:
                photoZone.remove(p)
                recommendation.pop(p)
                break
        recommendation[c] += 1
        photoZone.append(c)

ans = list(photoZone)
ans.sort()
print(*ans)