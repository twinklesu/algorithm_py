from itertools import permutations

n, m = map(int, input().split())

num = list(range(1,n+1))

per = permutations(num, m)

for p in per:
    for pp in p:
        print(pp, end=' ')
    print()