from collections import defaultdict
import sys
sys.setrecursionlimit(10**9)


input = sys.stdin.readline
n = int(input())

tree = defaultdict(list)
for _ in range(n-1):
    u, v = map(int, input().split())
    tree[u].append(v)
    tree[v].append(u)
dp = [[0, 0] for _ in range(n+1)]
visited = [False for _ in range(n+1)]

visited[1] = True


def dfs(root: int):
    dp[root][0] = 1
    visited[root] = True
    for leaf in tree[root]:
        if not visited[leaf]:
            dfs(leaf)
            dp[root][0] += min(dp[leaf])
            dp[root][1] += dp[leaf][0]


dfs(1)
print(min(dp[1]))
