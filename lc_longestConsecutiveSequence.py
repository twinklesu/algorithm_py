class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums:
            nums = sorted(list(set(nums)))
            N = len(nums)
            dp = [1 for _ in range(N)]

            for i in range(1, N):
                if nums[i] == nums[i-1]+1:
                    dp[i] = dp[i-1] + 1

            return max(dp)
        else:
            return 0