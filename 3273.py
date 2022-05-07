n = int(input())
numbers = list(map(int, input().split()))
x = int(input())

i = 0
j = n-1
numbers.sort()
count = 0
while (i < j):
    addintion = numbers[i] + numbers[j]
    if addintion == x:
        count += 1
        i += 1
        j -= 1
    elif addintion < x:
        i += 1
    else:
        j -= 1

print(count)
