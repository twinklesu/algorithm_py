from collections import defaultdict
def characterReplacement(s: str, k: int) -> int:
    start, end = 0, 1
    memory = defaultdict(int)
    maxiLen = 0

    memory[s[start]] += 1
    while start <= end < len(s):
        thisLen = end - start
        if thisLen - max(memory.values()) <= k:
            # possible to extend
            maxiLen = max(maxiLen, thisLen)
            memory[s[end]] += 1
            end += 1
        else:
            # shrink the length
            memory[s[start]] -= 1
            start += 1
    if end - start - max(memory.values()) <= k:
        maxiLen = max(maxiLen, end-start)
    return maxiLen

s = "ABAA"
k = 0
print(characterReplacement(s,k))