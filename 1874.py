# from collections import deque
#
# n = int(input())
# num = deque(range(1,n+1))
# stack = deque()
# result = ''
# possible = True
#
# for _ in range(n):
#     target = int(input())
#     while possible:
#         if stack:
#             top = stack[-1]
#             if top > target:
#                 possible = False
#             elif top < target:
#                 result += '+\n'  # push
#                 stack.append(num.popleft())
#             else:
#                 result += '-\n'  # pop
#                 stack.pop()
#                 break
#         else:
#             stack.append(num.popleft())
#             result += '+\n'
#     if not possible:
#         result = 'NO'
#         break
#
# print(result)


from collections import deque

n = int(input())
numList = []
for _ in range(n):
    numList.append(int(input()))

numbers = deque(range(1, n + 1))
answer = ['+']
stack = deque()
stack.append(numbers.popleft())

for num in numList:
    flag = True
    while not stack and numbers or (stack and numbers and stack[-1] < num):
        stack.append(numbers.popleft())
        answer.append('+')
        flag = False
    while stack and stack[-1] >= num:
        stack.pop()
        answer.append('-')
        flag = False
    if flag:
        break

if numbers or stack:
    print("NO")
else:
    print('\n'.join(answer))
