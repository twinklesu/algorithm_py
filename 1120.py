a, b = map(str, input().split())

len_a = len(a)
len_b = len(b)
word_list = []
for i in range(len_b - len_a + 1):
    word_list.append(b[i:i+len_a])

min_diff = len_a
for word in word_list:
    diff = 0
    for w1, w2 in zip(word, a):
        if w1 != w2:
            diff += 1
    if diff < min_diff:
        min_diff = diff

print(min_diff)