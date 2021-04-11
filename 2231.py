n = int(input())

error = True
for num in range(n):
    result = num
    s = str(num)
    result += sum(map(int, s))
    if result == n:
        print(num)
        error = False
        break
if error:
    print(0)