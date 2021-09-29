import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
count = 0

dpLast = [0 for _ in range(21)]
dpLast[numbers[0]] += 1

for num in numbers[1:-1]:
    dp = [0 for _ in range(21)]
    for i in range(21):
        if dpLast[i]:
            if i-num >= 0:
                dp[i-num] += dpLast[i]
            if i+num <= 20:
                dp[i+num] += dpLast[i]
    dpLast = dp.copy()

print(dpLast[numbers[-1]])