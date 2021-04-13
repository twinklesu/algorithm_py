n = int(input())

count = 0
for i in range(1, n+1):
    num = list(map(int, str(i)))
    for ind, el in enumerate(num[:-2]):
        diff = el - num[ind+1]
        if num[ind+1] - num[ind+2] != diff:
            break
    else:
        count += 1

print(count)
