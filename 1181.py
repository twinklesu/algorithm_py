def sortA(li):
    if len(li) <= 1:
        return li
    less = []
    equal = []
    greater = []
    pivot = len(li[len(li)//2])
    for l in li:
        if len(l)< pivot:
            less.append(l)
        elif len(l) > pivot:
            greater.append(l)
        else:
            equal.append(l)
    equal.sort()
    return sortA(less) + equal + sortA(greater)
            
n = int(input())
li = set()
for _ in range(n):
    li.add(input().rstrip())
for l in sortA(list(li)):
    print(l)