n = int(input())
m = int(input())

dic = dict()
for _ in range(m):
    p,q = map(int, input().split())
    if p in dic:
        dic[p].append(q)
    else:
        dic[p] = [q]
    if q in dic:
        dic[q].append(p)
    else:
        dic[q] = [p]

numSet = set()
numSet.add(1)
add = True

while add:
    popLi = []
    add = False
    for k in dic.keys():
        if k in numSet:
            add =True
            numSet.update(dic[k])
            popLi.append(k)
    for p in popLi:
        dic.pop(p)
print(len(numSet)-1)
