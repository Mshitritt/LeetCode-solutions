class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins))]
        # dp[c][amount] = number of ways to get amount by first c coins
        
        # initilaize
        for i in range(len(coins)):
            dp[i][0] = 1
        
        for a in range(1, amount+1):
            
            for c in range(len(coins)):
                coin = coins[c]
                if c == 0:
                    dp[c][a] = dp[c][a-coin] if a >= coin else 0
                else:
                    dp[c][a] = dp[c-1][a]
                    dp[c][a] += dp[c][a-coin] if a >= coin else 0
        

        return dp[len(coins)-1][amount]
        """
        # all premetuations
        for a in range(1, amount + 1):
            for coin in coins:
                dp[a] += dp[a - coin] if a >= coin else 0
        return dp[amount]
        """
        


