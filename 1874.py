from collections import deque

n = int(input())
num = deque(range(1,n+1))
stack = deque()
result = ''
possible = True

for _ in range(n):
    target = int(input())
    while possible:
        if stack:
            top = stack[-1]
            if top > target:
                possible = False
            elif top < target:
                result += '+\n'  # push
                stack.append(num.popleft())
            else:
                result += '-\n'  # pop
                stack.pop()
                break
        else:
            stack.append(num.popleft())
            result += '+\n'
    if not possible:
        result = 'NO'
        break

print(result)