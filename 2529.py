n = int(input())
brakets = list(map(str, input().split()))

# max
num = 9
ansMax = [0 for _ in range(n+1)]
lastFilled = 0
for i in range(n):
    if brakets[i] == '>':
        ind = i
        while ind >= lastFilled:
            ansMax[ind] = num
            num -= 1
            ind -= 1
        lastFilled = i +1

if lastFilled <= n:
    unFilledNum = n - lastFilled +1
    ansMax[lastFilled:] = list(range(num+1-unFilledNum, num+1))
print(*ansMax)

num = 0
ansMin = [0 for _ in range(n+1)]
lastFilled = 0
for i in range(n):
    if brakets[i] == '<':
        ind = i
        while ind >= lastFilled:
            ansMin[ind] = num
            num += 1
            ind -= 1
        lastFilled = i + 1

if lastFilled <= n:
    unFilledNum = n - lastFilled + 1
    ansMin[lastFilled:] = list(range(num-1+unFilledNum, num-1, -1))
print(*ansMin)