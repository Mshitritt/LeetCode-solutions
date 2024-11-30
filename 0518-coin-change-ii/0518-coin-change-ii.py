class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp=[0]*(amount+1)
        dp[0]=1
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i]=dp[i]+dp[i-coin]
        return dp[amount]
        
        """
        dp = [[0 for _ in range(amount+1)] for _ in range(2)]
        
        dp[0][0] = 1
        dp[1][0] = 1
        
        for a in range(amount+1):
            if a-coins[0] >= 0:
                dp[0][a] += dp[0][a-coins[0]]
        

        for c in range(1, len(coins)):
            dp[0][0] = 1
            dp[1][0] = 1
            for a in range(1, amount+1):
                if a-coins[c] >= 0:
                    dp[1][a] += dp[0][a] + dp[1][a-coins[c]]
                else:
                    dp[1][a] += dp[0][a]

            # swap lines 
            for i in range(amount+1):
                dp[0][i], dp[1][i] = dp[1][i], 0
            
        
        return dp[0][amount]
        """

            

        
        for r in dp:
            print(r)
        
        return dp[-1][amount]
                

            

                