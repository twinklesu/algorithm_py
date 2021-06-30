from collections import deque

def dfs(lenPermu, summed, nums, n, permu):
    global maxSum
    if lenPermu == n:
        maxSum = max(summed, maxSum)
        return
    lenPermu += 1
    for num in nums:
        if num not in permu:
            dfs(lenPermu, summed+num, nums, n, permu+[num])



def main():
    global maxSum
    n = int(input())
    nums = list(map(int, input().split()))
    maxSum = 0
    dfs(0, 0, nums, n, [])
    print(maxSum)



main()