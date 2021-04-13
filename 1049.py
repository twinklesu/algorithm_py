n, m = map(int, input().split())
bundle = []
sample = []
for _ in range(m):
    line = list(map(int, input().split()))
    bundle.append(line[0])
    sample.append(line[1])


bundleNum = n//6
sampleNum = n % 6

cost = 0

cost += min(bundle + [x*6 for x in sample]) * bundleNum
cost += min(bundle + [x*sampleNum for x in sample])

print(cost)
