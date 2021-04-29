line = input()

num = 1
pointer = 0
l = len(line)
while pointer < l:
    strNum = str(num)
    lenNum = len(strNum)
    for s in strNum:
        if pointer == l:
            break
        elif s == line[pointer]:
            pointer += 1
    num += 1
print(num-1)
