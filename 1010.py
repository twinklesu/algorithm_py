t = int(input())

def factorial(n):
    ans = 1
    for i in range(1, n+1):
        ans *= i
    return ans

for _ in range(t):
    n, m = map(int, input().split())
    ans = factorial(m)//(factorial(n)*factorial(m-n))
    print(ans)