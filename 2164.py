n = int(input())
q = list(range(1, n+1))
front = 0
length = n
while length != 0:
    if length ==1:
        break
    front +=1
    length -=1
    if length ==1:
        break
    num = q[front]
    front +=1
    q.append(num)
print(q[front])
        
