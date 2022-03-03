class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp로 생각해보자...
        N = len(nums)
        dp = [0 for _ in range(N)]

        for ind, el in enumerate(nums):
            dp[ind] = max(dp[ind - 1] + nums[ind], nums[ind])

        return max(dp)