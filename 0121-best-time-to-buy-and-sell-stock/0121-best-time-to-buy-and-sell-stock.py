class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 
        min_num = prices[0]
        for num in prices:
            if num > min_num:
                profit = max(profit, num - min_num)
            else:
                min_num = num

        return profit

        