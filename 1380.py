n = int(input())
count = 1
while n != 0:
    nameList = [None]
    for _ in range(n):
        nameList.append(input())
    numList = []
    for _ in range(2*n-1):
        number = int(input().split()[0])
        if number in numList:
            ind = numList.index(number)
            numList.pop(ind)
        else:
            numList.append(number)
    print(count, nameList[numList[0]])
    n = int(input())
    count +=1