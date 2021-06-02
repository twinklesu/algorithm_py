import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
numbers = [0] + list(map(int, input().rstrip().split()))

acc = 0
for i in range(1, n+1):
    numbers[i] += acc
    acc = numbers[i]


for _ in range(m):
    start, end = map(int, input().split())
    print(numbers[end]-numbers[start-1])