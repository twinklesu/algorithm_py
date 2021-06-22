m, n = map(int, input().split())

sieve = [True for _ in range(n+1)]

sqrtN = int(n**0.5)
for i in range(2, sqrtN+1):
    if sieve[i]:
        for j in range(i+i, n+1, i):
            sieve[j] = False


# for isPrime, num in zip(sieve[2:], range(2, n+1)):
#     if num >= m and isPrime:
#         print(num)

for isPrime, num in zip(sieve[m:], range(m, n+1)):
    if isPrime:
        print(num)