def sort(li):
    if len(li) <= 1:
        return li
    pivot = li[len(li)//2]
    smaller = []
    equal = []
    greater = []
    for i in li:
        if i > pivot:
            greater.append(i)
        elif i< pivot:
            smaller.append(i)
        else:
            equal.append(i)
    return sort(smaller)+equal+sort(greater)
n = int(input())
li = []
for _ in range(n):
    li.append(int(input()))
for l in sort(li):
    print(l)