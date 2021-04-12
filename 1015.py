n = int(input())
a = map(int, input().split())
numLi = list(range(n))
p = [[a_, p_] for a_, p_ in zip(a, numLi)]
p.sort()
pp = [p_[1] for p_ in p]
ppp = [[pp, i] for pp, i in zip(pp, range(n))]
ppp.sort()
ans = [p_[1] for p_ in ppp]
print(str(ans)[1:-1].replace(',',''))