import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
s = input()
p = 'I' + 'OI'*n
lenP = n*2+1
count = 0
pointer = 0

while pointer < m-n*2:
    if s[pointer:pointer+lenP] == p:
        count += 1
        pointer += lenP
        while pointer < m-1:
            if s[pointer:pointer+2] == 'OI':
                count += 1
                pointer += 2
            else:
                break
    else:
        pointer += 1


print(count)