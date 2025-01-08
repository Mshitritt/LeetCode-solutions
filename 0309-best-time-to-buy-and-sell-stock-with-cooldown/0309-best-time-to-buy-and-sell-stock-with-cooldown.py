class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        dp = {}

        def dfs(i, buy):
            # buy = 1 - if we boght 
            # but = 0 - if we sold
            if i >= len(prices):
                return 0
            if (i, buy) in dp:
                return dp[(i, buy)]
            
            if buy:
                buy = dfs(i+1, 0) - prices[i]
                keep = dfs(i+1, 1)
                dp[(i, buy)] = max(buy, keep)
                return dp[(i, buy)]
            else:
                sell = dfs(i+2, 1) + prices[i]
                keep = dfs(i+1, 0)
                dp[(i, buy)] = max(sell, keep)
                return dp[(i, buy)]

        
        return dfs(0, 1) 
                

