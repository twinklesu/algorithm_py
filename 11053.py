def solution(n, arr):
    dp = [0 for _ in range(n)]
    dp[0] = 1
    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i] and dp[j] > dp[i]:
                dp[i] = dp[j]
        dp[i] += 1 # 이전의 것에다 +1 이거나, 0에다 +1
    return(max(dp))




def main():
    n = int(input().rstrip())
    arr = list(map(int, input().split()))
    print(solution(n, arr))


main()
