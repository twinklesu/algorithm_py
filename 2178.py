from collections import deque

mapp = []
direction_dict = dict()
stack = deque()
n, m = map(int, input().split())

for _ in range(n):
    mapp.append(list(map(int, input())))


def check(top):
    # 1은 위, 2는 오른쪽, 3은 아래, 4는 왼쪽
    direction = direction_dict[top]
    row = top[0]
    col = top[1]
    direction_dict[top] = direction + 1  # 실패든 성공이든 방향은 바꿔주기.
    if direction == 4: #위
        if row != 0 and mapp[row - 1][col] != 0:
            new = (row - 1, col)
            if new not in stack:
                direction_dict[new] = 1
                return new
        return check(top)
    elif direction == 2: #오른
        print(col + 1, m - 1)
        if col + 1 != m and mapp[row][col + 1] != 0:
            new = (row, col + 1)
            if new not in stack:
                direction_dict[new] = 1
                return new
        return check(top)
    elif direction == 1: #아래
        if row + 1 != n and mapp[row + 1][col] != 0:
            new = (row + 1, col)
            if new not in stack:
                direction_dict[new] = 1
                return new
        return check(top)
    elif direction == 3: #왼
        if col != 0 and mapp[row][col - 1] != 0:
            new = (row, col - 1)
            if new not in stack:
                direction_dict[new] = 1
                return new
        return check(top)
    else:  # 가려는 방향이 이미 지나온 길인 경우
        return


stack.append((0, 0))
direction_dict[(0, 0)] = 1  # 위

top = stack.popleft()
while (n - 1, m - 1) != top:
    result = check(top)
    if result is None:
        direction_dict.pop(top)
        top = stack.pop()
    else:
        stack.append(top)
        top = result
    print(stack)
count = len(stack) + 1
print(count)
