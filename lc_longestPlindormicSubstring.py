class Solution:
    def longestPalindrome(self, s: str) -> str:
        N = len(s)
        for length in range(N, 1, -1):
            for start in range(0, N - length + 1):
                if s[start] == s[start + length - 1]:
                    if isPalin(s[start:start + length]):
                        return s[start:start + length]
        return s[0]


def isPalin(s):
    if s == s[::-1]:
        return True
    else:
        return False