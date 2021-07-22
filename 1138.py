n = int(input())
leftLarger = list(map(int, input().split()))
ans = [0 for _ in range(n)]
ansCandidate = list(range(n))

for ind, numOfLeft in enumerate(leftLarger):
    whereItStand = ansCandidate.pop(numOfLeft)
    ans[whereItStand] = ind + 1

print(*ans)