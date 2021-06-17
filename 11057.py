n = int(input())

numbers = [1 for _ in range(10)]

for _ in range(n-1):
    for i in range(10):
        numbers[i] = sum(numbers[i:])

print(sum(numbers)%10007)
