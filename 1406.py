import sys
input = sys.stdin.readline
from collections import deque


line = deque(map(str, input().rstrip()))
n = int(input())
line.appendleft(None)

for _ in range(n):
    move = input().rstrip()
    if move == 'L':
        if line[-1] is not None:
            line.rotate(1)
    elif move == 'D':
        if line[0] is not None:
            line.rotate(-1)
    elif move == 'B':
        if line[-1] is not None:
            line.pop()
    else:
        line.append(move[-1])


ind = line.index(None)
line.rotate(len(line)-ind)
line.popleft()
print(''.join(line))