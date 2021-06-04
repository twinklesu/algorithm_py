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


def binarySearch(start, end, prices):
    mid = (start+end)//2

    if start == mid:
        return min(start, max(prices))

    total = computeTotal(prices, mid)
    if total > money:
        return binarySearch(start, mid, prices)
    elif total == money:
        return mid
    else:
        return binarySearch(mid, end, prices)



print(binarySearch(1, money+1, prices))
