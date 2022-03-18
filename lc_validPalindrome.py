import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        pattern = re.compile('[a-z0-9]')
        newS = ''.join(pattern.findall(s))

        if newS == newS[::-1]:
            return True
        else:
            return False
