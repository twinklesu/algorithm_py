import sys
input = sys.stdin.readline

line = list(map(str ,input().rstrip()))
stick = 0
total = 0

isCut = False
for ind, el in enumerate(line):
    if el == '(':
        if line[ind+1] == ')':
            # cut
            isCut = True
            total += stick
        else:
            stick += 1
    elif isCut:
        isCut = False
    else:
        stick -= 1
        total += 1

print(total)