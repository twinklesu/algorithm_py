class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if N > 1:
            dp = [[0,0] for _ in range(N)]
            dp[0][0] = nums[0]
            dp[1][1] = nums[0]
            dp[1][0] = nums[1]

            for i in range(2, N):
                dp[i][0] = max(dp[i-2]) + nums[i]
                dp[i][1] = dp[i-1][0]

            return max(dp[-1])
        else:
            return max(nums)