n = int(input())
stack = []
length = 0
for m in range(n):
    x = input()
    if 'push' in x:
        stack.insert(0, int(x[5:]))
        length +=1
    elif 'pop' in x:
        if length == 0:
            print('-1')
        else:
            print(stack[0])
            length -= 1
            for i in range(length):
                stack[i] = stack[i+1]
    elif 'size' in x:
        print(length)
    elif 'empty' in x:
        if length == 0:
            print(1)
        else:
            print(0)
    elif 'top' in x:
        if length ==0:
            print(-1)
        else:
            print(stack[0])