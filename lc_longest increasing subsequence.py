class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lenNums = len(nums)
        dp = [1 for _ in range(lenNums)]

        for i in range(1, lenNums):
            for j in range(i):
                if nums[j] < nums[i] and dp[j] >= dp[i]:
                    dp[i] = dp[j] + 1

        return max(dp)