class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0 for _ in range(target + 1)]  # placeholder 0
        for n in nums:
            if n <= target:
                dp[n] += 1

        for i in range(2, target + 1):
            for j in range(i):
                if dp[j] and i - j in nums:
                    dp[i] += dp[j]

        return dp[-1]
