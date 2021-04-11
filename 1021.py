class Queue():
    def __init__(self, n):
        self.q = list(range(1, n+1))
        self.length = n
    def pop_first(self):
        self.q.pop(0)
        self.length -=1
    def toLeft(self):
        self.q.append(self.q.pop(0))
    def toRight(self):
        self.q.insert(0, self.q.pop())

n, m = map(int, input().split())
want = list(map(int, input().split()))
check = Queue(0)
check.q = [None]*n
check.length = n
for k in want:
    check.q[k-1] = k
number = Queue(n)
count = 0
while want:
    if check.q[0] == want[0]:
        want.pop(0)
        check.pop_first()
        number.pop_first()
    elif check.q.index(want[0]) < check.length/2:
        check.toLeft()
        number.toLeft()
        count +=1
    else:
        check.toRight()
        number.toRight()
        count +=1
print(count)