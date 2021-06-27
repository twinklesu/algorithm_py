from itertools import combinations

t, l = map(int, input().split())
letters = list(map(str, input().split()))
letters.sort()

aeiou = ['a', 'e', 'i', 'o', 'u']
comb = combinations(letters, t)
for c in comb:
    count = 0
    for ae in aeiou:
        if ae in c:
            count += 1
    if 1 <= count <= t-2:
        print(''.join(c))