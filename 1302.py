n = int(input())

sold = dict()
for _ in range(n):
    book = input()
    if book in sold:
        sold[book] += 1
    else:
        sold[book] = 1

maxList = []
maxSoldNum = 0
for key, value in zip(sold.keys(), sold.values()):
    if value > maxSoldNum:
        maxSoldNum = value
        maxList = [key]
    elif value == maxSoldNum:
        maxList.append(key)

maxList.sort()
print(maxList[0])