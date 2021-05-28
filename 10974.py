from itertools import permutations
n = int(input())
numbers = list(range(1, n+1))
perm = permutations(numbers, n)
for p in perm:
    print(str(p)[1:-1].replace(',',''))