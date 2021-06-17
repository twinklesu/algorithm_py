n, k = map(int, input().split())
count = 0
money = [int(input()) for _ in range(n)]

for cash in money[::-1]:
    if cash <= k:
        count += k//cash
        k %= cash
    if k == 0:
        break

print(count)

