from math import sqrt

n = int(input())
num = int(sqrt(n))
numbers = [None for _ in range(n+1)]

smaller_square = []
for i in range(1, n+1):
    if sqrt(i) == int(sqrt(i)):
        numbers[i] = 1
        smaller_square.append(i)
    else:
        candidate = []
        for square in smaller_square:
            candidate.append(1 + numbers[i-square])
        numbers[i]=min(candidate)

print(numbers[-1])

