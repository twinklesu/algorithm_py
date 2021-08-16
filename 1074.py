n, r, c = map(int, input().split())

ans = 0
def solution(n: int, r: int, c: int):
    global ans
    ans *= 4
    if n == 1:
        if r == 0:
            if c == 0:
                return
            else:
                ans += 1
                return
        else:
            if c == 0:
                ans += 2
                return
            else:
                ans += 3
                return
    n -= 1
    k = 2**n
    if r < k:
        if c < k:
            # 2사분면 / 0
            return solution(n, r, c)
        else:
            # 1사분면 / 1
            ans += 1
            return solution(n, r, c-k)
    else:
        if c < k:
            # 3사분면 / 2
            ans += 2
            return solution(n, r-k, c)
        else:
            # 4사분면 / 3
            ans += 3
            return solution(n, r-k, c-k)


solution(n, r, c)
print(ans)
