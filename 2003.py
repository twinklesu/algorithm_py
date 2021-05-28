import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
numbers = list(map(int, input().rstrip().split()))

summed = [0 for _ in range(n)]
count = 0
for i in range(n):
    summed[i] = numbers[i]
    if summed[i] == m:
        count += 1
    for j in range(i):
        summed[j] += numbers[i]
        if summed[j] == m:
            count += 1
    print(summed)

print(count)

