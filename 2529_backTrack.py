def backTrack(ind, ans, n):
    global minAns, maxAns
    if ind == n:
        minAns = min(minAns, int(str(ans)[1:-1].replace(", ", "")))
        maxAns = max(maxAns, int(str(ans)[1:-1].replace(", ", "")))
        return
    bra = brackets[ind]
    for i in range(10):
        if i not in ans:
            if bra == ">" and ans[-1] > i:
                backTrack(ind+1, ans+[i], n)
            elif bra == "<" and ans[-1] < i:
                backTrack(ind+1, ans+[i], n)

n= int(input())
brackets = list(map(str, input().split()))

minAns = 10**(n+1)
maxAns = 0


for i in range(10):
    backTrack(0, [i], n)

print(maxAns)
if len(str(minAns)) == n+1:
    print(minAns)
else:
    print('0', minAns, sep='')