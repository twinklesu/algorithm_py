#t = int(input())
#
#for _ in range(t):
#    p = input().rstrip()
#    n = int(input())
#    li = input().rstrip()
#    li = list(map(int, li[1:-1].split(",")))
#    error = False
#    reverse = False
#    front = 0
#    rear = n
#    length = n
#    for o in p:
#        if o =='R':
#            reverse = not reverse
#        elif length !=0:
#            length -=1
#            if reverse:
#                rear -=1
#            else:
#                front +=1
#        else:
#            error = True
#            break
#    if error:
#        print("error")
#    elif reverse == True:
#        temp = li[front:rear]
#        temp.reverse()
#        print(temp)
#    else:
#        print(li[front:rear])

def ac(p, n, li):
    reverse = False
    front = 0
    back = len(li)-1
    for i in p:
        if i is "R":
            reverse = not reverse
        else:
            if front -1 == back:
                return "error"
            elif reverse:
                back -=1
            else:
                front +=1
    if reverse:
        result = "["
        for a in range(back, front, -1):
            result += str(li[a])
            result += ","
        result += str(li[front])
        result +="]"
        return result
    else:
        result = "["
        for a in range(front, back):
            result += str(li[a])
            result +=","
        result += str(li[back])
        result += "]"
        return result
    
    
t = int(input())
for _ in range(t):
    p = input().rstrip()
    n = int(input())
    text = input().rstrip()
    if text == "[]":
        li = []
    else:
        li = list(map(int, li[1,-1].split(",")))
    print(ac(p, n, li))
    
    



