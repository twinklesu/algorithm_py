# from collections import deque
# n, k = map(int, input().split())
# circle = deque(range(1,n+1))
# ans = []
# while circle:
#     for _ in range(k):
#         circle.append(circle.popleft())
#     ans.append(circle.pop())
# print('<' + str(ans)[1:-1] + '>')

from collections import deque

n, k = map(int, input().split())
q = deque(range(1, n + 1))

answer = []
while q:
    q.rotate(-k +1) # 앞에꺼를 뒤로 보내니까 음수 rotate
    answer.append(q.popleft())

print(str(answer).replace('[', '<').replace(']', '>'))
