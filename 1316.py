n = int(input())

count = 0
for _ in range(n):
    word = input()
    alphaList = []
    l = len(word)
    for i, w in enumerate(word[:-1]):
        if w in alphaList:
            break
        elif w != word[i+1]:
            alphaList.append(w)
    else:
        if word[-1] not in alphaList:
            count += 1

print(count)
