import math

number = input()
numberList = [0 for _ in range(9)]

for num in number:
    if num == '9':
        numberList[6] += 1
    else:
        numberList[int(num)] += 1
answer = 0
for ind, el in enumerate(numberList):
    if ind == 6:
        answer = max(answer, math.ceil(el/2))
    else:
        answer = max(answer, el)

print(answer)