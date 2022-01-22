# DP
def maxProfit_dp(prices) -> int:
    length = len(prices)
    minBuy = [0 for _ in range(length)]
    maxProfit = 0

    minBuy[0] = prices[0]

    for day, price in enumerate(prices):
        if day == 0:
            pass
        else:
            maxProfit = max(price - minBuy[day - 1], maxProfit)  # does today's selling make the best profit?
            minBuy[day] = min(minBuy[day - 1], price)  # Is today's price lowest buying price?
    return maxProfit


# BruteForce
def maxProfit_brute(prices) -> int:
    maxiProfit = 0
    for i, selling in enumerate(prices):
        if i > 1:
            for j, buying in enumerate(prices[:i]):
                maxiProfit = max(maxiProfit, selling - buying)
    return maxiProfit

