class Queue():
    def __init__(self):
        self.q = []
        self.length = 0
        self.front = 0
    def push(self, n):
        self.q.append(n)
        self.length +=1
        return
    def pop(self):
        if self.length !=0:
            print(self.q[self.front])
            self.front +=1
            self.length -=1
        else:
            print(-1)
        return
    def size(self):
        print(self.length)
        return
    def empty(self):
        if self.length !=0:
            print(0)
        else:
            print(1)
        return
    def front(self):
        if self.length !=0:
            print(self.q[self.front])
        else:
            print(-1)
        return
    def back(self):
        if self.length !=0:
            print(self.q[-1])
        else:
            print(-1)
        return
    
n = int(input())
q = Queue()
for _ in range(n):
    l = input()
    if "push" in l:
        q.push(l[5:])
    elif l == "pop":
        q.pop()
    elif l =="size":
        q.size()
    elif l =="empty":
        q.empty()
    elif l =="front":
        q.front()
    elif l =="back":
        q.back()
      