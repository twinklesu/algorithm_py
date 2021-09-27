from collections import deque

inline = input()
stack = deque()
ans = ""
priority = {"+": 1, "-":1, "*":0, "/":0, "(":2}

for letter in inline:
    # 피연산자는 바로 출력
    if letter.isalpha():
        ans += letter
    # 연산자는 우선순위 고려
    # (는 늘 최 우선
    elif letter == "(":
        stack.append(letter)
    elif letter == ")":
        # (가 나올때까지 pop
        while stack[-1] != "(":
            ans += stack.pop()
        stack.pop() # ( 제거
    else:
        # 연산자
        if stack:
            # 스택이 차 있는 경우, top 과 우선순위 비교
            if priority[stack[-1]] > priority[letter]:
                stack.append(letter)
            else:
                while stack and priority[stack[-1]] <= priority[letter]:
                    ans += stack.pop()
                stack.append(letter)
        else:
            # 스택 비어있으면, 그냥 push
            stack.append(letter)
while stack:
    ans += stack.pop()

print(ans)