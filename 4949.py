line = input()
while line != ".":
    stack = []
    isRight = True
    for l in line:
        if l =="(" or l =="[":
            stack.append(l)
        elif l==")":
            if stack and stack[-1] == "(":
                stack.pop()
            else:
                isRight = False
                break
        elif l == "]":
            if stack and stack[-1] == "[":
                stack.pop()
            else:
                isRight = False
                break
    if stack:
        isRight = False
    if isRight:
        print("yes")
    else:
        print("no")
    line = input()
        
