from collections import deque


line = input()
line = line.replace("()", "2").replace("[]", "3")
stack = deque()

for letter in line:
    if letter in "([":
        stack.append(letter)
    elif letter.isdigit():
        if stack and stack[-1].isdigit():
            temp = stack.pop()
            stack.append(str(int(temp)+int(letter)))
        else:
            stack.append(letter)
    elif letter == ")":
        if stack:
            if stack[-1].isdigit():
                temp = stack.pop()
                if stack and stack[-1] == "(":
                    stack.pop()
                    if stack and stack[-1].isdigit():
                        temp2 = stack.pop()
                        stack.append(str(int(temp)*2 + int(temp2)))
                    else:
                        stack.append(str(int(temp)*2))
                else: # [ 인 경우, 빈 스택인 경우
                    print(0)
                    break
            elif stack[-1] == "(":
                stack.pop()
                stack.append("2")
            else: # [ 인 경우
                print(0)
                break
        else: # 빈 stack에 닫음
            print(0)
            break
    elif letter == "]":
        if stack:
            if stack[-1].isdigit():
                temp = stack.pop()
                if stack and stack[-1] == "[":
                    stack.pop()
                    if stack and stack[-1].isdigit():
                        temp2 = stack.pop()
                        stack.append(str(int(temp)*3 + int(temp2)))
                    else:
                        stack.append(str(int(temp)*3))
                else: # ( 인 경우, 빈 스택인 경우
                    print(0)
                    break
            elif stack[-1] == "[":
                stack.pop()
                stack.append("3")
            else: # ( 인 경우
                print(0)
                break
        else: # 빈 stack에 닫음
            print(0)
            break
else:
    ans = stack.pop()
    if stack or not ans.isdigit():
        print(0)
    else:
        print(ans)
