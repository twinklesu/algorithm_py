n , m = map(int, input().split())
li = list(map(int, input().split()))

maxsum = 0
for a in range(n):
    for b in range(a+1,n):
        for c in range(b+1,n):
            summ = sum([li[a], li[b], li[c]])
            if summ <= m and summ > maxsum:
                maxsum = summ
print(maxsum)

