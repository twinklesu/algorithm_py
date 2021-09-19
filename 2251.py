from collections import deque
criteria = list(map(int, input().split()))

state = [0, 0, criteria[2]]
ans = set()
history = set()

q = deque()
q.append(state)
while q:
    thisState = q.pop()
    if thisState[0] == 0:
        ans.add(thisState[2])
    for fromCup in range(3):
        for toCup in range(3):
            if fromCup == toCup:
                continue
            newState = thisState.copy()
            if thisState[fromCup] and thisState[toCup] < criteria[toCup]:
                newState[toCup] = min(criteria[toCup], thisState[fromCup]+thisState[toCup])
                newState[fromCup] = thisState[fromCup] - newState[toCup] + thisState[toCup]
                if tuple(newState) not in history:
                    history.add(tuple(newState))
                    q.append(newState)
ans = list(ans)
ans.sort()
print(*ans)