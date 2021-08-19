import sys
input = sys.stdin.readline

a,b,c = map(int, input().split())

ans = 1
for _ in range(b):
    ans*=a
    ans%=c
print(ans)
