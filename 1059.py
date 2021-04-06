l = int(input())
s = list(map(int, input().split()))
n = int(input())

s.sort()
small = 0
big = 0

if s[0] > n:
    small = 1
    big = s[0]
else:
    for ind, el in enumerate(s):
        if el > n:
            small = s[ind-1] +1
            big = el
            break


num = list(range(small, big))
count = 0
for ind, el in enumerate(num):
    for j in range(ind+1, len(num)):
        if el <= n <= num[j]:
            count += 1

print(count)