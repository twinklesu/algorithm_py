import sys
input = sys.stdin.readline


def main():
    n = int(input())
    prices = list(map(int, input().strip().split()))
    prices.sort()
    money = int(input())

    if sum(prices) <= money:
        return prices[-1]

    for i in range(n-1, 1, -1):
        totalUsed = sum(prices[:i])
        if totalUsed < money:
            left = money - totalUsed
            limitedPrice = left//(n-i)
            if limitedPrice >= prices[i-1]:
                return limitedPrice

    # i === 0에 줘야할때 3인데 1씩주는는
    return money//n


print(main())
