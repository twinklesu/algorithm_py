from math import gcd

n = int(input())
numbers = list(map(int, input().split()))

numerator = numbers[0]
for num in numbers[1:]:
    divisor = gcd(numerator, num)
    print(numerator//divisor, '/', num//divisor, sep='')
