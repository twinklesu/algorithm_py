# 이항계수
from math import factorial

n, k = map(int, input().split())
ans = factorial(n)//factorial(k)//factorial(n-k)
print(ans%10007)