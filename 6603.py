from itertools import combinations

while True:
    line = list(map(int, input().split()))
    if line == [0]:
        break
    numbers = line[1:]
    numbers.sort()
    comb = combinations(numbers, 6)
    for c in comb:
        print(*c)
    print()