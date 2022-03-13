from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        closeToOpen = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        for letter in s:
            if letter in "({[":
                stack.append(letter)
            else:
                if stack and stack[-1] == closeToOpen[letter]:
                    stack.pop()
                else:
                    return False
        if stack:
            # 마지막인데 차 있으면
            return False
        return True