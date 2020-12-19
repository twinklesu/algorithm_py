a,b,c = map(int, input().split())
base = a
for _ in range(b):
    if a >= c:
        a%=c
    a*base

print(a)