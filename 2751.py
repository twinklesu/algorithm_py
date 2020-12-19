def merge(a, b):
    i = 0
    j = 0
    res = []
    while i<len(a) and j<len(b):
        if a[i] <= b[j]:
            res.append(a[i])
            i +=1
        else:
            res.append(b[j])
            j+=1

    res.extend(a[i:])
    res.extend(b[j:])
    return res
        
    
def mergeSort(li):
    if len(li) <= 1:
        return li
    return merge(mergeSort(li[:len(li)//2]), mergeSort(li[len(li)//2:]))

n = int(input())
li = []
for _ in range(n):
    li.append(int(input()))
li = mergeSort(li)
for i in li:
    print(i)
    