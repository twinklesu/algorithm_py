from itertools import permutations

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

perm = permutations(numbers, m)
for p in perm:
    for pp in p:
        print(pp, end=' ')
    print()