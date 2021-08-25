from collections import defaultdict
import sys
sys.setrecursionlimit(5000)

# 백트래킹 dfs
code = input()
n = len(code)
code = int(code)
memo = defaultdict(int)
for i in range(1, 10):
    memo[i] = 1
for i in range(10, 27):
    memo[i] = 2
memo[10] = 1
memo[20] = 1


def dfs(code: int, n: int):
    if code//(10**(n-1)) < 1:
        return 0
    if code in memo:
        return memo[code]
    if 9 < code//(10**(n-2)) < 27:
        memo[code] += dfs(code%(10**(n-2)), n-2)
    # 한자리 검사
    if 0 < code//(10**(n-1)):
        memo[code] += dfs(code%(10**(n-1)), n-1)
    memo[code] %= 1000000
    return memo[code]


print(dfs(code, n))


