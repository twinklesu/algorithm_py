def dfs(lenPermu, nums, n, permu):
    global maxSum
    if lenPermu == n:
        summed = 0
        for i in range(n-1):
            summed += abs(permu[i]-permu[i+1])
        maxSum = max(maxSum, summed)
        return
    lenPermu += 1
    for num in nums:
        if num not in permu:
            dfs(lenPermu, nums, n, permu+[num])



def main():
    global maxSum
    n = int(input())
    nums = list(map(int, input().split()))
    maxSum = 0
    dfs(0, nums, n, [])
    print(maxSum)



main()