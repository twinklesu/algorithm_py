class Deque():
    def __init__(self):
        self.deq = []
        self.length = 0
    def push_front(self,x):
        self.deq.insert(0,x)
        self.length +=1
    def push_back(self, x):
        self.deq.append(x)
        self.length +=1
    def pop_front(self):
        if self.deq:
            print(self.deq[0])
            self.deq.pop(0)
            self.length -=1
        else:
            print(-1)
    def pop_back(self):
        if self.deq:
            print(self.deq[-1])
            self.deq.pop(-1)
            self.length -=1
        else:
            print(-1)
    def size(self):
        print(self.length)
    def empty(self):
        if self.deq:
            print(0)
        else:
            print(1)
    def front(self):
        if self.deq:
            print(self.deq[0])
        else:
            print(-1)
    def back(self):
        if self.deq:
            print(self.deq[-1])
        else:
            print(-1)
            
n = int(input())
d = Deque()
for _ in range(n):
    l = input()
    if "push_front" in l:
        d.push_front(int(l[11:]))
    elif "push_back" in l:
        d.push_back(int(l[10:]))
    elif l == "pop_front":
        d.pop_front()
    elif l=="pop_back":
        d.pop_back()
    elif l=="size":
        d.size()
    elif l=="empty":
        d.empty()
    elif l =="front":
        d.front()
    elif l =="back":
        d.back()
