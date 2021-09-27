n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

accMax = 1
for num in numbers:
    if num <= accMax:
        accMax += num
    else:
        break
print(accMax)