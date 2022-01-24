from collections import defaultdict


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start, end = 0, 1
        memory = defaultdict(int)
        maxiLen = 0
        thisLen = 1
        lenS = len(s)

        memory[s[start]] += 1

        while end < lenS:
            if thisLen - max(memory.values()) <= k:
                # possible to extend
                maxiLen = max(maxiLen, thisLen)
                memory[s[end]] += 1
                end += 1
                thisLen += 1
            else:
                # shrink the length
                memory[s[start]] -= 1
                start += 1
                thisLen -= 1
        if thisLen - max(memory.values()) <= k:
            maxiLen = max(maxiLen, end - start)
        return maxiLen