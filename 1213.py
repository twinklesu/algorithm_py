name = input()
letter = dict()

for n in name:
    if n in letter:
        letter[n] += 1
    else:
        letter[n] = 1

oddNum = 0
oddLetter = ''
oddLetterNum = 0
for value, key in zip(letter.values(), letter.keys()):
    if value%2 != 0:
        oddNum += 1
        oddLetter = key
        oddLetterNum = value
if oddNum > 1:
    print("I'm Sorry Hansoo")
else:
    if oddLetterNum == 1:
        letter.pop(oddLetter)
    elif oddLetterNum > 1:
        letter[oddLetter] -= 1
    sorted_letter = list(letter.keys())
    sorted_letter.sort()
    ans = ''
    for w in sorted_letter:
        ans += w*(letter[w]//2)
    ans = ans + oddLetter + ans[::-1]
    print(ans)

# aaabb의 경우 홀수를 그냥 가운데로 넣어버리면 baaab가 되는데 ababa가 앞선다.
# 따라서 홀수의 경우 1개만 빼서 짝수와 같이 처리하고, 1개는 그냥 가운데 넣음.