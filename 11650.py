n = int(input())
li = []
for _ in range(n):
    li.append(list(map(int,input().rstrip().split())))
li.sort(key=lambda x:x[0])
for i in range(len(li)):
    equal = []
    equal.append(li[i])
    index = None
    for t in range(i+1, len(li)):
        if li[i][0] == li[t][0]:
            equal.append(li[t])
            index = t #last index of same x
        else:
            break
    if index:
        equal.sort(key = lambda x:x[1])
        for m in range(index, i-1, -1):
            li[m]=equal.pop()        
for l in li:
    print(l[0],l[1], sep =' ')