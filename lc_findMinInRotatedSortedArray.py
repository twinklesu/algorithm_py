from heapq import heappop, heappush
class Solution:
    def findMin(self, nums: List[int]) -> int:
        heap = []
        for n in nums:
            heappush(heap, n)
        return heappop(heap)