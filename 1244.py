def boy(k, li, n):
    d = {0:1,1:0}
    for i in range(k, n+1, k):
        li[i] = d[li[i]]

def girl(k, li, n):
    count = 0
    d = {0:1,1:0}
    while k-count >0 and k+count < n:
        if li[k-count-1] == li[k+count+1]:
            count += 1
        else:
            break
    li[k-count:k+count+1] = list(d[el] for el in li[k-count:k+count+1])

n = int(input())
li = list(map(int, input().split()))
li = [None] + li
m = int(input())
for _ in range(m):
    gender, num = map(int, input().split())
    if gender == 1:
        boy(num, li, n)
    else:
        girl(num, li, n)
print(str(li[1:])[1:-1].replace(',',''))