n = int(input())

before = [0,1,1,1,1,1,1,1,1,1]

if n ==1:
    print(sum(before))
else:
    now = [0 for _ in range(10)]
    for _ in range(1, n):
        now[0] = before[1]
        now[9] = before[8]
        for i in range(1, 9):
            now[i] = (before[i-1] + before[i+1])
        before = now.copy()
    print(sum(before)%(10**9))
