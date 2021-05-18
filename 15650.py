from itertools import combinations

n, m = map(int, input().split())
num = list(range(1,n+1))
comb = combinations(num, m)

for c in comb:
    sorted_c = sorted(c)
    for s in sorted_c:
        print(s, end=' ')
    print()