from collections import defaultdict



def minWindow(s: str, t: str) -> str:
    countDict = defaultdict(int)
    for letter in t:
        countDict[letter] += 1

    lenS = len(s)
    start = 0
    end = 0
    if s[start] in countDict:
        countDict[s[start]] -= 1

    minLen = 10 ** 5 + 1
    minStr = ""
    while start <= end < lenS:
        # t의 모든 글자를 포함하는 substring
        if all(value <= 0 for value in countDict.values()):
            thisLen = end - start + 1
            if thisLen < minLen:
                minLen = thisLen
                minStr = s[start:end + 1]
            if s[start] in countDict:
                countDict[s[start]] += 1
            start += 1
        else:
            # substring에 t의 모든 글자가 들어가지 않아
            # end만 +1 해서 길이 늘려줌
            end += 1
            if end < lenS and s[end] in countDict:
                countDict[s[end]] -= 1
    return minStr

s = "a"
t = "aa"
print(minWindow(s, t))

