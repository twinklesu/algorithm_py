def hanoi(n, a, b, c):  # a 를 c로
    global count
    if n == 0:
        return
    hanoi(n - 1, a, c, b)  # a 를 b로
    ans.append(str(a) + ' ' + str(c))
    count += 1
    hanoi(n - 1, b, a, c)  # b를 c로


n = int(input())

if n > 4:
    # 횟수만 출력하기
    # dp = [0 for _ in range(n+1)]
    # for i in range(1, n+1):
    #     dp[i] = dp[i-1]*2 + 1
    # print(dp[-1])
    print(2**n -1)
else:
    ans = []
    global count
    count = 0

    hanoi(n, 1, 2, 3)
    print(count)
    print('\n'.join(ans))