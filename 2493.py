from collections import deque


n = int(input())
polls = list(map(int, input().split()))
stack = deque()

for ind, el in enumerate(polls):
    # 스택이 비었으면 앞에 닿을 기둥이 없음 의미
    if not stack:
        print(0, end=' ')
    # 스택이 차 있으면, 가장 위의 기둥과 높이 비교
    else:
        while stack:
            top_ind, top_h = stack[-1]
            if top_h < el:
                stack.pop()
            elif top_h >= el:
                print(top_ind, end=' ')
                break
        else:
            print(0, end=' ')
    stack.append([ind + 1, el])  # 기둥번호, 기둥 길이
