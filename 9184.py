import sys
input = sys.stdin.readline

memoization = dict()

def w(a:int, b:int, c: int):
    if (a,b,c) in memoization:
        return memoization[(a,b,c)]
    if a <= 0 or b<=0 or c<=0:
        memoization[(a,b,c)] = 1
        return 1
    elif a>20 or b>20 or c>20:
        return 1048576
    elif a<b<c:
        memoization[(a,b,c)] = w(a,b,c-1) + w(a,b-1,c-1) - w(a,b-1,c)
        return memoization[(a,b,c)]
    else:
        memoization[(a, b, c)] =w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return memoization[(a, b, c)]


while True:
    a,b,c = list(map(int, input().split()))
    if a == -1 and b== -1 and c == -1:
        break
    ans = w(a,b,c)
    print("w(", a, ", ", b, ", ", c, ") = ", ans, sep='')

