def hanoi(n, a, b, c):  # a 를 c로
    if n == 0:
        return
    hanoi(n - 1, a, c, b)  # a 를 b로
    print(a, c)
    hanoi(n - 1, b, a, c)  # b를 c로


n = int(input())
count = 2**n - 1
if n > 20:
    print(count)
else:
    print(count)
    hanoi(n, 1, 2, 3)