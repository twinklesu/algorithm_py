from collections import deque


def solution():
    line = list(map(str, input()))
    leftQ = deque()
    rightQ = deque()

    for l in line:
        if l == '<' and leftQ:
            rightQ.appendleft(leftQ.pop())
        elif l == '>' and rightQ:
            leftQ.append(rightQ.popleft())
        elif l == '-' and leftQ:
            leftQ.pop()
        elif l not in '<>-':
            leftQ.append(l)

    print(*leftQ, *rightQ, sep='')


def main():
    t = int(input())
    for _ in range(t):
        solution()


main()