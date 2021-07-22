memoization = [0, 1, 2, 4]
lenMem = 4

t = int(input())
for _ in range(t):
    n = int(input())
    while n >= lenMem:
        memoization.append(sum(memoization[lenMem-3:])%1000000009)
        lenMem += 1
    if n < lenMem:
        print(memoization[n])
