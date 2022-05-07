a = int(input())
b = int(input())
c = int(input())

multi = str(a*b*c)
numbers = [0 for _ in range(10)]
for s in multi:
    numbers[int(s)] += 1

for el in numbers:
    print(el)