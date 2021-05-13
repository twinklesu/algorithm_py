n = int(input())
stair = []
for _ in range(n):
    stair.append(int(input()))

stair = stair[::-1]

if n < 3:
    print(sum(stair))
else:
    score = []
    score.append([stair[0] + stair[1], 0])
    score.append([0, stair[0] + stair[2]])
    pointer = 2

    while pointer < n-1:
        score.append([score[pointer-1][1]+stair[pointer+1], max(score[pointer-2])+stair[pointer+1]])
        pointer += 1

    ans = []
    ans.extend(score[-1])
    if len(score) > 1:
        ans.extend(score[-2])
    print(max(ans))
