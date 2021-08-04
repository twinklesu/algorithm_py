from collections import deque
import sys
input = sys.stdin.readline


t = int(input())
for _ in range(t):
    a, b = list(map(int, input().split()))

    numbers = ['' for _ in range(10000)]

    q = deque()
    q.append(a)
    while q:
        a = q.popleft()
        order = numbers[a]
        if a == b:
            print(order)
            break
        # L
        v = a % 1000
        w = a // 1000
        newA = v*10+w
        if numbers[newA] == '':
            q.append(newA)
            numbers[newA] = order+'L'
        # R
        v = a % 10
        w = a // 10
        newA = v*1000+w
        if numbers[newA] == '':
            q.append(newA)
            numbers[newA] = order + 'R'
        # D
        newA = (a*2)%10000
        if numbers[newA] == '':
            q.append(newA)
            numbers[newA] = order + 'D'
        # S
        if a == 0 and numbers[9999] == '':
                q.append(9999)
                numbers[9999] = order + 'S'
        elif a != 0 and numbers[a-1] == '':
            q.append(a-1)
            numbers[a-1] = order + 'S'

