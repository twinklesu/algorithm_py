class Solution:
    def containsDuplicate(self, nums) -> bool:
        return False if len(nums) == len(set(nums)) else True