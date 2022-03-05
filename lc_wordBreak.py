from collections import deque


class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        global ans
        ans = False
        wordLen = dict()
        for word in wordDict:
            wordLen[word] = len(word)

        # bfs
        q = deque()
        q.append(s)
        visited = set()
        while q:
            thisS = q.popleft()
            if thisS == "":
                return True
            for word, wLen in zip(wordLen, wordLen.values()):
                if thisS[:wLen] == word:
                    if thisS[wLen:] not in visited:
                        visited.add(thisS[wLen:])
                        q.append(thisS[wLen:])

        return False

