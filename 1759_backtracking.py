def backTrack(letters, comb, t, l, length, ind):
    global ans
    if length == t:
        count = 0
        for vowel in 'aeiou':
            if vowel in comb:
                count += 1
        if 1 <= count <= t-2:
            ans.append(comb)
        return
    for i in range(ind+1, l):
        backTrack(letters, comb+letters[i], t, l, length+1, i)


def main():
    global ans
    t, l = map(int, input().split())
    letters = list(map(str, input().split()))
    letters.sort()

    ans = []
    for ind in range(l-t+1):
        backTrack(letters, letters[ind], t, l, 1, ind)

    for a in ans:
        print(a)


main()
