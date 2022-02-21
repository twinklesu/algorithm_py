from collections import defaultdict


def isAnagram(s: str, t: str) -> bool:
    letter = defaultdict(int)
    for le in s:
        letter[le] += 1

    for le in t:
        letter[le] -= 1

    return all(count == 0 for count in letter.values())


s = "anagram"
t = "nagaram"
print(isAnagram(s, t))