n = int(input())
tipList = []
for _ in range(n):
    tipList.append(int(input()))

tipList.sort(reverse=True)
sumMax = 0
for ind, el in enumerate(tipList):
    tip = el-ind
    if tip <= 0:
        break
    else:
        sumMax += tip

print(sumMax)