class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [[float('-inf')] * 5 for _ in range(len(prices))]
        # Initialize first day
        dp[0][0] = 0           # Start with no stock
        dp[0][1] = -prices[0]  # Buy on first day
        dp[0][2] = float('-inf')  # Can't complete a transaction on day 1
        dp[0][3] = float('-inf')  # Can't be in middle of second transaction
        dp[0][4] = float('-inf')  # Can't complete two transactions on day 1

        for i in range(1, len(prices)):
            price = prices[i]
            # s0: No stock, 0 transactions
            dp[i][0] = dp[i-1][0]  # hold

            # s1: Have stock, 0 transactions
            dp[i][1] = max(
                dp[i-1][1],          # hold
                dp[i-1][0] - price)  # buy

            # s2: No stock, 1 transaction
            dp[i][2] = max(
                dp[i-1][2],          # hold
                dp[i-1][1] + price)  # sell

            # s3: Have stock, 1 transaction
            dp[i][3] = max(
                dp[i-1][3],          # hold
                dp[i-1][2] - price)  # buy

            # s4: No stock, 2 transactions
            dp[i][4] = max(
                dp[i-1][4],          # hold
                dp[i-1][3] + price)  # sell

        n = len(prices)
        return max(dp[n-1][0], dp[n-1][1], dp[n-1][2], dp[n-1][3], dp[n-1][4])


        