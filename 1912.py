import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().rstrip().split()))

maxi = numbers[0]
for i in range(1, n):
    numbers[i] = max(numbers[i], numbers[i-1]+numbers[i])
    if maxi < numbers[i]:
        maxi = numbers[i]

print(maxi)
