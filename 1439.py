s = input()
while '11' in s or '00' in s:
    s = s.replace('11', '1').replace('00','0')

num0, num1 = 0,0
for n in s:
    if n == '0':
        num0 += 1
    else:
        num1 += 1

print(min(num0, num1))
