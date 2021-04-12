from collections import deque

n, m = map(int, input().split())
target = list(map(int, input().split()))

count = 0
deq = deque(range(1, n+1))

for t in target:
    # from front
    count_left = 0
    deq_left = deq.copy()
    left = deq_left.popleft()
    while left != t:
        count_left += 1
        deq_left.append(left)
        left = deq_left.popleft()
    # from tail
    count_right = 0
    deq_right = deq.copy()
    right = deq_right.pop()
    while right != t:
        count_right += 1
        deq_right.appendleft(right)
        right = deq_right.pop()
    count_right += 1

    if count_left <= count_right:
        count += count_left
        deq = deq_left
    else:
        count += count_right
        deq = deq_right

print(count)

