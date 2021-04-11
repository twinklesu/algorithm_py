class Node():
    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next
        
class Deque():
    def __init__(self):
        self.first = Node()
        self.last = Node()
        self.first.next = self.last
        self.last.prev = self.first
        self.length = 0
    def push_front(self,x):
        temp = Node(x, self.first, self.first.next)
        self.first.next.prev = temp
        self.first.next = temp
        self.length +=1
    def push_back(self, x):
        temp = Node(x, self.last.prev, self.last)
        self.last.prev.next = temp
        self.last.prev = temp
        self.length +=1
    def pop_front(self):
        if self.first.next is self.last:
            print(-1)
        else:
            print(self.first.next.value)
            self.first.next = self.first.next.next
            self.first.next.prev = self.first
            self.length -=1
    def pop_back(self):
        if self.first.next is self.last:
            print(-1)
        else:
            print(self.last.prev.value)
            self.last.prev = self.last.prev.prev
            self.last.prev.next = self.last
            self.length -= 1
    def size(self):
        print(self.length)
    def empty(self):
        if self.length ==0:
            print(1)
        else:
            print(0)
    def front(self):
        if self.length ==0:
            print(-1)
        else:
            print(self.first.next.value)
    def back(self):
        if self.length ==0:
            print(-1)
        else:
            print(self.last.prev.value)
            
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