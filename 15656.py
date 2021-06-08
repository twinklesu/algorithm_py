from itertools import product

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

perm = product(numbers, repeat=m)
for p in perm:
    for pp in p:
        print(pp, end=' ')
    print()
