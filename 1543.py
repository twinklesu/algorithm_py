doc = input()
word = input()
lenD = len(doc)
lenW = len(word)

maxCount = 0
for start in range(lenD-lenW+1):
    temp = doc[start:]
    count = 0
    i = 0
    while i < len(temp):
        if temp[i:i+lenW] == word:
            count += 1
            i += lenW
        else:
            i += 1
    if count > maxCount or start == 0:
        maxCount = count

print(maxCount)
