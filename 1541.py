line = list(map(str, input().split('-')))

ansList = []
for l in line:
    numbers = map(int, l.split('+'))
    summed = sum(numbers)
    ansList.append(summed)

ans = ansList[0]
for a in ansList[1:]:
    ans -= a

print(ans)
