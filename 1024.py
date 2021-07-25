def adding(a,b):
    return b*(b+1)//2 - a*(a-1)//2


n, l = map(int, input().split())
start = n//2
end = start + l -1
while start >= 0 and end-start<100:
    if adding(start, end) == n:
        print(*range(start, end+1))
        break
    elif adding(start, end) < n:
        start -= 1
    else:
        start -= 1
        end -= 1
else:
    print(-1)