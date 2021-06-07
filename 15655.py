from itertools import combinations

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
comb = list(combinations(numbers, m))


for c in comb:
    for cc in c:
        print(cc, end=' ')
    print()

