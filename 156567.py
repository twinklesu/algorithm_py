from itertools import combinations_with_replacement

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
comb = combinations_with_replacement(numbers, m)

for c in comb:
    for cc in c:
        print(cc, end=' ')
    print()
