from collections import deque

def solution(n):
    num = deque()
    num.append(n)
    one = 0
    zero = 0
    while num:
        temp = num.popleft()
        if temp ==0:
            zero +=1
        elif temp == 1:
            one +=1
        else:
            num.append(temp-1)
            num.append(temp-2)
    print(zero, one)

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        solution(n)


main()