n = int(input())
prices = list(map(int, input().split()))
money = int(input())


def computeTotal(prices, limit):
    total = 0
    for p in prices:
        if p > limit:
            total += limit
        else:
            total += p
    return total


def binarySearch(start, end, money, prices):
    while True:
        mid = (start + end) // 2
        total = computeTotal(prices, mid)
        if total > money:
            end = mid -1
        elif total == money or mid == end:
            return mid
        else:
            start = mid +1


maxi = max(prices)
print(binarySearch(0, maxi, money, prices))
