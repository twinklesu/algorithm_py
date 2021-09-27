n = int(input())
k = int(input())

start = 1
end = k

while start <= end:
    mid = (start+end)//2
    ith = 0
    for i in range(1, n+1):
        ith += min(mid//i, n)
    if ith <= k:
        start = mid +1
    else:
        end = mid -1

print(mid)