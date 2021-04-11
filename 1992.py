def quad(n, li):
    if n == 1:
        return  li[0]
    else:
        same = True
        first = li[0]
        for l in li:
            if l != first:
                same = False
                break
        if same:
            return first
        
    a=[]
    b=[]
    c=[]
    d=[]
    length = len(li)
    for i in range(length):
        if i < length//2:
            if i%n < n//2:
                a.append(li[i])
            else:
                b.append(li[i])
        else:
            if i%n < n//2:
                c.append(li[i])
            else:
                d.append(li[i])
    return "("+ quad(n/2,a) + quad(n/2,b) + quad(n/2,c)+ quad(n/2,d) +")"
   
    
n = int(input())
pic = []
for _ in range(n):
    line = input().rstrip()
    for l in line:
        pic.append(l)
    
res = quad(n,pic)
print(res)
        