n = int(input())
li = []
for _ in range(n):
    li.append(int(input()))

for i in range(len(li), 1, -1):
    flipped = False
    for j in range(i-1):
        if li[j] > li[j+1]:
            temp = li[j]
            li[j] = li[j+1]
            li[j+1] = temp
            flipped = True
    if not flipped:
        break

for i in li:
    print(i)