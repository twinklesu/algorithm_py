from itertools import combinations

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
comb = list(set(combinations(numbers, m)))
comb.sort()
for c in comb:
    print(*c)