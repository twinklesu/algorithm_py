class Node():
    def __init__(self, target, imp):
        self.target = target
        self.imp = imp
    
    
n = int(input())
for _ in range(n):
    k,t = map(int, input().split())
    impli = list(map(int,input().split()))  #list
    q = []
    for i in range(k):
        q.append(Node(False, impli[i]))
    q[t].target = True
    

    count = 0
    while True:
        p = q[0]
        if p.imp == max(impli):
            if p.target:
                break
            impli.remove(p.imp)
            q.pop(0)
            count +=1
        else:
            q.append(q.pop(0))
    count +=1
    print(count)
    