import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
numbers = list(map(int, input().rstrip().split()))

count = 0
for ind, el in enumerate(numbers):
    if ind == 0 and el == m:
        count += 1
    else:
        if el == m:
            count += 1
        for i in range(ind):
            numbers[i] += el
            if numbers[i] == m:
                count += 1

print(count)
