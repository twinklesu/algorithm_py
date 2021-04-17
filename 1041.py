from itertools import combinations

n = int(input())
diceNum = list(map(int, input().split()))

if n == 1:
    diceNum.sort()
    print(sum(diceNum[:-1]))
else:
    min1 = min(diceNum[0], diceNum[5])
    min2 = min(diceNum[1], diceNum[4])
    min3 = min(diceNum[2], diceNum[3])

    twoMin = min([min1+min2, min2+min3, min3+min1])
    threeMin = min1+min2+min3

    ans = 0
    # 가운데
    ans += (n - 2) * (n - 2) * 5 * min(diceNum)
    # 아래 테두리
    ans += (n - 2) * 4 * min(diceNum)
    # 위 꼭지점
    ans += threeMin * 4
    # 기둥
    ans += twoMin * (n - 1) * 4
    # 위 테두리
    ans += twoMin * (n - 2) * 4

    print(ans)
