import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
broken = list(map(int, input().split()))

minClick = abs(n-100) # 현위치 100에서 +,-로 이동하는 횟수
if m == 10:
    print(minClick)
else:
    for k in range(10**6):
        unableNum = set(broken).intersection(set(map(int, str(k))))
        if not unableNum:
            numClick = len(str(k))
            numClick += abs(n-k)
            if k > n and numClick > minClick:
                break
            minClick = min(minClick, numClick)

    print(minClick)