#def search(n, nlist, m):
#    if n == 2:
#        if m in nlist:
#            return 1
#        else:
#            return 0
#    if nlist[n//2] > m:
#        return search(n//2, nlist[:n//2],m)
#    elif nlist[n//2]==m:
#        return 1
#    else:
#        return search(n-n//2, nlist[n//2+1:],m)

def solution(num, nlist, m):
    li = nlist
    n = num
    while n!=1:
        if li[n//2]>m:
            li = li[ :n//2]
            n //=2
        elif li[n//2]==m:
            print(1)
            return
        else:
            li = li[n//2+1: ]
            n = n - n//2
    if m in li:
        print(1)
    else:
        print(0)
        
    
n = int(input())
nlist = list(map(int, input().split()))
m = int(input())
mlist = list(map(int, input().split()))

nlist.sort()
for el in mlist:
    solution(n, nlist, el)
