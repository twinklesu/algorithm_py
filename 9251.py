str1 = list(map(str, input()))
str2 = list(map(str, input()))
len1 = len(str1)
len2 = len(str2)

dp = [[0 for _ in range(len1+1)] for _ in range(len2+1)]

for i in range(1, len2+1): # 0 행은 place holder
    for j in range(1, len1+1): # 0 열은 place holder
        if str2[i-1] == str1[j-1]: # dp의 0행0열이 place holder라서 dp[1][1]이 str1[0] 과 str2[0]을 위한 자리
            dp[i][j] = dp[i-1][j-1] + 1 # 왼쪽 사선 위 +1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j]) # 왼쪽과 위쪽 중 max


print(dp[-1][-1])