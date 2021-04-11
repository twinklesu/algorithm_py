n = int(input())
li = list(range(n+1, 0, -1))
stack = []
result = []
stack.append(li.pop())
result.append("+")
br = True
for _ in range(n):
    order = int(input())
    while stack and stack[-1] != order:
        if stack[-1] < order:
            if li[-1] > order:
                br = False
                break
            stack.append(li.pop())
            result.append("+")
        elif stack[-1] > order:
            stack.pop()
            result.append("-")
    if stack and stack[-1] == order: #pop the right num
        stack.pop()
        result.append("-")
    elif not stack or not br:
        br = False
        break
if not br:
    print("NO")
else:
    for x in result:
        print(x)