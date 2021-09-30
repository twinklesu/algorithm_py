import sys
input = sys.stdin.readline

def calc(firstNum, op, num):
    if operations[op] == "+":
        return firstNum + num
    elif operations[op] == "-":
        return firstNum - num
    else:
        return firstNum * num


def dfs(numPointer, res):
    global maxRes
    if numPointer >= n:
        maxRes = max(maxRes, res)
        return
    # 괄호 없이 연산
    dfs(numPointer+1, calc(res, numPointer-1, numbers[numPointer]))
    # 괄호 있이 연산
    if numPointer < n-1:
        thisRes = calc(numbers[numPointer], numPointer, numbers[numPointer+1])
        dfs(numPointer+2, calc(res, numPointer-1, thisRes))


n = int(input())
numbers = []
operations = []
inline = list(map(str, input()))
for i in inline:
    if i.isdigit():
        numbers.append(int(i))
    else:
        operations.append(i)

n, m = n//2+1, n//2
maxRes = -2**31

dfs(1, numbers[0])
print(maxRes)

