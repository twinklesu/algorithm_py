word = input()

def reorg(a,b,c):
    return a[::-1]+b[::-1]+c[::-1]

l = len(word)
ans = ''
for i in range(1,l-2):
    for j in range(i+1,l):
            new_word = reorg(word[:i],word[i:j], word[j:])
            if ans == '':
                ans = new_word
            elif ans > new_word:
                ans = new_word

print(ans)