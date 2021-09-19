import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

fixedSeat = []
for _ in range(m):
    fixedSeat.append(int(input()))

dp = dict()
dp[0] = 1
dp[1] = 1
dp[2] = 2

def dynamic(n):
    if n in dp:
        return dp[n]
    for i in range(max(dp)+1, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]


fixedSeat.sort()
start = 1
end = 0
ans = 1
for f in fixedSeat:
    end = f
    ans *= dynamic(end-start)
    start = end+1
ans *= dynamic(n-start+1)
print(ans)