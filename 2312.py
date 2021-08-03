t = int(input())
for _ in range(t):
    n = int(input())
    k = 2
    num = n
    count = 0
    while k <= n and num >= k:
        if num%k == 0:
            num//= k
            count += 1
        else:
            if count > 0:
                print(k, count)
            k += 1
            count = 0
    if count > 0:
        print(k, count)
