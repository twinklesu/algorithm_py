n = int(input())
k = len(str(n))

count = 0
for i in range(1, k):
    count += i * 9 * 10**(i-1)

count += k * (n - 10**(k-1) + 1)

print(count)