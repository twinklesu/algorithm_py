from collections import deque
n, k = map(int, input().split())
circle = deque(range(1,n+1))
ans = []
while circle:
    for _ in range(k):
        circle.append(circle.popleft())
    ans.append(circle.pop())
print('<' + str(ans)[1:-1] + '>')