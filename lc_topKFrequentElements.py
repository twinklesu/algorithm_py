from collections import defaultdict

    def topKFrequent(nums, k):
        # counting frequency
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        # sort by frequency
        li = [[num, freq[num]] for num in freq]
        li.sort(key=lambda x: x[1], reverse=True)
        ans = [el[0] for el in li]

        return ans[:k]