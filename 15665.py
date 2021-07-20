from itertools import product

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

perm = list(set(product(numbers, repeat=m)))
perm.sort()
for p in perm:
    print(*p)