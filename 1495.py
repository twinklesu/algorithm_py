n, s, m = map(int, input().split())
v = set()
for i in input().split():
    i = int(i)
    v.add(i)
    v.add(-i)

v = list(v)
v.sort(reverse=True)
ans = -1

dp = [0 for _ in range(m+1)]
dp[s] = 1
for _ in range(n):
    new_dp = [0 for _ in range(m+1)]
    for i in range(1, m+1):
        if dp[i]:
            for vv in v:
                if 0<= i + vv <= m:
                    new_dp[i+vv] = 1
    dp = new_dp

for i in range(m, -1, -1):
    if dp[i]:
        print(i)
        break
else:
    print(-1)