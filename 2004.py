n, m = map(int, input().split())

nFive = n//5
countFive = list(range(nFive+1))
five = 5
while five <= nFive:
    for i in range(five, nFive+1, five):
        countFive[i] += 1
    five *= 5

mFive = m//5
t = n-m
tFive = t//5

zeroN = countFive[-1]
zeroM = countFive[mFive]
zeroT = countFive[tFive]

print(zeroN-zeroM-zeroT)