import sys
input = sys.stdin.readline.rstrip()


class Stack():
    def __init__(self):
        self.stack = []
        self.check = True
    def push(self,n):
        self.stack.append(n)
    def pop(self):
        if len(stack) == 0:
            check = False
            return
        self.stack.pop(-1)
        
n = int(input())
for _ in range(n):
    line = input()
    st = Stack()
    check = True
    for l in line:
        if l == "(":
            st.push(0)
        else:
            st.pop()
    if len(st.stack) != 0 or not st.check:
        print("NO")
    else:
        print("YES")
        
        