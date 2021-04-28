n, m = map(int, input().split())

numToName = dict()
nameToNum = dict()

for i in range(1,n+1):
    name = input()
    numToName[i] = name
    nameToNum[name] = i

for _ in range(m):
    quest = input()
    if quest[0] in '123456789':
        print(numToName[int(quest)])
    else:
        print(nameToNum[quest])