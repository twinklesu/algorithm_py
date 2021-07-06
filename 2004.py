n, m = map(int, input().split())

nFive = n//5
countFive = [1]*(nFive+1)
countFive[0] = 0
five = 5
while five <= nFive:
    for i in range(five, nFive+1, five):
        countFive[i] += 1
    five *= 5

mFive = m//5
t = n-m
tFive = t//5

zeroN = sum(countFive)
zeroM = sum(countFive[:mFive+1])
zeroT = sum(countFive[:tFive+1])

print(zeroN-zeroM-zeroT)