class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        min_num = prices[0]
        for num in prices:
            profit = max(profit, num - min_num)
            if num < min_num:
                min_num = num

        return profit
        
        