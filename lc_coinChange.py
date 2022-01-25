class Solution:
    def coinChange(self, coins, amount: int) -> int:
        if amount > 0:
            maxi = 10**4+1
            dp = [maxi for _ in range(amount+1)]
            dp[0] = 0
            new_coin = []
            for coin in coins:
                if coin <= amount:
                    new_coin.append(coin)
            if new_coin:
                for target in range(min(new_coin), amount+1):
                    for coin in new_coin:
                        if dp[target-coin] < maxi:
                            dp[target] = min(dp[target], dp[target-coin]+1)
            if dp[amount] == maxi:
                return -1
            else:
                return dp[amount]
        else:
            return 0