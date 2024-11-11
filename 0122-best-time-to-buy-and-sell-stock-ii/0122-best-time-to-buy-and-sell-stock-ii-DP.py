class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[0 for _ in range(len(prices))] for _ in range(2)]
        dp[0][0] = -prices[0]   # holding
        dp[1][0] = 0            # not holding

        for i in range(1, len(prices)):
            dp[0][i] = max(dp[0][i-1], dp[1][i-1] - prices[i])
            dp[1][i] = max(dp[1][i-1], dp[0][i-1] + prices[i])
        
        return dp[1][len(prices)-1]


