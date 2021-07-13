from itertools import combinations_with_replacement

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
comb = list(set(combinations_with_replacement(numbers, m)))
comb.sort()
for c in comb:
    print(*c)

