# longest substring을 담는 `substr`
# `s`를 순회하면서 `substr`에 없는 문자일 시 뒤에 더함
# 이미 존재할 경우 `substr`에서 처음~중복문자를 제거하고, 뒤에 새 문자 더해서 반복
# `substr`이 truncate되기 전에 길이가 최대인지 확인. 최대일 경우 길이 저장.

def lengthOfLongestSubstring(self, s: str) -> int:
    substr = ""
    longestLen = 0
    for letter in s:
        if letter not in substr:
            substr += letter
        else:
            ind = substr.index(letter)
            if len(substr) > longestLen:
                longestLen = len(substr)
            substr = substr[ind + 1:]
            substr += letter
    if len(substr) > longestLen:
        longestLen = len(substr)
    return longestLen