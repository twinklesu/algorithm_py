n = int(input())
glass = []
for _ in range(n):
    glass.append(int(input()))

acc_wine = [[] for _ in range(n)]

if n == 1:
    print(glass[0])
elif n==2:
    print(sum(glass))
else:
    acc_wine[0].extend([0, glass[0]])
    acc_wine[1].extend([glass[0] + glass[1], glass[1]])

    maxi = glass[0]
    for i in range(2,n):
        one_before = acc_wine[i-1][1]
        acc_wine[i].append(one_before+glass[i])
        acc_wine[i].append(maxi+glass[i])

        maxi = max([maxi] + acc_wine[i-1])

    print(max(max(acc_wine[-1]),max(acc_wine[-2])))