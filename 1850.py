# from math import gcd

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)


n, m = map(int, input().split())
gcdNum = 0
if n <= m:
    gcdNum = gcd(m, n)
else:
    gcdNum = gcd(n, m)
print('1'*gcdNum)