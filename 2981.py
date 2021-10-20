from math import gcd, sqrt

n = int(input())
numbers = []
prev = int(input())
for _ in range(n-1):
    this = int(input())
    numbers.append(abs(prev - this))
    prev = this

gcdNum = numbers[0]
for i in range(1, n-1):
    gcdNum = gcd(numbers[i], gcdNum)

# 최대공약수의 약수 구하기
division = set() # 25의 경우 55 떄문에 duplicate 발생
for i in range(2, int(sqrt(gcdNum))+1):
    if gcdNum%i == 0:
        division.add(i)
        division.add(gcdNum//i)
division.add(gcdNum)
division = list(division)
division.sort()

print(*division)

