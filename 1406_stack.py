import sys
input = sys.stdin.readline
from collections import deque

left = deque(map(str, input().rstrip()))
right = deque()
n = int(input())

for _ in range(n):
    move = input().rstrip()
    if move == 'L' and left:
        right.appendleft(left.pop())
    elif move == 'D' and right:
        left.append(right.popleft())
    elif move == 'B' and left:
        left.pop()
    elif move[0] == 'P':
        left.append(move[-1])


for l in left:
    print(l, end='')
for r in right:
    print(r, end='')