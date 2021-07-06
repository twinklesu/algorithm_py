from collections import deque

line = list(map(str, input()))
stack = deque()
stack.append(line[0])
sett = {'(':')', '[':']'}
values = {'(': 2, '[': 3}

flag = True
for l in line[1:]:
    if l in '([':
        stack.append(l)
    elif l in ')]': # ) ]
        top = stack.pop()
        if type(top) is int:
            secondTop = stack.pop()
            if l == sett[secondTop]:
                value = values[secondTop]
                stack.append(top*value)
            else:
                flag = False
                break
        else:
            if l in sett and l == sett[top]:
                value = values[top]
                stack.append(value)
            else:
                flag = False
                break
    else:
        flag = False
        break
    # 덧셈 확인
    while len(stack)> 1:
        top = stack.pop()
        secondTop = stack.pop()
        if type(top) is int and type(secondTop) is int:
            stack.append(top+secondTop)
        else:
            stack.append(secondTop)
            stack.append(top)
            break


if flag and len(stack) == 1:
    print(stack[0])
else:
    print(0)