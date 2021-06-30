from itertools import permutations

n = int(input())
nums = list(map(int, input().split()))
perm = permutations(nums)

maxSum = 0
for p in perm:
    summed = 0
    for i in range(n-1):
        summed += abs(p[i]-p[i+1])
    maxSum = max(maxSum, summed)

print(maxSum)