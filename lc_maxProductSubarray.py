class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        N = len(nums)
        minProduct = nums[0]
        maxProduct = nums[0]
        maxi = maxProduct

        for i in range(1, N):
            product = set()
            product.add(minProduct * nums[i])
            product.add(maxProduct * nums[i])
            product.add(nums[i])

            minProduct = min(product)
            maxProduct = max(product)

            maxi = max(maxi, maxProduct)

        return maxi