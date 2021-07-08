from itertools import permutations

n, m = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
perm = list(set(permutations(numbers, m)))
perm.sort()

for p in perm:
    print(*p)