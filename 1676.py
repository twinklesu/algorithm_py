n = int(input())
ans = 0
for i in range(5,n+1,5):
    if i%125 == 0:
        ans += 3
    elif i%25 == 0:
        ans += 2
    else:
        ans += 1
print(ans)
