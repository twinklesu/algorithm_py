from collections import deque


t = int(input())
for _ in range(t):
    order = input().replace("RR", "")
    n = int(input())
    arr = list(map(str, input()[1:-1].split(',')))
    if n == 0 and 'D' in order:
        print("error")
        continue
    q = deque(arr)
    head = True # 0이 head
    for o in order:
        if o == 'R':
            head = not head
        elif o == 'D':
            if not q:
                print("error")
                break
            elif head:
                q.popleft()
            else:
                q.pop()
    else:

        if head:
            print("[" + ','.join(q) + "]")
        else:
            q.reverse()
            print("[" + ','.join(q) + ']')